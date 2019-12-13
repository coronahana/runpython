import re
import json

class  regex_demp:
    def regg(self):
        phone = "2004-959-559 # 这是一个国外电话号码"

        # 删除字符串中的 Python注释
        num = re.sub (r'#.*$', "", phone)
        print("电话号码是: ", num)
        # 删除非数字(-)的字符串
        num = re.sub (r'\D', "", phone)
        print("电话号码是 : ", num)

    def getprojectid_re(self):
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
    def getprojectid_re02(self):
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
def findstr():
    #提取出只包含数字以及字母，且以字母开头的最长子串
    strdemo ="pf%dfe%$$ddfsf222s%%5fddsf22sfsfddsdsdsss2222444f222asdf>22sdfsfd22"
    strlist = re.findall('[a-zA-Z]{1}[a-zA-Z0-9]+',strdemo)
    maxlen = 0
    for i in strlist:
        print (i)
        # print (f'{strlist.index(i)}-{maxlen}')
        if(str(i).__len__()>maxlen):
            maxlen = str(i).__len__()
            # print(maxlen)
            # print (f'if{maxlen}')
    print(maxlen)
    strlist.

if __name__ == '__main__':
    findstr()
    # regex_demp().getprojectid_re02( )
    # regex_demp().getprojectid_re()
    # regex_demp().regg()
