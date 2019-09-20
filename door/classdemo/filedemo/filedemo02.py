# -*- coding: UTF-8 -*-


def readflowdata():
    try:
        jj='willdeleteprojects.txt'
        f = open(jj, 'w')
        f.write("233#")
        f.write ("555#")
        f.write ("66#")
    finally:
        if f:
            f.close()

readflowdata()


f = open('willdeleteprojects.txt', 'r')
ggg=f.read()
oo = str(ggg).split("#")

for str01 in oo:
    if(str01!=""):
        print (int(str01))
        if(str01=="233"):
            #删除工程
            #删除成功后，将工程id在文件中删除
            try:
                f = open('willdeleteprojects.txt', 'r')
                ggg = f.read ()
                f.close ()
                newstrs = str(ggg).replace(str01,"")
                f = open('willdeleteprojects.txt', 'w')
                f.write(newstrs)
            finally:
                if f:
                    f.close ()
        print("wsxcde")
print(oo)

ds="ujhdhhdhd500hhdhhd"
print(ds.__contains__("500"))





