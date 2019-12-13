
import requests
import json
from logind import LoginDemo

class InterfaceDemo(LoginDemo):

    name=19
    """
    
    def __init__(self):
        print("interfaceDemo___init__")
    """
    def newproject(self):
        print("interfaceDemo__newproject")
        url = 'https://xxxx.xxx.xx/login?src=https%3A%2F%2Fwww.vip.com%2F'

        data01 = {"loginName": "18126132321", "password": "long1234", "remUser": 0, "vipc": "", "captcha": "",
                  "anticache": "1534909211992", "whereFrom": ""}
        data02 = json.dumps(data01)
        print(data02)
        res = requests.post(url, data02)
        # res = requests.get(url, data)  # 直接用requests.get(url,data)即可，其中.get表示为get方法，不需要对字典类型的data进行处理
        # res=res.text#text方法是获取到响应为一个str，也不需要对res进行转换等处理
        res01 = res.text
        # res = res.json()# 当返回的数据是json串的时候直接用.json即可将res转换成字典
        print(res01)

    def newpro(self):
        print("interfaceDemo__newpro")
        print("name="+str(self.name))

        return "proid"

if __name__ == '__main__':

    InterfaceDemo().newpro()


