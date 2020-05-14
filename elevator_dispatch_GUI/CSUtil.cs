using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace elevator_dispatch_GUI
{
    public static class CSUtil
    {
        public static void ArrayPrint(IEnumerable array)
        {
            int len = 0;
            Console.WriteLine();
            Console.WriteLine("ArrayPrint");
            foreach (var item in array)
            {
                Console.WriteLine("\t" + item);
                len++;
            }
            Console.WriteLine($"\tlength = {len}");
            Console.WriteLine("ArrayPrint End");
            Console.WriteLine();
        }
    }
}
