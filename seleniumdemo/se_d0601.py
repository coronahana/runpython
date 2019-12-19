from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
def setup():
    driver = webdriver.Chrome ()
    driver.get ("https://www.vmall.com/")
    driver.implicitly_wait (5)
    return  driver
def checkHuawei(driver):
    driver.find_element_by_xpath ('//div[@class="s-sub"]/ul/li[2]').click ()
    # 屏幕放大
    driver.fullscreen_window()
    wins = driver.window_handles
    driver.switch_to.window (wins[1])
    # 检查"华为官网"页面上是否有如下主菜单
    allItems = ["智能手机", "笔记本", "平板", "穿戴设备", "智能家居", "更多产品", "软件应用", "服务与支持"]
    onlineItem = []
    eles = driver.find_elements_by_css_selector (
        "#header-v3 > div.header-wrap > div.nav-wrap > div.left-box > ul > li > a")
    print (f'{driver.current_url}当前URL---------------')
    for el in eles:
        onlineItem.append (el.text)
    for item in allItems:
        if item in onlineItem:  #
            print (f'菜单{onlineItem}中包含 {item}')
        else:
            print (f'菜单{onlineItem}中不包含 {item}')
    return wins



def checkItem(driver,wins):
    #回到主窗口
    driver.switch_to.window (wins[0])
    print (f'{driver.current_url}当前URL----------------')
    time.sleep(1)
    attrible=  driver.find_element_by_link_text ("笔记本 & 平板")
    ActionChains (driver).move_to_element (attrible).perform()
    # print (attrible.text) #笔记本 & 平板
    temps = driver.find_elements_by_xpath('//*[@id="zxnav_1"]/div[2]/ul/li')
    #悬停显示的菜单
    move_afters=[]
    for temp in temps:
        move_afters.append(temp.find_element_by_tag_name("a").text)
    #菜单中是否包含"平板电脑  笔记本电脑 笔记本配件"
    islist=["平板电脑","笔记本电脑","笔记本配件"]
    for item in move_afters:
        if item in islist:  #
            print (f'菜单{move_afters}中包含 {item}')
        else:
            print (f'菜单{move_afters}中不包含 {item}')
def tearDown(driver):
    driver.quit()

if __name__ == '__main__':
    driver= setup ()
    wins=checkHuawei(driver)
    checkItem(driver, wins)
    tearDown (driver)
    pass

"""
Selenium 作业 6
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



-- 作业2
写一个程序实现如下的自动化过程

- 登录   https://tinypng.com/
- 点击 上传文件的虚线框
- 选择 插图，在本地目录中选择一张准备好的图片 , 查看是否能够上传图片成功

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