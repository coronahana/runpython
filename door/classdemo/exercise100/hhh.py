import re
import json

hh='{"return_code":1,"return_msg":"OK","return_data":{"taskid":329,"taskname":"CreateCluster","clustername":"tx2019_test_40"}}{"return_code":1,"return_msg":"OK","return_data":null}'
print(hh)
num = re.sub (r'{"return_code":1,"return_msg":"OK","return_data":null}', "", hh)
print("截取house : ", num)
dd = json.loads(num)
print(dd["return_data"])
print(dd["return_msg"])
print(str(dd["return_code"]))

print("hhhh"=="hhhh")
