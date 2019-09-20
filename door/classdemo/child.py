from door.classdemo import fatherc

class child(fatherc.Father):


    name ="xiaoniu"
    def csex(self):
        #print("cnan")
        super().sex()

    def csex02(self):
        print("cnan02")

    def csex03(self):
        print("cnan02")
""
if __name__ == '__main__':

    child().csex()
""