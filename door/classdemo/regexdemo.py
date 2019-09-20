import re
import json
def regg():
    phone = "2004-959-559 # 这是一个国外电话号码"

    # 删除字符串中的 Python注释
    num = re.sub (r'#.*$', "", phone)
    print("电话号码是: ", num)

    # 删除非数字(-)的字符串
    num = re.sub (r'\D', "", phone)
    print("电话号码是 : ", num)

def getprojectid_re( ):
    proresp_data = {"data": "{\"id\":1458,\"status\":\"success\",\"path\":\"manager?project=proname1903\",\"action\":\"redirect\"}","success": "true"}
    id = 0;
    p = re.compile (':\d{4}')
    dd = p.findall (json.dumps (proresp_data))
    # print(dd.__len__())
    if (dd.__len__ () == 1):
        mm = re.compile ('\d{4}').findall (dd[0])
        id = mm[0]
        print (id)
    return  id
#getprojectid_re()
def getprojectid_re02( ):
    proresp_data = {"data": "{\"id\":14538,\"status\":\"success\",\"path\":\"manager?project=proname1903\",\"action\":\"redirect\"}","success": "true"}
    #params = (json.loads(proresp_data))['data']
    #print (params)
    id = 0;
    p = re.compile (':\d+')
    dd = p.findall (json.dumps (proresp_data))
    # print(dd.__len__())
    if (dd.__len__ () == 1):
        mm = re.compile ('\d+').findall (dd[0])
        id = mm[0]
        print (id)
    return  id
#getprojectid_re02( )
regg()