using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace elevator_dispatch_GUI
{
    public static class PythonCaller
    {
        private const string filename = "algorithm_wrapper.py";
        private static string pathPythonFile;

        public static string PathPythonFile
        {
            get
            {
                if (string.IsNullOrEmpty(pathPythonFile))
                {
                    SearchPythonFilePython();
                }
                return pathPythonFile;
            }
            set => pathPythonFile = value;
        }

        public static void SearchPythonFilePython()
        {
            var paths = new List<string>
            {
                "./",
                "../../../elevator_dispatch_algorithm"
            };
            foreach (var path in paths)
            {
                //Console.WriteLine(path);
                var files = Directory.GetFiles(path);
                foreach (var file in files)
                {
                    if (file.Contains(filename))
                    {
                        pathPythonFile = file;
                        return;
                    }
                }
                //ArrayPrint(files);
                //ArrayPrint(Directory.GetDirectories(path));
            }
            throw new FileNotFoundException($"未找到 {filename}");
        }

    }
}
