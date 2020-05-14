# 关于楼层编号:从地下3到地上18编号 0-20 一楼编号:3

max_person = 13  # 电梯载客量
elevator_speed = 0.5  # 电梯速度,每秒0.5层


class person:  # 人
    come_time = 0  # 出现的时间
    from_floor = 0  # 出发楼层
    to_floor = 0  # 到达楼层
    current_floor = 0  # 现在的楼层
    is_in_elevator = False  # 是否在电梯中
    is_out = False  # 是否已经完成电梯乘坐

# 电梯
# 电梯0可以停靠所有楼层,电梯1单到单,电梯2双到双


class elevator:
    current_floor = 3.0  # 现在的楼层,允许小数,每一秒都要进行精确更新.初始位置1楼
    is_up = True  # 是否在往上

    def __init__(self, current_floor, is_up):
        self.current_floor = current_floor
        self.is_up = is_up

# 核心算法:顺向截停


def core_algorithm(time, array_people):
    # return [ [电梯1,电梯2,电梯3], [人1,人2....] ]
    pass

# 测试算法


def test():
    person_1 = person()
    person_1.from_floor = 3
    person.to_floor = 12
    person_1.come_time = 1

    core_algorithm(7, [person_1, person_1, person_1])
    # 有3个人在1.0秒出现于第3层(第0层指地下三层,第3层指1楼),要前往第12层,求第7.0秒时电梯和人员的位置

    # 由第3层到第12层,只能使用电梯0

    # 1.0秒到7.0秒,共6秒,电梯上移三层,由3层到6层

    #所以应该返回
     
    [elevator(6,True),elevator(3,False),elevator(3,False),[]]


# 通过标准输入输出,供外部程序调用,还没有写
if __name__ == "__main__":
    pass
