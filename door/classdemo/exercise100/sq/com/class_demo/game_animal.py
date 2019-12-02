from random  import  randint
import  time

class Tiger:
    callVoice = "WOW!!"
    nickName="老虎"
    isHungry = False
    def __init__(self, inifood, iniweight=200):
        self.food = inifood
        self.weight =iniweight
    def call(self):
        print(self.callVoice)
        self.weight-=5 # 如果叫体重就会减少5斤
        pass
    def feed(self,food):
        if(food=="mead"):
            print("虎喂对了")
            self.weight += 10
            self.isHungry = True
        else :
            self.weight -= 10

class Sheep:
    callVoice = "mie!!"
    nickName="羊"
    isHungry= False#喂过一次就不饿了
    def __init__(self, inifood, iniweight=100):
        self.weight = iniweight
        self.food = inifood

    def call(self):
        # 如果叫体重就会减少5斤
        print(self.callVoice)
        self.weight -= 5
        pass

    def feed(self,food):
        if(food == "grass"):
            print("羊喂对了")
            self.weight += 10
            self.isHungry=True
        else :
            self.weight -= 10
class Room:
    def __init__(self,ininum,inianima):
        self.num = ininum
        self.anima = inianima

def game_demo():
    print("开始游戏")
    # 记忆房间动物
    rem={"0":"房间号：动物名"}
    romList=[]
    #随机初始化10个房间的动物编号和动物
    for one in range(1,11):
        if randint(0,1):
            print("初始化一个老虎")
            ani = Room(str(one),Tiger("meat"))
        else:
            print("初始化一只羊")
            ani=  Room(str(one),Sheep("grass"))
        romList.append(ani)

    startime = time.time()
    while True :
        # 随机产生一个房间号，让用户选择喂食或者敲门
        room_num =randint(0,9)
        print("请您去房间号"+str(room_num+1)+"门口选择操作")
        # choose ="1"
        choose =""
        while True :
            choose = input("输入1喂食，输入2敲门！请选择操作，提示"+str(rem))
            if(choose=="1" or choose=="2"):
                break


        if(choose=="1"):
            # feedfood="meat" #或者grass 用户输入
            feedfood = input("输入meate或者grass！请输入")
            ((romList[room_num]).anima.feed(feedfood))
        else:
            #选则了敲门2
            an=(romList[room_num]).anima
            an.call()
            if(an.nickName=="老虎"):
                rem[str((romList[room_num]).num)]="老虎"
            else:
                rem[str((romList[room_num]).num)]= "羊"

        endtime=time.time()
        if((endtime-startime)>40):
            print("游戏结束")
            break
    for roomone in romList:
        print(str(roomone.num),roomone.anima.nickName,roomone.anima.isHungry,roomone.anima.weight)

    print(romList)

game_demo()





