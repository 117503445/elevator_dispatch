using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace elevator_dispatch_GUI.models
{
    public class Person
    {

        public int come_time { get; set; }
        public int from_floor { get; set; }
        public int to_floor { get; set; }
        public int current_floor { get; set; }
        public int in_which_elevator { get; set; } = 0;
        public bool is_out { get; set; } = false;
    }
}
