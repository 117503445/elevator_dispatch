#定义常量
NUMBER_OF_FLOOR_LEVELS = 21


class floor:
    floor_people = []
    up_button = False #电梯上升按钮
    down_button = False #电梯下降按钮


def core_algorithm(time, array_people):
    #初始化楼层对象(不太熟悉python语法，写的有点奇怪？
    f = []
    for i in range(NUMBER_OF_FLOOR_LEVELS):
        f.append(floor())


    #初始化电梯对象
    e = elevator(3.0,False)

    
    #时间迭代    
    for t in range(time):
        for p in array_people:  #遍历人群
        #分配到各个电梯的算法暂时不考虑，现在只实现一个电梯的情况
            
        #处理人群到达的事件
            if(p.come_time==t):   #这个人[第一次]出现，则加入到楼层中（第一次出现显然不会在电梯里，也不会完成乘坐
                #更新人的状态
                p.current_floor = p.from_floor #（看了下测试代码，感觉这里有些多余，不过还是保留在这里

                
                #更新楼层状态
                f[from_floor].floor_people.append(p)        #将人添加到楼层中
                if(p.to_floor > p.from_floor): #此人上行
                    f[from_floor].up_buttom = True #按下上行按钮
                else:
                    f[from_floor].down_buttom = True #按下下行按钮 (to_floor==from_floor的情况感觉很麻烦，最好不要出现...
        #人群到达事件处理完毕



    #下面根据电梯运行情况分类处理
    if(is_up == True): #电梯上行
        if(e.current_floor % 1 != 0): #电梯未与楼层对齐
            e.current_floor += 0.5    #向上半层(用时一秒)
            for p in array_people:  #更新所有乘客状态
                if(p.is_in_elevator == True):
                    p.current_floor = e.current_floor   
        else: #电梯对齐某一楼层
            if(f[current_floor].up_button == True): #这层楼有人需要上行
                #这里没处理电梯人满的情况
                
                f[current_floor].floor_people[0].is_in_elevator = True #加入电梯中
                f[current_floor].floor_people.pop(0)
                if(len(f[current_floor]) == 0):
                    f[current_floor].up_button == False #人已经全部进入电梯，楼层上行灯灭
            elif(): #电梯里有人到达目标楼层
                pass
                
        
    # return [ [电梯1,电梯2,电梯3], [人1,人2....] ]
    pass

