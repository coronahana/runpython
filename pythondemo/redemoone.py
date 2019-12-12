# author：xintian   time:2019-12-06
#设置读取网页的头部，该行代码主要用于模拟浏览器来访问网站
# _header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
#https://search.51job.com/
#51job
#1- 模拟浏览器发出请求
import requests
import re
import xlwt #写表的
url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99°reefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
reps = requests.get(url)
#2- 获取页面返回的内容
reps.encoding = 'gbk'
print(reps.text)#字符串
# print(reps.content)#字节

pageNum = int(re.findall('<span class="td">共(.+?)页，到第</span>',reps.text,re.S)[0])
print(pageNum)
#-----------------写出列表--------------
workBook = xlwt.Workbook(encoding='utf-8')#创建excel表文件对象
workSheet = workBook.add_sheet('51job')#创建子表单
colNames = ['职位名','公司名','工作地点','薪资','发布时间']
for col in range(len(colNames)):
    #第一行------0
    workSheet.write(0,col,colNames[col])#(行，列，值)
#--------------------------------------
lineNum = 1#起始值
#3- 提取有用的数据----正则表达式
#提取所有的工作信息

for page in range(1,pageNum+1):
    url = f'https://search.51job.com/list/010000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,{page}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99°reefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    reps = requests.get(url)
    # 2- 获取页面返回的内容
    reps.encoding = 'gbk'
    linesInfo = re.findall('<div class="el">(.*?)</div>',reps.text,re.S)
    for line in linesInfo:#每一个岗位的详情
        #1- 获取岗位名称
        temp = re.findall('<a target="_blank" title="(.*?)"',line,re.S)
        jobName = temp[0]
        workSheet.write(lineNum,0,jobName)
        #2- 获取公司名称
        company = temp[1]
        workSheet.write(lineNum, 1, company)
        #3- 获取地址
        address = re.findall('<span class="t3">(.*?)</span>',line,re.S)[0]
        workSheet.write(lineNum, 2, address)
        #4- 获取薪资
        salary = re.findall('<span class="t4">(.*?)</span>', line, re.S)[0]
        workSheet.write(lineNum, 3, salary)
        #5- 发布时间
        jobTime = re.findall('<span class="t5">(.*?)</span>', line, re.S)[0]
        workSheet.write(lineNum, 4, jobTime)
        lineNum += 1
    # print(jobName,company,address,salary,jobTime)
#4- 存储excel
#保存excel
workBook.save('G:\\51job_res.xls')

'''
https://search.51job.com/list/010000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99°reefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
https://search.51job.com/list/010000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99°reefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
'''