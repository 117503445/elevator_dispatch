using elevator_dispatch_GUI.models;

using Newtonsoft.Json;

using System;
using System.Collections.Generic;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace elevator_dispatch_GUI
{
    /// <summary>
    /// WdMain.xaml 的交互逻辑
    /// </summary>
    public partial class WdMain : Window
    {

        public WdMain()
        {
            InitializeComponent();
        }
        private readonly List<FrameworkElement> tempElements = new List<FrameworkElement>();
        private void JsonToUI(string json)
        {
            Console.WriteLine(json);
            var algorithmResult = JsonConvert.DeserializeObject<AlgorithmOutput>(json);

            for (int i = 0; i < 21; i++)
            {
                string s;
                if (i <= 2)
                {
                    s = $"{i - 3}F";
                }
                else
                {
                    s = $"{i - 2}F";

                }
                TextBlock tb = new TextBlock
                {
                    Text = s,
                    FontSize = 16,
                    FontWeight = FontWeight.FromOpenTypeWeight(600)

                };
                Canvas.SetLeft(tb, 110 + i * 80);
                CvsMain.Children.Add(tb);
                tempElements.Add(tb);
            }//生成楼层告示

            var ImgElevators = new List<Image>();//生成3个电梯
            for (int i = 0; i < algorithmResult.Elevators.Length; i++)
            {
                var e = algorithmResult.Elevators[i];
                Image im = new Image
                {
                    Source = new BitmapImage(new Uri("pack://application:,,,/resource/elevator.jpg")),
                    Width = 80,
                    Height = 112,
                    Opacity = 0.5
                };

                Canvas.SetTop(im, 200 + i * 120);
                Canvas.SetLeft(im, e.current_floor * 80 + 80);
                CvsMain.Children.Add(im);
                ImgElevators.Add(im);
                tempElements.Add(im);
            }

            var UnigridElevators = new List<UniformGrid>();//3个电梯的 UniformGrid
            for (int i = 0; i < algorithmResult.Elevators.Length; i++)
            {
                UniformGrid u = new UniformGrid
                {
                    Width = 80,
                    Height = 112,
                    Rows = 4,
                    Columns = 3
                };
                Canvas.SetTop(u, Canvas.GetTop(ImgElevators[i]));
                Canvas.SetLeft(u, Canvas.GetLeft(ImgElevators[i]));
                CvsMain.Children.Add(u);
                UnigridElevators.Add(u);
                tempElements.Add(u);
            }

            foreach (var person in algorithmResult.People)
            {
                if (person.is_out == false)
                {
                    if (person.in_which_elevator != 0)//在电梯中
                    {

                        Grid nodeGrid = new Grid();

                        Ellipse nodeCircle = new Ellipse
                        {
                            Fill = Brushes.Yellow,
                            Stroke = Brushes.Black,
                            Width = 20,
                            Height = 20
                        };

                        TextBlock nodeText = new TextBlock
                        {
                            Text = person.to_floor.ToString(),
                            HorizontalAlignment = HorizontalAlignment.Center,
                            VerticalAlignment = VerticalAlignment.Center,
                            TextAlignment = TextAlignment.Center,
                            FontWeight = FontWeight.FromOpenTypeWeight(600)
                        };

                        nodeGrid.Children.Add(nodeCircle);
                        nodeGrid.Children.Add(nodeText);

                        UnigridElevators[person.in_which_elevator - 1].Children.Add(nodeGrid);
                        tempElements.Add(nodeGrid);
                    }
                }
            }
        }
        private void ClearUI()
        {
            foreach (var item in tempElements)
            {
                CvsMain.Children.Remove(item);
            }
            tempElements.Clear();
        }
        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            //Console.WriteLine(PythonCaller.PathPythonFile);
            string cmd = $"python {PythonCaller.PathPythonFile}";
            string output = CMDHelper.RunCmd(cmd);
            //Console.WriteLine(output);
            JsonToUI(output);
        }

        private void BtnTest_Click(object sender, RoutedEventArgs e)
        {
            ClearUI();
        }


    }
}
