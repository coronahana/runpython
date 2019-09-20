from door.classdemo  import fatherc
import re
class  testd:

    def getdata(self):
        print("dssdsd")
        fatherc.Father().sex()

    def getreg(self):

        strrespaon = '{"success" : true,"data" : "{\"id\":1205,\"status\":\"success\",\"path\":\"manager?project=工程名称\",\"action\":\"redirect\"}"}'
        """
        {
          "success" : true,
          "data" : "{\"id\":1205,\"status\":\"success\",\"path\":\"manager?project=工程名称\",\"action\":\"redirect\"}"
        }
        """
        print(strrespaon)


        phone = "2004-959-559 # 这是一个国外电话号码"

        # 删除字符串中的 Python注释
        num = re.sub(r'#.*$', "", phone)
        print("电话号码是: ", num)

        num02 = re.sub (r'[0-9]{4}]', "", phone)
        print ("电话号码是: ", num02)


    def kkk(self):
        for i in 10:
            print(str(i)+"ooooooo varchar(255),")
if __name__ == '__main__':
    #testd().getdata()
    #testd().getreg()
    testd ().kkk ()




