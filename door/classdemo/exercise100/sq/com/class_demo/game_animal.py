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
        if (self.eatNum <3):
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
    callVoice = "mie!!"
    nickName="羊"
    eatNum = 0  # 吃的次数
    callNum = 0  # 叫的次数
    def __init__(self, inifood,inieatMaxNum,inicallMaxNum,iniweight=100):
        self.weight = iniweight
        self.food = inifood
        self.eatMaxNum =inieatMaxNum
        self.callMaxNum = inicallMaxNum
    def call(self):
        # 如果叫体重就会减少5斤
        print(self.callVoice)
        self.weight -= 5
        pass

    def feed(self,food):
        if(self.eatNum <3):
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
            ani = Room(str(one),Tiger("meat",3,1))
        else:
            # print("初始化一只羊")
            ani=  Room(str(one),Sheep("grass",2,1))
        roomList.append(ani)
    # 完成初始化
    print("============================================开始游戏============================================")
    print ("\n-游戏规则默认每只老虎能喂3次、每只羊只能喂2次，都只能叫1次\n-游戏时间" + str (game_Maxtime) + "s\n")
    startime = time.time()
    while True :
        #随机产生一个房间号，让用户选择喂食或者敲门
        room_num =randint(0,9)
        print("请您去房间号"+str(room_num+1)+"门口选择操作 \n")
        while True :
            endtime = time.time ()
            if ((endtime - startime) > int (game_Maxtime)):
                print ("============================================游戏结束============================================")
                break
            choose = input("输入1喂食,输入2敲门,提示"+str(rem)+"\n")
            if(choose=="1" or choose=="2"):
                break
        an = (roomList[room_num]).anima
        if(choose=="1"):
            # 喂食1
            feedfood = input("输入meate或者grass！请输入 ")
            res=(an.feed(feedfood))
            if(res=="success"):
                print("编号"+str((roomList[room_num]).num)+"的"+an.nickName+"成功吃到"+an.food)
                if rem.keys().__contains__(str((roomList[room_num]).num)):
                    rem.pop(str((roomList[room_num]).num))#喂过的去掉强提示
                pass
            else:
                pass
        else:
            #敲门2

            if an.callNum<an.callMaxNum:
                an.call()
                if (an.nickName == "老虎"):
                    if an.callNum >=an.eatMaxNum:
                        pass
                    else:
                        #添加老虎还能喂强提示2
                        rem[str((roomList[room_num]).num)] = "老虎"
                else:

                    if an.callNum >=an.eatMaxNum:
                        pass
                    else:
                        # 添加羊还能喂#print(romList)的强提示
                        rem[str ((roomList[room_num]).num)] = "羊"
            else:
                print (an.nickName + "叫够次数了,不叫了")
        endtime = time.time ()
        if ((endtime - startime) > int (game_Maxtime)):
            print ("============================================游戏结束============================================")
            break

    return roomList

roomList= game_demo(40)
for roomone in roomList:
    print (str (roomone.num), roomone.anima.nickName, roomone.anima.weight)
#print(romList)


