# -*- coding: utf-8 -*-
#定义常量
NUMBER_OF_FLOOR_LEVELS = 21
max_person = 12  # 电梯载客量
elevator_speed = 0.5  # 电梯速度,每秒0.5层

class person:  # 人
    come_time = 0  # 出现的时间
    from_floor = 0  # 出发楼层
    to_floor = 0  # 到达楼层
    current_floor = 0  # 现在的楼层
    in_which_elevator = 0  # 在哪个电梯中,可取 0 1 2 3 分别指不在电梯中 在第一个电梯中 在第二个电梯中 在第三个电梯中
    is_out = False  # 是否已经完成电梯乘坐

    def to_json(self):
        dict_name_value = {}

        for name, value in vars(self).items():
            dict_name_value[name] = value
        return dict_name_value
# 电梯
# 电梯0可以停靠所有楼层,电梯1单到单,电梯2双到双


class elevator:
    current_floor = 3.0  # 现在的楼层,允许小数,每一秒都要进行精确更新.初始位置1楼
    move_direction = 0  # 移动方向,可取到0 1 2,分别是 停止 向上 向下

    def __init__(self, current_floor, move_direction):
        self.current_floor = current_floor  
        self.move_direction = move_direction

    def to_json(self):
        dict_name_value = {}

        for name, value in vars(self).items():
            dict_name_value[name] = value
        return dict_name_value
# 核心算法:顺向截停
# 对输入人群数组,不应假设每个人的出现时间都是1 6 11 ... 而可能是任意整数时间点(不方便的话再进行沟通),不应假设come_time<=t


class floor:
    floor_people = []
    up_button = False #电梯上升按钮
    down_button = False #电梯下降按钮


def core_algorithm(time, array_people):
    #初始化楼层对象(不太熟悉python语法，写的有点奇怪？
    f1 = []                                 # 一号电梯对应的楼层，下同
    for i in range(NUMBER_OF_FLOOR_LEVELS):
        f1.append(floor())
    f2 = []
    for i in range(NUMBER_OF_FLOOR_LEVELS):
        f2.append(floor())
    f3 = []
    for i in range(NUMBER_OF_FLOOR_LEVELS):
        f3.append(floor())

    f = [f1,f2,f3]              #f1:只停单层，f2:只停双数层(包括1层)，f3:全停


    #初始化电梯对象            #e1:只停单层，e2:只停双数层(包括1层)，e3:全停
    e1 = elevator(3.0,0) #一号电梯，下同
    e2 = elevator(3.0,0)
    e3 = elevator(3.0,0)

    e = [e1,e2,e3]

    
    #时间迭代    
    for t in range(time):
        for p in array_people:  #遍历人群

            
        #处理人群到达的事件
            if(p.come_time==t):   #这个人[第一次]出现，则加入到楼层中（第一次出现显然不会在电梯里，也不会完成乘坐
                #更新人的状态
                p.current_floor = p.from_floor #（看了下测试代码，感觉这里有些多余，不过还是保留在这里

                #分配到各个电梯(这里写的有些乱，要小心)
                if((p.from_floor>=3 and p.from_floor%2==1) or (p.from_floor<3 and p.from_floor%2==0)):#要注意0代表负三层等一系列的问题
                    if((p.to_floor>=3 and p.to_floor%2==1) or (p.to_floor<3 and p.to_floor%2==0)): # 单-单
                        temp1 = 0
                    elif(p.from_floor == 3): #1-双
                        temp1 = 1
                    else: #单-双
                        temp1 = 2
                else:
                    if(p.from_floor == 3): #双-1
                        temp1 = 1
                    elif((p.to_floor>3 and p.to_floor%2==1) or (p.to_floor<3 and p.to_floor%2==0)): #双-单
                        temp1 = 2
                    else:
                        temp1 = 1
                    
                #更新楼层状态
                f[temp1][p.from_floor].floor_people.append(p)        #将人添加到楼层中
                if(p.to_floor > p.from_floor): #此人上行
                    f[temp1][p.from_floor].up_button = True #按下上行按钮
                else:
                    f[temp1][p.from_floor].down_button = True #按下下行按钮 (to_floor==from_floor的情况感觉很麻烦，最好不要出现...
        #人群到达事件处理完毕



        #下面根据电梯运行情况分类处理
        #
        for i in [0,1,2]:
            if(e[i].move_direction == 0): #电梯静止
                for j in range(NUMBER_OF_FLOOR_LEVELS):
                    if(f[i][j].up_button == True or f[i][j].down_button == True):
                        if(j > e[i].current_floor): #楼上有人，电梯上行
                            e[i].move_direction = 1
                            break
                        elif(j < e[i].current_floor): #楼下有人，电梯下行
                            e[i].move_direction = 2
                            break
                        else: #本层有人，由此人上行还是下行而定
                            if(f[i][j].down_button == True):
                                e[i].move_direction = 2
                            else:
                                e[i].move_direction = 1


            elif(e[i].move_direction == 1): #电梯上行
                if(e[i].current_floor % 1 != 0): #电梯未与楼层对齐
                    e[i].current_floor += elevator_speed    #向上半层(用时一秒)
                    for p in array_people:  #更新所有乘客状态
                        if(p.in_which_elevator == i+1):
                            p.current_floor = e[i].current_floor
                else: #电梯对齐某一楼层
                    #电梯里有人到达目标楼层
                    for p in array_people:
                        if(p.in_which_elevator==i+1 and p.to_floor==e[i].current_floor):
                            p.in_which_elevator = 0
                            p.is_out = True
                            break


                    #处理电梯人满的情况
                    sum_of_people = 0
                    for p in array_people:
                        if(p.in_which_elevator == i+1):
                            sum_of_people += 1
                    if(sum_of_people == max_person): #人满，电梯向上
                        e[i].current_floor += elevator_speed    #向上半层(用时一秒)
                        for p in array_people:  #更新所有乘客状态
                            if(p.in_which_elevator == i+1):
                                p.current_floor = e[i].current_floor
                        break #结束这一秒

                    if(f[i][int(e[i].current_floor)].up_button == True): #这层楼有人需要上行

                        f[i][int(e[i].current_floor)].floor_people[0].in_which_elevator = i+1 #加入电梯中
                        f[i][int(e[i].current_floor)].floor_people.pop(0)
                        if(len(f[i][int(e[i].current_floor)].floor_people) == 0):
                            f[i][int(e[i].current_floor)].up_button = False #人已经全部进入电梯，楼层上行灯灭
                        break

                    if(sum_of_people > 0):  #电梯里还有人，继续上行
                        e[i].current_floor += elevator_speed    #向上半层(用时一秒)
                        for p in array_people:  #更新所有乘客状态
                            if(p.in_which_elevator == i+1):
                                p.current_floor = e[i].current_floor
                    elif(sum_of_people == 0): #电梯内无人，电梯静止(下一秒遍历楼层找人
                        e[i].move_direction = 0

            elif(e[i].move_direction == 2): #电梯下行
                if(e[i].current_floor % 1 != 0): #电梯未与楼层对齐
                    e[i].current_floor -= elevator_speed    #向下半层(用时一秒)
                    for p in array_people:  #更新所有乘客状态
                        if(p.in_which_elevator == i+1):
                            p.current_floor = e[i].current_floor
                else: #电梯对齐某一楼层
                    #电梯里有人到达目标楼层
                    for p in array_people:
                        if(p.in_which_elevator==i+1 and p.to_floor==e[i].current_floor):
                            p.in_which_elevator = 0
                            p.is_out = True
                            break


                    #处理电梯人满的情况
                    sum_of_people = 0
                    for p in array_people:
                        if(p.in_which_elevator == i+1):
                            sum_of_people += 1
                    if(sum_of_people == max_person): #人满，电梯向下
                        e[i].current_floor -= elevator_speed    #向下半层(用时一秒)
                        for p in array_people:  #更新所有乘客状态
                            if(p.in_which_elevator == i+1):
                                p.current_floor = e[i].current_floor
                        break #结束这一秒

                    if(f[i][int(e[i].current_floor)].down_button == True): #这层楼有人需要下行

                        f[i][int(e[i].current_floor)].floor_people[0].in_which_elevator = i+1 #加入电梯中
                        f[i][int(e[i].current_floor)].floor_people.pop(0)
                        if(len(f[i][int(e[i].current_floor)].floor_people) == 0):
                            f[i][int(e[i].current_floor)].down_button = False #人已经全部进入电梯，楼层下行灯灭
                        break

                    if(sum_of_people > 0):  #电梯里还有人，继续下行
                        e[i].current_floor -= elevator_speed    #向下半层(用时一秒)
                        for p in array_people:  #更新所有乘客状态
                            if(p.in_which_elevator == i+1):
                                p.current_floor = e[i].current_floor
                    elif(sum_of_people == 0): #电梯内无人，电梯静止(下一秒遍历楼层找人
                        e[i].move_direction = 0
                
        
    return [[e1,e2,e3],array_people]

