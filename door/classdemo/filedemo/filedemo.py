# -*- coding: UTF-8 -*-


def readflowdata():
    try:
        jj='newflow_json.txt'
        f = open (jj, 'rb')
        print(f.read ())
    finally:
        if f:
            f.close ()

readflowdata()
#print("kkkk\nooooo")

name01="hhh"
name02="kkkk"
hyperPa_flowId=44
kkk =  {"globalParams":name01+"= 9\n"+name02+" = ooo"}
print(kkk)
print(kkk["globalParams"])




hyperPa_num_name="na01"
hyperPa_num_name_s=1
hyperPa_num_name_e=5
hyperPa_num_name_interval=2
hyperPa_str_name="na02"
enumV = "hhh kkk jjjj"



#params02={"paramArray":[{"name":"+hyperPa_num_name+","start":""+hyperPa_num_name_s+"","end":""+hyperPa_num_name_e+"","interval":""+hyperPa_num_name_interval+""},{"name":""+hyperPa_str_name+"","enum":""+enumV+""}]}
params03= {"paramArray":[{"name": hyperPa_num_name,"start": str(hyperPa_num_name_s),"end":str(hyperPa_num_name_e),"interval": str(hyperPa_num_name_interval)},{"name":  hyperPa_str_name ,"enum":enumV}]}
print(params03)

hyperPa_str_name_vaules ="va01#va02#va03"
print(hyperPa_str_name_vaules.replace("#"," "))

ooooo = [{"globalParams":name01+"= 9\n"+name02+" = ooo"},{"globalParams":name01+"= 9\n"+name02+" = ooo"}]
print("\""+str(ooooo)+"\"")
print(kkk["globalParams"])
import random

boundary = '-----------------------------' + str (random.randint (1e28, 1e29 - 1))

print(boundary)
