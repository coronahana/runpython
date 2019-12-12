"""
Selenium 作业 1

请到如下网址下载最新Chrome浏览器 的 web driver 驱动
https://chromedriver.storage.googleapis.com/index.html

pip 安装Selenium Web driver Python 客户端库
1. 访问天气查询网站（网址如下），查询江苏省天气
http://www.weather.com.cn/html/province/jiangsu.shtml

2. 获取江苏所有城市的天气，并找出其中每天最低气温最低的城市，显示出来，比如
温度最低为12℃, 城市有连云港 盐城
"""
from selenium import webdriver
def selenium_demo01():
    driver = webdriver.Chrome()
    driver.get("http://www.weather.com.cn/html/province/jiangsu.shtml")
    temp = driver.find_element_by_id("forecastID").find_elements_by_tag_name("dl")
    driver.implicitly_wait(10)
    lowdic ={}#存储城市和最低气温
    lowlist=[]#存储每个城市的最低温度
    for dldata in temp:
        cityName= dldata.find_element_by_tag_name("dt").text
        temlist= (dldata.find_element_by_tag_name("dd").text).replace("℃","").strip().split("/")
        lowTem = temlist[0]#低温
        highTem=temlist[-1] #高温

        lowdic[cityName]=lowTem
        lowlist.append(int(lowTem))
        pass
    minLowTem = min(lowlist)
    minLowTemCity=[]
    for one in lowdic:
        # print(one)
        if int(lowdic.get(one))== minLowTem :
            # print(one,minLowTem)
            minLowTemCity.append(one)
            return minLowTemCity,minLowTem
    driver.quit()
if __name__ == '__main__':
    mostLowCityAndTem = selenium_demo01()
    print(f'温度最低城市是{mostLowCityAndTem[0]}温度{mostLowCityAndTem[1]}℃')
    pass
"""
温度最低城市是['徐州']温度0℃
"""