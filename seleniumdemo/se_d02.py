"""
打开百度新歌榜， http://music.baidu.com/top/new

在排名前50的歌曲中，找出其中排名上升的歌曲和演唱者

注意： 有的歌曲名里面有 "影视原声" 这样的标签， 要去掉


最终结果显示的结果如下：
我不能忘记你       :  林忆莲
等                :  严艺丹
飞天              :  云朵
粉墨              :  霍尊
春风十里不如你     :  李健

"""

"""
思路：
打开页面
找到前50数据
    识别上升
    歌曲和演唱者
    歌曲名里面有 "影视原声"去掉
    
"""
import traceback
from  selenium  import webdriver
def songlist():
    driver= webdriver.Chrome(r'E:\Python\webdriver\72\chromedriver.exe')
    driver.get('http://music.baidu.com/top/new')
    driver.implicitly_wait(3)
    elem = driver.find_elements_by_id('__qianqian_pop_closebtn')
    if elem is not []:
        # print('关闭弹框')
        elem[0].click()
    #$x('//div[@id="songListWrapper"]/div/ul/li[15]/div/span[5]/span/a')
    tempul= driver.find_element_by_xpath('//div[@id="songListWrapper"]/div/ul')
    temps=tempul.find_elements_by_tag_name('li')
    for temp in range(1,temps.__len__()+1):
        try :
            singer = (driver.find_element_by_xpath(f'//div[@id="songListWrapper"]/div/ul/li[{temp}]/div/span[@class="singer"]')).text
            songtemp = (driver.find_element_by_xpath (f'//div[@id="songListWrapper"]/div/ul/li[{temp}]/div/span[@class="song-title "]')).text
            if str(songtemp).__contains__("（"):
                song = songtemp.split("（")[0]
            else:
                song=songtemp
            songStatus = (driver.find_element_by_xpath (f'//div[@id="songListWrapper"]/div/ul/li[{temp}]/div/span[2]/i')).get_attribute("class")
            if(songStatus == "up"):
                print(f'{song}:{singer}')
        except Exception as e:
            print(f'当前元素定位失败-{traceback.format_exc()}')
        finally:
            pass
    # driver.quit()

if __name__ == '__main__':
    songlist()
"""
爱的箴言:黄渤/王珞丹/白客/谭卓
心如止水:Selina任家萱
你的答案:酷
游戏的意义:Y星人／Cheryl Chen
槐花香:贾凡
陪你去流浪:薛之谦
偏爱:阿肆
鹤·焰:萨顶顶
青山白云:戴荃
新将相和:徐鹤尼
Decisions:Stepken
清新的小女孩:69
我不要一个人在楼道里唱歌:吴克群
抱着你:胡海泉
不该拥有的事情-男女对唱版:蔡旻佑/张牧乔
酒醉的蝴蝶–骏仔:骏仔
我不是张智成:张智成
蛋头先生:空岛
Zoo (chinese version):KikoBlob
山楂:王圆坤
怕什么:VOGUE 5
千面:逍遥乐队
不该拥有的事情-孤单版:蔡旻佑
朔望之归:洛兵
瞎扯:王啸坤
野狼Disco:故事与她
喜欢你:井胧
我想做个梦:舒米恩
要自由:BongBong乐团
"""

