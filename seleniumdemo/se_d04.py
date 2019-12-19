from selenium import webdriver
import time
"""
符合要求数据如下：
Python（安卓逆向）|杭州联仕企业管理咨询有限公司|杭州|1.5-5万/月|11-14
"""
def getNewJob():
    driver = webdriver.Chrome()
    driver.get("http://www.51job.com")
    driver.implicitly_wait(6)
    #点击高级搜索
    driver.find_element_by_css_selector("div.fltr.radius_5 > div > a.more").click()
    # 职能类别 选 计算机软件 -> 高级软件工程师
    # indtype_click

    driver.find_element_by_id ("funtype_click").click ()
    driver.find_element_by_id ("funtype_click_center_left_each_0100").click ()
    driver.find_element_by_id ("funtype_click_center_right_list_category_0100_0100").click ()
    driver.find_element_by_id ("funtype_click_center_right_list_sub_category_each_0100_0106").click ()
    driver.find_element_by_id ("funtype_click_bottom_save").click ()
    # 公司性质选 外资 欧美
    driver.find_element_by_css_selector ("#cottype_list span").click ()
    driver.find_element_by_css_selector ("#cottype_list > div > span:nth-child(3)").click ()
    #工作年限选 1-3 年
    driver.find_element_by_css_selector ("#workyear_list span").click ()
    driver.find_element_by_css_selector ("#workyear_list > div > span:nth-child(3)").click ()
    # 输入搜索关键词 python
    # 地区选择 杭州-先删除已经选中,在设置杭州
    driver.find_element_by_id ("work_position_click").click ()
    time.sleep (2)# 否则后面就报异常
    oldcity = driver.find_elements_by_css_selector ("#work_position_click_multiple_selected span.ttag")
    for city in oldcity:
        # print ("删除已经选中的城市")
        city.click()
    driver.find_element_by_id ("work_position_click_center_right_list_category_000000_080200").click ()
    driver.find_element_by_id ("work_position_click_bottom_save").click ()

    driver.find_element_by_id ("kwdselectid").send_keys ("python")
    #提交高级设置
    driver.find_element_by_css_selector ("span.p_but").click ()

    jobs = driver.find_elements_by_css_selector("#resultList div.el")
    for job in jobs[1:]:
        print((job.text).replace("\n","|"))

    driver.quit()
if __name__ == '__main__':
    getNewJob()
"""
Selenium 作业 4

登录 http://www.51job.com
    点击高级搜索
    输入搜索关键词 python 
    地区选择 杭州
    职能类别 选 计算机软件 -> 高级软件工程师
    公司性质选 外资 欧美
    工作年限选 1-3 年
    
搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
 
    Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
    Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27


【参考答案，往下翻】


# coding:utf8
from selenium import webdriver
executable_path = r"d:\tools\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path)
driver.implicitly_wait(10)

# 打开网址
driver.get('http://www.51job.com')

# 选择高级搜索 
driver.find_element_by_css_selector('div.ush > a').click()


# 输入选择关键词
driver.find_element_by_id('kwdselectid').send_keys('python')

# 工作地点选择
driver.find_element_by_id('work_position_input').click()

# 取消 已经选择的
selectedCityEles = driver.find_elements_by_css_selector('#work_position_click_center em[class=on]')

for one in selectedCityEles:
    one.click()

# 选杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()

# 保存选择
driver.find_element_by_id('work_position_click_bottom_save').click()


# 要点一下别的地方， 否则下面的元素会被挡住
driver.find_element_by_css_selector('div.tit').click()



# 职能类别 选 计算机软件 -> 高级软件工程师

driver.find_element_by_id('funtype_click').click()


driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()

driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()


driver.find_element_by_id('funtype_click_bottom_save').click()

# 公司性质选 外资 欧美
driver.find_element_by_id('cottype_list').click()
driver.find_element_by_css_selector('#cottype_list span.li[data-value="01"]').click()

# 工作年限选
driver.find_element_by_id('workyear_list').click()
driver.find_element_by_css_selector('#workyear_list span.li[data-value="02"]').click()

# 点击搜索
driver.find_element_by_css_selector('div.p_sou > span.p_but').click()

# 结果列表获取内容
jobs = driver.find_elements_by_css_selector('#resultList div[class=el]')


for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    stringFilelds = [field.text for field in fields]
    print (' | '.join(stringFilelds))


driver.quit()
"""