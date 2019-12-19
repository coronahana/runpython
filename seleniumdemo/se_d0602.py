import win32com.client
from selenium import webdriver
import time
def setup():
    driver = webdriver.Chrome ()
    driver.get ("https://tinypng.com/")
    driver.implicitly_wait (5)
    return  driver

def isUpload(driver,filepath):
    img_path = filepath
    imgname = (img_path.split("\\"))[-1]
    s = win32com.client.Dispatch ('WScript.Shell')
    driver.find_element_by_css_selector (".icon").click ()
    time.sleep (2)
    s.SendKeys (img_path, 0)
    time.sleep (3)
    s.SendKeys("{ENTER}", 0)
    s.SendKeys ("{ENTER}", 0)
    time.sleep (1) #给点上传文件的时间
    #失败的上传class="progress error"  成功的上传class="progress success"
    els= driver.find_elements_by_xpath ('//section/div/section/ul/li/div[@class="progress success"]')
    for el in els:
        es = el.find_elements_by_xpath (f'preceding-sibling::div[@title="{imgname}"]')
        if(es.__len__()==1):
            print("上传成功")
            return "success"
            break
        else:
            return "fail"
    pass
def tearDown(driver):
    driver.quit()


if __name__ == '__main__':
    # 测试控制台结果：
    # E:\Python\Python36\python.exe E:/PycharmProjects/runpython/seleniumdemo/se_d0602.py
    # 上传成功
    # 文件上传E:\example-shrunk.png：success
    # 文件上传C:\protobuf-java-2.5.0.jar：fail

    driver = setup()
    fileone=r"E:\example-shrunk.png"
    re= isUpload(driver,fileone)
    print(f'文件上传{fileone}：{re}')

    filetwo= r"C:\protobuf-java-2.5.0.jar"
    re = isUpload (driver,filetwo)
    print (f'文件上传{filetwo}：{re}')

    tearDown(driver)










"""
Selenium 作业 6
-- 作业2
写一个程序实现如下的自动化过程

- 登录   https://tinypng.com/
- 点击 上传文件的虚线框
- 选择 插图，在本地目录中选择一张准备好的图片 , 查看是否能够上传图片成功


-- 作业1


登录华为官网 https://www.vmall.com/，
点击 "华为官网" 链接

检查 "华为官网" 页面上是否 有如下主菜单

  智能手机
  笔记本
  平板
  穿戴设备
  智能家居
  更多产品
  软件应用
  服务与支持



最后再回到主窗口， 检查鼠标停留在 "笔记本&平板" 处的时候， 是否显示的菜单有
"平板电脑  笔记本电脑 笔记本配件"

怎么模拟鼠标停留事件，请大家自行网上搜索，看看能不能自己解决问题。





【参考答案，往下翻】































from selenium import  webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)


driver.get('https://www.vmall.com/')


driver.find_element_by_css_selector(
    'a[href="http://consumer.huawei.com/cn/"]'
).click()


driver.find_element_by_css_selector(
    '.s-sub li:nth-last-child(1)'
).click()

driver.find_element_by_css_selector(
    'a[href="http://appstore.huawei.com/"]'
).click()


def checkHuaWei():
    expected = '智能手机|笔记本|平板|智能穿戴|智能家居|更多产品|软件应用|服务与支持'

    # 注意窗口的宽度决定显示多少个菜单，可能需要拉宽窗口
    # 先不写下面的代码，发现错误再添加
    size = driver.get_window_size()
    driver.set_window_size(1520, size['height'])

    eles = driver.find_elements_by_css_selector(".left-box .nav-cnt > li")
    eleTexts = [ele.text for ele in eles]


    actual = '|'.join(eleTexts)
    if actual == expected:
        print('huawei page pass')
    else:
        print('huawei page fail!!!!')





def checkVmail():
    expected = '''平板电脑|笔记本电脑|笔记本配件'''
    from selenium.webdriver.common.action_chains import ActionChains
    ac = ActionChains(driver)

    ac.move_to_element(driver.find_element_by_id('zxnav_1')).perform()

    # 用 setTimeout(function(){debugger;},3000) 来 查看元素
    # 分析 得知  zxnav_1 ，2,3,4  分别就是对应 菜单的，里面有隐藏菜单
    eles = driver.find_elements_by_css_selector('#zxnav_1 .subcate-item a span')
    eleTexts = [ele.text for ele in eles]
    actual = '|'.join(eleTexts)
    if actual == expected:
        print('main page pass')
    else:
        print('main page fail!!!!')


for handle in driver.window_handles:
    driver.switch_to.window(handle)

    if '消费者业务官网' in driver.title:
        checkHuaWei()
    else:
        checkVmail()




driver.quit()

"""