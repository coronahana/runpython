name = "python"
name02 = "python02"
if (name == "python"):
    print("you  like python")
if (name02 == 'python02'):
    print("you do not like python")
print("----------------------------------------------------------------------------------------")
def iscontain(strS,contstr):
    if strS.find (contstr) == -1:
        print ("Found " + contstr + " not in " + strS)
        #print(strS.find (contstr) )
        return False
    else:
        print("Found "+contstr+" in "+strS)
        #print (strS.find (contstr))
        return True
ww= iscontain("ianname","name")
print("ww")
print(ww)
print("----------------------------------------------------------------------------------------")
aa=["cos","本地"]
bb=["北京","上海","广州","深圳","长春"]
cc=["新增","已有版本"]
print(aa.__contains__("a"))
cases=[]
for str01 in aa:
    case=""
    for str02 in bb:
        for str03 in cc:
            case = str01 + "-" + str02 + "-" + str03
            if cases.__contains__(case)==False:
                cases.append(case)
                print(case)


print(cases.__len__())
print(cases)
print("----------------------------------------------------------------------------------------")



