from selenium import webdriver
import time

from selenium.webdriver.support.select import Select
import time
"""
执行结果在文本(se_d05_results)内保存

"""
def findTickets():
    #setup
    driver = webdriver.Chrome()
    driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
    driver.implicitly_wait(6)

    driver.find_element_by_id("fromStationText").clear()
    driver.find_element_by_id ("fromStationText").click()
    driver.find_element_by_id("fromStationText").send_keys("南京南\n")

    driver.find_element_by_id("toStationText").clear()
    driver.find_element_by_id ("toStationText").click()
    driver.find_element_by_id("toStationText").send_keys("杭州东\n")

    Select(driver.find_element_by_id("cc_start_time")).select_by_visible_text("06:00--12:00")
    driver.find_element_by_xpath("//*[@id='date_range']/ul/li[2]/span[1]").click()
    #加载搜索结果
    time.sleep(5)
    allticket = driver.find_elements_by_xpath('//*[@id="queryLeftTable"]/tr[contains(@id,"ticket_")]') #是否有票
    for ticket in allticket:
        ishave = ticket.find_element_by_xpath("./td[4]").text
        # 判断二等座是否有票
        if(ishave not in ["无","--","候补"]):
            ticketName = ticket.find_element_by_xpath('./td[1]/div[1]/div[1]/div[1]/a[1]').text
            print(ticketName)
    print("前面执行完了")
    #teardow
    #driver.quit()

if __name__ == '__main__':
    findTickets()
    print("方法调用完成")
"""
Selenium 作业 5
打开 12306 网站  https://kyfw.12306.cn/otn/leftTicket/init
出发城市 填写 ‘南京南’， 到达城市 填写 ‘杭州东’ 
注意输入城市名前，一定要先点击一下输入框，否则查不到。 
而且输入城市名最后要包含一个回车符，否则输入框里面会自动清除
发车时间 选 06:00--12:00

发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签
我们要查找的是所有 二等座还有票的车次，打印出这些有票的车次的信息（这里可以用xpath），结果如下：

G7641
G1505
G7393
G7689


【参考答案，往下翻】































from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

fromEle = driver.find_element_by_id('fromStationText')
# 为什么这里要点击一下
fromEle.click()

fromEle.clear()
fromEle.send_keys(u'南京南\n')

toEle = driver.find_element_by_id('toStationText')

toEle.click()
toEle.clear()
toEle.send_keys(u'杭州东\n')

# 输入开始时间，
timeSelect =  Select(driver.find_element_by_id('cc_start_time'))
timeSelect.select_by_visible_text('06:00--12:00')


tomorrow = driver.find_element_by_css_selector('#date_range li:nth-child(2)')
# 点击这个，就会搜索车次了
tomorrow.click()

# 方法一：用xpath实现获取二等座有票的车次信息
print('\n\n\n===============================\n\n\n')
xpath ='//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'

theTrains = driver.find_elements_by_xpath(xpath)
for one in theTrains:
    print (one.text)



# 方法二：用css实现获取二等座有票的车次信息
print('\n\n\n===============================\n\n\n')
theTrainLines = driver.find_elements_by_css_selector('#queryLeftTable > tr')
# 先不加这个，发现特别慢
driver.implicitly_wait(0)
for one in theTrainLines:
    secondlevelseat = one.find_elements_by_css_selector('td:nth-of-type(4)[class]')
    if secondlevelseat:
        print (one.find_element_by_css_selector('td:nth-of-type(1) a').text)
driver.implicitly_wait(10)
driver.quit()
"""