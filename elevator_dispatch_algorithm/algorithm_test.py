from algorithm_interface import *
import algorithm_implement
# 测试算法


def test1():
    person_1 = person()
    person_1.from_floor = 3
    person_1.to_floor = 12
    person_1.come_time = 1
    person_1.current_floor = 3
    person_1.in_which_elevator = 0
    person_1.is_out = False

    person_2 = person()
    person_2.from_floor = 3
    person_2.to_floor = 12
    person_2.come_time = 1
    person_2.current_floor = 3
    person_2.in_which_elevator = 0
    person_2.is_out = False

    person_3 = person()
    person_3.from_floor = 3
    person_3.to_floor = 12
    person_3.come_time = 1
    person_3.current_floor = 3
    person_3.in_which_elevator = 0
    person_3.is_out = False

    core_algorithm(7, [person_1, person_2, person_3])
    # 有3个人在1.0秒出现于第3层(第0层指地下三层,第3层指1楼),要前往第12层,求第7.0秒时电梯和人员的位置

    # 由第3层到第12层,只能使用电梯0

    # 1.0秒到7.0秒,共6秒,电梯上移三层,由3层到6层(还没有考虑进入电梯的时间)

    # 所以应该返回
    person_1.current_floor = 6
    person_1.in_which_elevator = 1
    person_2.current_floor = 6
    person_2.in_which_elevator = 1
    person_3.current_floor = 6
    person_3.in_which_elevator = 1

    return [[elevator(6, 1), elevator(3, 0), elevator(3, 0)], [person_1, person_2, person_3]]


def test2():
    person_1 = person()
    person_1.from_floor = 3
    person_1.to_floor = 12
    person_1.come_time = 1
    person_1.current_floor = 3
    person_1.in_which_elevator = 0
    person_1.is_out = False

    person_2 = person()
    person_2.from_floor = 3
    person_2.to_floor = 12
    person_2.come_time = 1
    person_2.current_floor = 3
    person_2.in_which_elevator = 0
    person_2.is_out = False

    person_3 = person()
    person_3.from_floor = 3
    person_3.to_floor = 12
    person_3.come_time = 1
    person_3.current_floor = 3
    person_3.in_which_elevator = 0
    person_3.is_out = False

    person_4 = person()
    person_4.from_floor = 4
    person_4.to_floor = 6
    person_4.come_time = 6
    person_4.current_floor = 3
    person_4.in_which_elevator = 0
    person_4.is_out = False

    person_5 = person()
    person_5.from_floor = 4
    person_5.to_floor = 6
    person_5.come_time = 6
    person_5.current_floor = 3
    person_5.in_which_elevator = 0
    person_5.is_out = False

    core_algorithm(7, [person_1, person_2, person_3, person_4, person_5])
    # 有3个人在1.0秒出现于第3层(第0层指地下三层,第3层指1楼),要前往第12层.有2个人在6.0秒出现在第4层,要前往第6层.求第7.0秒时电梯和人员的位置

    # 由第3层到第12层,只能使用电梯0
    # 由第4层到第6层,使用电梯2

    # 1.0秒到7.0秒,共6秒,电梯上移三层,由3层到6层(还没有考虑进入电梯的时间)
    # 6.0秒到7.0秒,共1秒,电梯上移0.5层,由3层到3.5层


# 第一秒：p1 p2 p3 到一楼 电梯开始上行
# 第二秒：p1进电梯e2
# 第三秒：p2进电梯e2
# 第四秒：p3进电梯e2
# 第五秒：电梯e2到3.5
# 第六秒：电梯e2到4
# 第七秒：p4 p5到二楼，p4进电梯e2

    # 所以应该返回
    person_1.current_floor = 4.0
    person_1.in_which_elevator = 2
    person_2.current_floor = 4.0
    person_2.in_which_elevator = 2
    person_3.current_floor = 4.0
    person_3.in_which_elevator = 2
    person_4.current_floor = 4.0
    person_4.in_which_elevator = 2
    person_5.current_floor = 4.0
    person_4.in_which_elevator = 0

    return [[elevator(3.0, 0), elevator(4.0, 1), elevator(3.0, 0)], [person_1, person_2, person_3, person_4, person_5]]


def test3():
    person_1 = person()
    person_1.from_floor = 3
    person_1.to_floor = 12
    person_1.come_time = 1
    person_1.current_floor = 3.0
    person_1.in_which_elevator = 0
    person_1.is_out = False

    person_2 = person()
    person_2.from_floor = 3
    person_2.to_floor = 12
    person_2.come_time = 1
    person_2.current_floor = 3.0
    person_2.in_which_elevator = 0
    person_2.is_out = False

    person_3 = person()
    person_3.from_floor = 3
    person_3.to_floor = 12
    person_3.come_time = 1
    person_3.current_floor = 3.0
    person_3.in_which_elevator = 0
    person_3.is_out = False

    person_4 = person()
    person_4.from_floor = 4
    person_4.to_floor = 6
    person_4.come_time = 6
    person_4.current_floor = 4.0
    person_4.in_which_elevator = 0
    person_4.is_out = False

    person_5 = person()
    person_5.from_floor = 4
    person_5.to_floor = 6
    person_5.come_time = 6
    person_5.current_floor = 4.0
    person_5.in_which_elevator = 0
    person_5.is_out = False

    return algorithm_implement.core_algorithm(7, [person_1, person_2, person_3, person_4, person_5])


if __name__ == "__main__":
    print('test2_is')
    result2 = test2()
    r2 = algorithm_result()
    r2.elevators = result2[0]
    r2.people = result2[1]
    r2_json = json.dumps(r2, indent=4)
    print(r2_json)

    print('test3_is')
    result3 = test3()
    r3 = algorithm_result()
    r3.elevators = result3[0]
    r3.people = result3[1]
    r3_json = json.dumps(r3, indent=4)
    print(r3_json)

    if r2_json == r3_json:
        print('test success')
    else:
        print('test failed')
