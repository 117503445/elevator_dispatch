using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
using TLib.Software;

namespace elevator_dispatch_GUI
{
    /// <summary>
    /// App.xaml 的交互逻辑
    /// </summary>
    public partial class App : Application
    {
        private void Application_Startup(object sender, StartupEventArgs e)
        {
#if !DEBUG
            WpfExpectionHandler.HandleExpection(Current, AppDomain.CurrentDomain);
            WpfExpectionHandler.ExpectionCatched += WpfExpectionHandler_ExpectionCatched;
#endif
        }

        private void WpfExpectionHandler_ExpectionCatched(object sender, Exception e)
        {
            MessageBox.Show("很抱歉发生了异常,请将err.json和log.txt发送给开发者");
        }
    }
}
