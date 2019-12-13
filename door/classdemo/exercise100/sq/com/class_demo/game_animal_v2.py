from random  import  randint
import  time
class Tiger:
    callVoice = "WOW!!"
    nickName="老虎"
    eatNum = 0 #吃的次数
    callNum =0 #叫的次数
    def __init__(self, inifood, inieatMaxNum,inicallMaxNum,iniweight=200):
        self.food = inifood
        self.weight =iniweight
        self.eatMaxNum = inieatMaxNum
        self.callMaxNum = inicallMaxNum
    def call(self):
        print(self.callVoice)
        self.weight-=5 # 如果叫了一声体重就会减少5斤
        pass
    def feed(self,food):
        if (self.eatNum < self.eatMaxNum):
            if(food=="meate"):
                # print("虎喂对了")
                self.weight += 10
                self.eatNum += 1
                return "success"

            else :
                self.weight -= 10
                return "fail"
        else :
            print("喂过了,不能再喂了")
            return "fail"

class Sheep:
    #静态变量和实例变量有点混了？eatMaxNum callMaxNum 应该是静态的？
    callVoice = "mie!!"
    nickName="羊"
    eatNum = 0  # 已经吃的次数
    callNum = 0  # 已经叫的次数
    def __init__(self, inifood,inieatMaxNum,inicallMaxNum,iniweight=100):
        self.weight = iniweight
        self.food = inifood
        self.eatMaxNum =inieatMaxNum
        self.callMaxNum = inicallMaxNum
    def call(self):
        # 如果叫体重就会减少5斤
        print(self.callVoice)
        if (self.callNum < self.callMaxNum+1):
            self.weight -= 5
            return "success"
        else:
            print ("达到call的上限次数")
            return "fail"

    def feed(self,food):
        if(self.eatNum <self.eatMaxNum):
            if(food == "grass"):
                # print("羊喂对了")
                self.weight += 10
                self.eatNum+=1
                return "success"
            else :
                self.weight -= 10
                return "fail"
        else :
            print("喂过了,不能再喂了")
            return "fail"

class Room:
    def __init__(self,ininum,inianima):
        self.num = ininum
        self.anima = inianima
def game_demo(game_Maxtime):
    # 记忆房间动物
    rem={"可喂食房间和动物":""}
    roomList=[]
    #随机初始化10个房间的动物编号和动物,每只老虎能喂3次、每只羊只能喂2次，只能叫1次
    for one in range(1,11):
        if randint(0,1):
            # print("初始化一个老虎")
            ani = Room(str(one),Tiger("meat",3,2))
        else:
            # print("初始化一只羊")
            ani=  Room(str(one),Sheep("grass",2,2))
        roomList.append(ani)
    # 完成初始化
    print("==========开始游戏==========")
    print (f'\n-游戏规则默认每只老虎能喂3次、每只羊只能喂2次，都只能叫1次\n-游戏时间{game_Maxtime}s\n')
    startime = time.time()
    while True :
        #随机产生一个房间号，让用户选择喂食或者敲门
        endtime = time.time ()
        if ((endtime - startime) < int (game_Maxtime)):

            while True:
                room_num = randint (0, 9)
                print ("请您去房间号" + str (room_num + 1) + "门口选择操作\n")
                an = (roomList[room_num]).anima
                choose=""
                while True:
                    choose = input("输入1喂食,输入2敲门,提示" + str (rem) + "\n")
                    if (choose == "1" or choose == "2"):
                        break
                if (choose == "1"):  # 直接喂食1
                    print ("选择投喂")
                    feedfood = input (f'输入meate或者grass!请输入')
                    res = (an.feed (feedfood))  # 投喂成功或者失败
                    if (res == "success"):  # 投喂成功
                        print (f'编号{(roomList[room_num]).num}的{an.nickName}成功吃到{an.food}')
                        # 如果是投喂次数达到上限 就去掉提示 ；否则添加提示(如果是羊就给羊加提示，如果是虎就给虎加提示)eatNum
                        if an.eatNum == an.eatMaxNum:  # 已经达到投喂上限次数，去掉强提示
                            if rem.keys ().__contains__ (str ((roomList[room_num]).num)):
                                print (f'去掉强提示:编号{(roomList[room_num]).num}的{an.nickName}')
                                rem.pop (str ((roomList[room_num]).num))  # 喂过的去掉强提示
                            else:
                                pass
                        else:
                            if int (an.eatNum) == 0:  # 没加过提示就加提示
                                if (an.nickName == "老虎"):
                                    rem[str ((roomList[room_num]).num)] = "老虎"
                                    pass
                                elif (an.nickName == "羊"):
                                    rem[str ((roomList[room_num]).num)] = "羊"
                                else:
                                    pass
                    else:  ##投喂失败:已经达到投喂上限或者喂错食物了
                        print (f'编号{(roomList[room_num]).num}的{an.nickName}投喂失败')
                        if an.eatNum == an.eatMaxNum:  # 已经达到投喂上限次数，去掉强提示
                            if rem.keys ().__contains__ (str ((roomList[room_num]).num)):
                                print (f'去掉强提示:编号{(roomList[room_num]).num}的{an.nickName}')
                                rem.pop (str ((roomList[room_num]).num))  # 喂过的去掉强提示
                            else:
                                pass
                        else:
                            if int (an.eatNum) == 0:  # 没加过提示就加提示
                                if (an.nickName == "老虎"):
                                    rem[str ((roomList[room_num]).num)] = "老虎"
                                    pass
                                elif (an.nickName == "羊"):
                                    rem[str ((roomList[room_num]).num)] = "羊"
                                else:
                                    pass
                        pass
                else:# 直接喂食1
                    # 敲门2后识别出动物再喂
                    print ("选择先让动物叫")
                    if an.callNum < an.callMaxNum:
                        an.call ()
                    else:
                        print (f'{an.nickName}叫够次数了,不叫了')
                    print ("然后再投喂")
                    feedfood = input (f'输入meate或者grass!请输入')
                    res = (an.feed (feedfood))  # 投喂成功或者失败
                    if (res == "success"):  # 投喂成功
                        print (f'编号{(roomList[room_num]).num}的{an.nickName}成功吃到{an.food}')
                        # 如果是投喂次数达到上限 就去掉提示 ；否则添加提示(如果是羊就给羊加提示，如果是虎就给虎加提示)eatNum
                        if an.eatNum == an.eatMaxNum:  # 已经达到投喂上限次数，去掉强提示
                            if rem.keys ().__contains__ (str ((roomList[room_num]).num)):
                                rem.pop (str ((roomList[room_num]).num))  # 喂过的去掉强提示
                            else:
                                pass
                        else:
                            if int (an.eatNum) == 0:  # 没加过提示就加提示
                                if (an.nickName == "老虎"):
                                    rem[str ((roomList[room_num]).num)] = "老虎"
                                    pass
                                elif (an.nickName == "羊"):
                                    rem[str ((roomList[room_num]).num)] = "羊"
                                else:
                                    pass
                    else:  ##投喂失败:已经达到投喂上限或者喂错食物了
                        print (f'编号{(roomList[room_num]).num}的{an.nickName} 投喂失败')
                        if an.eatNum == an.eatMaxNum:  # 已经达到投喂上限次数，去掉强提示
                            if rem.keys ().__contains__ (str ((roomList[room_num]).num)):
                                rem.pop (str ((roomList[room_num]).num))  # 喂过的去掉强提示
                            else:
                                pass
                        else:
                            if int (an.eatNum) == 0:  # 没加过提示就加提示
                                if (an.nickName == "老虎"):
                                    rem[str ((roomList[room_num]).num)] = "老虎"
                                    pass
                                elif (an.nickName == "羊"):
                                    rem[str ((roomList[room_num]).num)] = "羊"
                                else:
                                    pass
                        pass

                break

        else:
            print ("============================================游戏结束============================================")
            break
    return roomList
a=2222
print (f'{a}:9< {a} {a}')
roomList= game_demo(20)

print (f'打印的动物信息')
for roomone in roomList:
    print (f'{roomone.num},{roomone.anima.nickName},{roomone.anima.weight}')

# 添加异常
# 使用父类
# 使用多线程