﻿using elevator_dispatch_GUI.models;

using Newtonsoft.Json;

using System;
using System.Collections.Generic;
using System.IO;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.Windows.Threading;
using TLib.Software;

namespace elevator_dispatch_GUI
{
    /// <summary>
    /// WdMain.xaml 的交互逻辑
    /// </summary>
    public partial class WdMain : Window
    {
        private const int floorNum = 21;
        public WdMain()
        {
            InitializeComponent();
        }
        private readonly List<FrameworkElement> tempElements = new List<FrameworkElement>();
        private int IndexToFloor(int index)
        {
            if (index <= 2)
            {
                return index - 3;
            }
            else
            {
                return index - 2;
            }
        }
        private void JsonToUI(string json)
        {
            Console.WriteLine(json);
            Logger.WriteLine(json);
            var algorithmResult = JsonConvert.DeserializeObject<AlgorithmOutput>(json);

            var TbFloors = new List<TextBlock>();//楼层告示
            for (int i = 0; i < floorNum; i++)
            {
                string s=$"{IndexToFloor(i)}F";

                TextBlock tb = new TextBlock
                {
                    Text = s,
                    FontSize = 16,
                    FontWeight = FontWeight.FromOpenTypeWeight(600)
                };
                Canvas.SetLeft(tb, 110 + i * 80);
                TbFloors.Add(tb);
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
            var UnigridWait = new List<UniformGrid>();//等待区的 UniformGrid
            for (int i = 0; i < floorNum; i++)
            {
                UniformGrid u = new UniformGrid
                {
                    Width = 80,
                    Height = 112,
                    Rows = 4,
                    Columns = 3
                };
                //Canvas.SetTop(u, Canvas.GetTop(TbFloors[i]) + 80);
                Canvas.SetTop(u, 40);
                Canvas.SetLeft(u, Canvas.GetLeft(TbFloors[i]) - 30);
                CvsMain.Children.Add(u);
                UnigridWait.Add(u);
                tempElements.Add(u);
            }
            foreach (var person in algorithmResult.People)
            {
                if (person.is_out == false && algorithmInput.Time >= person.come_time)
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
                        Text = IndexToFloor(person.to_floor).ToString(),
                        HorizontalAlignment = HorizontalAlignment.Center,
                        VerticalAlignment = VerticalAlignment.Center,
                        TextAlignment = TextAlignment.Center,
                        FontWeight = FontWeight.FromOpenTypeWeight(600)
                    };

                    nodeGrid.Children.Add(nodeCircle);
                    nodeGrid.Children.Add(nodeText);
                    tempElements.Add(nodeGrid);
                    if (person.in_which_elevator != 0)//在电梯中
                    {
                        UnigridElevators[person.in_which_elevator - 1].Children.Add(nodeGrid);
                    }
                    else
                    {
                        UnigridWait[person.from_floor].Children.Add(nodeGrid);
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

        private readonly string path_in_json = "in.json";
        private readonly Random r = new Random();
        private AlgorithmInput algorithmInput;
        private void SetAlgorithmInput()
        {
            algorithmInput = new AlgorithmInput
            {
                Time = 10,
                People = new Person[9]
            };

            for (int i = 0; i < 3; i++)
            {
                int from = r.Next(3, 20);
                int to = r.Next(3, 20);

                for (int j = 0; j < 3; j++)
                {
                    Person p = new Person
                    {
                        from_floor = from,
                        current_floor = from,
                        come_time = i * 5 + 1,
                        to_floor = to
                    };
                    algorithmInput.People[i * 3 + j] = p;
                }
            }
        }

        private void TimerUpdateUI_Tick(object sender, EventArgs e)
        {
            var timer = sender as DispatcherTimer;
            TbTime.Text = $"当前时间:第{(int)timer.Tag}秒";
            ClearUI();
            algorithmInput.Time = (int)timer.Tag;
            string json = JsonConvert.SerializeObject(algorithmInput);
            //Console.WriteLine(json);
            File.WriteAllText(path_in_json, json);

            //Close();
            string cmd = $"python {PythonCaller.PathPythonFile}";
            string output = CMDHelper.RunCmd(cmd);
            //Logger.WriteLine(output);
            //Console.WriteLine(output);
            if (string.IsNullOrWhiteSpace(output))
            {
                MessageBox.Show($"发生异常!输入为{json}");
            }
            JsonToUI(output);
            timer.Tag = (int)timer.Tag + 1;
            Console.WriteLine(timer.Tag);
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            Logger.IsOutputInConsole = true;
            //Console.WriteLine(PythonCaller.PathPythonFile);
            //FileInfo info = new FileInfo(PythonCaller.PathPythonFile);
            //string dir = info.DirectoryName;
            //string path_in_json = dir + "/in.json";
            SetAlgorithmInput();
            DispatcherTimer TimerUpdateUI = new DispatcherTimer
            {
                Interval = TimeSpan.FromMilliseconds(500),
                Tag = 0
            };
            TimerUpdateUI.Tick += TimerUpdateUI_Tick;
            TimerUpdateUI.Start();
        }

        private void BtnTest1_Click(object sender, RoutedEventArgs e)
        {
            ClearUI();
        }

        private void BtnTest2_Click(object sender, RoutedEventArgs e)
        {
            string cmd = $"python {PythonCaller.PathPythonFile}";
            string output = CMDHelper.RunCmd(cmd);
            JsonToUI(output);
        }
    }
}
