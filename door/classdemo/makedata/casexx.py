def hhh(strS,contstr):
    #s = "This be a string"
    if strS.find (contstr) == -1:
        #print ("Found " + contstr + " not in " + strS)
        #print(strS.find (contstr) )
        return False
    else:
        #print("Found "+contstr+" in "+strS)
        #print (strS.find (contstr))
        return True
def makecases():
    aa=["cos","本地"]
    bb=["PMML","ONNX","XGBOOST","ANGEL","TFServing"]
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

def makecases02():
    aa = ["cos", "本地"]
    bb = ["PMML", "ONNX", "XGBOOST", "ANGEL", "TFServing"]

    print (aa.__contains__ ("a"))

    cases = []

    for str01 in aa:
        case = ""
        for str02 in bb:

                case = str01 + "-" + str02
                if cases.__contains__ (case) == False:
                    cases.append (case)
                    print (case)
    print (cases.__len__ ())
    print (cases)

makecases()