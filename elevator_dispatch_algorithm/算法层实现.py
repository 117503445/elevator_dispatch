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
                p.current_floor = p.from_floor

                
                #更新楼层状态
                f[from_floor].append(p)        #将人添加到楼层中
                if(p.to_floor > p.from_floor): #此人上行
                    f[from_floor].up_buttom = True #按下上行按钮
                else:
                    f[from_floor].down_buttom = True #按下下行按钮 (to_floor==from_floor的情况感觉很麻烦，最好不要出现...
        #人群到达事件处理完毕



    #下面根据电梯运行情况分类处理
                
                
        
    # return [ [电梯1,电梯2,电梯3], [人1,人2....] ]
    pass

