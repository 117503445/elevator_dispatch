using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.IO;
using System.Collections;
using System.Configuration;
using Newtonsoft.Json;
using elevator_dispatch_GUI.models;

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
        private void JsonToUI(string json)
        {
            Console.WriteLine(json);
            var algorithmResult = JsonConvert.DeserializeObject<AlgorithmResult>(json);

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
                Canvas.SetLeft(tb, 10 + i * 80);
                CvsMain.Children.Add(tb);
            }//生成楼层告示

            var images = new List<Image>();//生成3个电梯
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
                
                Canvas.SetTop(im, 80 + i * 120);
                Canvas.SetLeft(im, e.current_floor * 80-20);
                CvsMain.Children.Add(im);
                images.Add(im);
            }

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


        }


    }
}
