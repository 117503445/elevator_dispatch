from algorithm import *

# 测试算法


def test1():
    person_1 = person()
    person_1.from_floor = 3
    person_1.to_floor = 12
    person_1.come_time = 1
    person_1.current_floor = 3
    person_1.is_in_elevator = False
    person_1.is_out = False

    person_2 = person()
    person_2.from_floor = 3
    person_2.to_floor = 12
    person_2.come_time = 1
    person_2.current_floor = 3
    person_2.is_in_elevator = False
    person_2.is_out = False

    person_3 = person()
    person_3.from_floor = 3
    person_3.to_floor = 12
    person_3.come_time = 1
    person_3.current_floor = 3
    person_3.is_in_elevator = False
    person_3.is_out = False

    core_algorithm(7, [person_1, person_2, person_3])
    # 有3个人在1.0秒出现于第3层(第0层指地下三层,第3层指1楼),要前往第12层,求第7.0秒时电梯和人员的位置

    # 由第3层到第12层,只能使用电梯0

    # 1.0秒到7.0秒,共6秒,电梯上移三层,由3层到6层(还没有考虑进入电梯的时间)

    # 所以应该返回
    person_1.current_floor = 6
    person_1.is_in_elevator = True
    person_2.current_floor = 6
    person_2.is_in_elevator = True
    person_3.current_floor = 6
    person_3.is_in_elevator = True

    return [elevator(6, True), elevator(3, False), elevator(3, False), [person_1, person_2, person_3]]


def test2():
    person_1 = person()
    person_1.from_floor = 3
    person_1.to_floor = 12
    person_1.come_time = 1
    person_1.current_floor = 3
    person_1.is_in_elevator = False
    person_1.is_out = False

    person_2 = person()
    person_2.from_floor = 3
    person_2.to_floor = 12
    person_2.come_time = 1
    person_2.current_floor = 3
    person_2.is_in_elevator = False
    person_2.is_out = False

    person_3 = person()
    person_3.from_floor = 3
    person_3.to_floor = 12
    person_3.come_time = 1
    person_3.current_floor = 3
    person_3.is_in_elevator = False
    person_3.is_out = False

    person_4 = person()
    person_4.from_floor = 4
    person_4.to_floor = 6
    person_4.come_time = 6
    person_4.current_floor = 3
    person_4.is_in_elevator = False
    person_4.is_out = False

    person_5 = person()
    person_5.from_floor = 4
    person_5.to_floor = 6
    person_5.come_time = 6
    person_5.current_floor = 3
    person_5.is_in_elevator = False
    person_5.is_out = False

    core_algorithm(7, [person_1, person_2, person_3, person_4, person_5])
    # 有3个人在1.0秒出现于第3层(第0层指地下三层,第3层指1楼),要前往第12层.有2个人在6.0秒出现在第4层,要前往第6层.求第7.0秒时电梯和人员的位置

    # 由第3层到第12层,只能使用电梯0
    # 由第4层到第6层,使用电梯2

    # 1.0秒到7.0秒,共6秒,电梯上移三层,由3层到6层(还没有考虑进入电梯的时间)
    # 6.0秒到7.0秒,共1秒,电梯上移0.5层,由3层到3.5层

    # 所以应该返回
    person_1.current_floor = 6
    person_1.is_in_elevator = True
    person_2.current_floor = 6
    person_2.is_in_elevator = True
    person_3.current_floor = 6
    person_3.is_in_elevator = True



    return [elevator(6, True), elevator(3, False), elevator(3.5, True), [person_1, person_2, person_3, person_4, person_5]]
