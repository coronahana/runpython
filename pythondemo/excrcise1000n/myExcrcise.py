# 请写一个函数reverse，参数是一个列表，该函数将列表中的所有元素倒序排列并返回
def myreverse_wrong(listone):
    #listone[1, 2, 3, 4, 5]
    if listone==[]:
        return []
    else:
        newlist=listone
        print(f'原 始-{listone}\n') #原 始-[1, 2, 3, 4, 5]
        for i in range(listone.__len__()):
            newlist[i]=listone[listone.__len__()-i-1]
        print (f'反转后-{newlist}\n') #反转后-[5, 4, 3, 4, 5]
        return newlist
    pass

def myreverse(listone):
    """
        请写一个函数reverse，参数是一个列表，该函数返回一个新的列表， 新列表中元素是参数列表的倒序。
        注意，该函数调用后不能改变原来参数列表的内容
    """
    if listone==[]:
        return []
    else:
        newlist =[0 for x in range(0,listone.__len__())]
        print(f'原 始-{listone}\n')
        for i in range(listone.__len__()):
            newlist[i]=listone[listone.__len__()-i-1]
        print (f'反转后-{newlist}\n')
        print (f'原 始-{listone}\n')
        return newlist
    pass
def reverse_anser(inlist):
    # 防止改变参数列表，先拷贝生成新列表
    print (f'原 始-{inlist}\n')
    newlist = [i for i in inlist]
    newlist.reverse()
    print (f'反转后-{newlist}\n')
    print (f'反转后原始-{inlist}\n')
    return newlist

def myreverse_anser(listone):
    #改变了原始的列表
    print (f'原 始-{listone}\n')
    listone.reverse()
    print (f'反转后-{listone}\n')#反转后-[5, 4, 3, 2, 1]
    return listone
import  traceback
def tri_area(length,high):
    """
     请写一个函数tri_area，参数是三角形的底和高，请计算返回三角形面积
    比如
    tri_area(3, 2) ➞ 3
    tri_area(7, 4) ➞ 14
    tri_area(10, 10) ➞ 50
    """
    try:
        if length>0 and high>0:
            area=int(length*high/2)
    except:
        print(f'输入异常，无法计算{traceback.format_exc()}')
    return area
def remainder(a,b):
    """
    请写一个函数remainder，参数是两个数字，请计算返回这两个数字相除的余数
    比如
    remainder(1, 3) ➞ 1

    remainder(5, 5) ➞ 0

    remainder(7, 2) ➞ 1
    """
    try:
        if a >= 0 and b > 0:
            yu = int (a%b)
    except:
        print (f'输入异常，无法计算{traceback.format_exc()}')
    return  yu

def animals(gugu,meme,henghegn):
    """
        农场上有3种动物：鸡、奶牛、猪
        请写一个函数animals，该函数有3个参数，分别是鸡、奶牛、猪的个数，请计算返回这么多的动物总共有多少条腿
        比如
        animals(2, 3, 5) ➞ 36
        animals(1, 2, 3) ➞ 22
        animals(5, 2, 8) ➞ 50
        :return:
        """
    try:
        if gugu.isdigit() and meme.isdigit() and henghegn.isdigit() :
            hands = gugu*2+meme*4+henghegn*4
    except:
        print(f'输入有误{traceback.format_exc()}')
    return hands
def concat(list01,list02):
    """
      请写一个函数concat，参数分别是两个列表，请返回两个列表合并的结果
比如
concat([1, 3, 5], [2, 6, 8]) ➞ [1, 3, 5, 2, 6, 8]
concat([7, 8], [10, 9, 1, 1, 2]) ➞ [7, 8, 10, 9, 1, 1, 2]
concat([4, 5, 1], [3, 3, 3, 3, 3]) ➞ [4, 5, 1, 3, 3, 3, 3, 3]
    :return:
    """
    try:
        if type(list01) ==list  and type(list02)==list:
            return list01+list02
    except:
        print(f'输入有误{traceback.format_exc()}')
def findLargestNum(listone):
    """
    请写一个函数findLargestNum，参数分别是1个列表，里面的元素都是数字，请返回该列表中最大的数字
比如
findLargestNum([4, 5, 1, 3]) ➞ 5
findLargestNum([300, 200, 600, 150]) ➞ 600
findLargestNum([1000, 1001, 857, 1]) ➞ 1001
    :return:
    """
    try:
        maxone= max(listone)
    except:
        print(f'输入有误{traceback.format_exc()}')
    return maxone
def findSmallestNum(list01):
    """
     请写一个函数findSmallestNum，参数分别是1个列表，里面的元素都是数字，请返回该列表中最小的数字
比如
findSmallestNum([34, 15, 88, 2]) ➞ 2
findSmallestNum([34, -345, -1, 100]) ➞ -345
    :return:
    """
    try:
        minone= min(list01)
    except:
        print(f'输入有误{traceback.format_exc()}')
    return minone
def ctoa(charone):
    """
      请写一个函数ctoa，参数是1个字母，请返回该字母对应的ASCII码数字
比如
ctoa("A") ➞ 65
ctoa("m") ➞ 109
ctoa("[") ➞ 91
    :return:
    """
    try:
        ordNum = ord(charone)
    except:
        print (f'输入有误{traceback.format_exc()}')
    return ordNum
def is_symmetrical(oneNum):
    """
    请写一个函数is_symmetrical，参数是1个数字，请返回该数字是否对称
    比如
    is_symmetrical(7227) ➞ True
    is_symmetrical(12567) ➞ False
    is_symmetrical(12521) ➞ True
    is_symmetrical(44444444) ➞ True
    :return:
    """
    if oneNum.isdigit():
        isNum = True
        for i in range(str(oneNum).__len__()):
            if oneNum[i]==oneNum[str(oneNum).__len__()-i-1]:
                isNum=True
            else:
                isNum = False
        return isNum
    else:
        return False
def find_odd(oneList):
    """
     请写一个函数find_odd，参数是1个列表，请返回该列表中出现奇数次的元素
比如
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1
find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5
find_odd([10]) ➞ 10

    :return:
    """
    dictNum={}
    jishuNum = []
    for i in oneList:
        if i not in dictNum:
            dictNum[i]=0
        else:
            dictNum[i]= dictNum[i]+1

    for i in dictNum:
        if dictNum[i]%2==0:
            jishuNum.append(i)

    return jishuNum

def is_valid_PIN(oneStr):
    """
    ATM机允许4或6位PIN码，PIN码只能包含4位数或6位数字。
    请写一个参数为字符串的函数，如果PIN有效则返回True，如果不是则返回False。
    比如
    is_valid_PIN("1234") ➞ True
    is_valid_PIN("12345") ➞ False
    is_valid_PIN("a234") ➞ False
    is_valid_PIN("") ➞ False
    :return:
    """
    if oneStr.__len__()==4 or (oneStr.__len__()==6 and oneStr.isdigit()):
        return True
    else:
        return False
def indexOfCaps(oneStr):
    """
    请写一个函数，该函数 参数为1个字符串，请分析并返回包含字符串中所有大写字母索引的有序列表。
    比如
    indexOfCaps("eDaBiT") ➞ [1, 3, 5]
    indexOfCaps("eQuINoX") ➞ [1, 3, 4, 6]
    indexOfCaps("determine") ➞ []
        :return:
    答案：可以用  if ord('A') <= ord(ch) <= ord('Z') :
    """
    strIndex=[]
    for temp in oneStr:
        if temp.isupper():
            strIndex.append(int(oneStr.index(temp)))
    return  strIndex
def removeDups(oneList):
    """
     请写一个函数，该函数 参数为1个列表，删除所有重复的元素，并以与旧列表相同的顺序返回新列表（减去重复项）。
比如
removeDups(["John", "Taylor", "John"]) ➞ ["John", "Taylor"]
removeDups([1, 0, 1, 0]) ➞ [1, 0]
removeDups(['The', 'big', 'cat']) ➞ ['The', 'big', 'cat']
    :return:
    """
    for i  in oneList:
        if oneList.count(i)>1:
            for j in range(
                            oneList.count(i)-1):
                oneList.remove(i)
    return oneList
def sumboforei(oneList):
    """
    请写一个函数，该函数 参数为数字列表，请算出另外一个列表，里面每个元素依次是参数列表里面元素的累计和。
比如 参数为[1, 2, 3, 4]
结果计算方法为[1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]
返回结果就应该是[1, 3, 6, 10]
    :return:
    """
    newlist=[0 for aa in range(oneList.__len__())]
    for i in range(oneList.__len__()):
        for j in range(i+1):
            newlist[i]+=oneList[j]
    return newlist

def validate_phone(oneStr):
    """
    请写一个函数，该函数 参数为一个字符串，请验证该字符串是否是一个合法的电话号码，合法返回True，否则返回False
规则如下
	该字符串必须全部都是数字。
	该字符串长度为11位。
	该字符必须以数字1开头。
比如
validate_phone("13423445566") ➞ True
validate_phone(".23rfs") ➞ False
    :return:
    """
    if oneStr.__len__()==11 and oneStr.startswith("1")  and oneStr.isdigit():
        return True
    else:
        return False
def progress_weeks(oneList):
    """
    为了训练即将到来的马拉松，小明每周进行一次长跑。如果一周比上周跑的里程多，这周就是被称之为 进展周
写一个函数progress_weeks，该函数参数是每周长跑的里程列表，这个函数要并返回共有几个进展周。
比如
progress_weeks([3, 4, 1, 2]) ➞ 2
# 因为(3->4) 和 (1->2) 这两次是提高了
progress_weeks([10, 11, 12, 9, 10]) ➞ 3
    :return:
    """
    upweek=0
    for i in range(oneList.__len__()-1):

        if oneList[i] < oneList[i+1]:
            upweek+=1
    return upweek
def concat2(*kw):
    """
    写一个函数concat，该函数参数是n个列表，这个函数要将这n个列表拼接起来并返回。 注意n个数是不确定的。
    比如
    concat([1, 2, 3], [4, 5], [6, 7]) ➞ [1, 2, 3, 4, 5, 6, 7]
    concat([1], [2], [3], [4], [5], [6], [7]) ➞ [1, 2, 3, 4, 5, 6, 7]
    concat([1, 2], [3, 4]) ➞ [1, 2, 3, 4]
    concat([4, 4, 4, 4, 4]) ➞ [4, 4, 4, 4, 4]
    """
    #可变数参数  不管传进来几个参数，都是放在一个tuple中的
    newlist=[]
    print(type(kw))
    for i in kw:
        if type(i)==list:
            newlist=newlist+i
    return newlist

def myReplace(oneStr,twoStr):
    """
    写一个函数replace，该函数参数是两个字符串，
第一个参数给出一个源，
第二个参数是指定范围。
要求该函数将 第一个参数里面的字符串中 落在第二个参数指定范围内的字符串替换为 # 号

比如
replace("abcdef", "c-e") ➞ "ab###f"
replace("rattle", "r-z") ➞ "#a##le"
replace("microscopic", "i-i") ➞ "m#croscop#c"
replace("", "a-z") ➞ ""
    :return:
    """
    newstr=""
    b01,b02=twoStr.split("-")
    for i  in oneStr:
        if b01<=i<=b02:
            newstr+="#"
            pass
        else:
            newstr += i
    return newstr

def alphabet_index(oneStr):
    """
    写一个函数alphabet_index，该函数参数是1个字符串，

要求该函数返回一个新字符串，里面是 参数字符串中每个字母依次对应的 数字。如果是非字母，则忽略它

字母"a" 和"A" 都对应 1, "b"和"B"都对应2, "c"和"C"对应3， 依次类推

比如

alphabet_index("Wow, does that work?")
➞ "23 15 23 4 15 5 19 20 8 1 20 23 15 18 11"

alphabet_index("The river stole the gods.")
➞ "20 8 5 18 9 22 5 18 19 20 15 12 5 20 8 5 7 15 4 19"

alphabet_index("We have a lot of rain in June.")
➞ "23 5 8 1 22 5 1 12 15 20 15 6 18 1 9 14 9 14 10 21 14 5"

    :return:
    """
    newList=[0 for i in range(oneStr.__len__())]
    temp = ord ('A')
    # print(temp)
    for i in range(oneStr.__len__()):

        if oneStr[i].isupper() or oneStr[i].islower():
            oneStr[i].upper ()

            num = ord(oneStr[i])-temp+1
            # print (num)
            newList[i]=str(num)
        else:
            newList.remove(0)
    newStr=" ".join(newList)
    return newStr
def hh():
    """
     写一个函数keys_and_values，该函数参数是1个字典，
要求该函数返回一个列表，里面包含了2个元素也是列表，分别是 字典里面的key 和对应的 value
比如
keys_and_values({ "a": 1, "b": 2, "c": 3 })
➞ [["a", "b", "c"], [1, 2, 3]]
keys_and_values({ "a": "Apple", "b": "Microsoft", "c": "Google" })
➞ [["a", "b", "c"], ["Apple", "Microsoft", "Google"]]
keys_and_values({ "key1": True, "key2": False, "key3": True })
➞ [["key1", "key2", "key3"], [True, False, True]

    :return:
    """

    if __name__ == '__main__':
    print(alphabet_index('AlphAbet_"'))
    # print (myReplace ("microscopic","i-i"))
    # print(concat2([10, 11, 12, 9, 10],[6, 7, 8, 9, 10],[10, 11, 12]))
    # print (progress_weeks ([10, 11, 12, 9, 10]))
    # print (validate_phone ("12548756987"))
    # print(sumboforei([1, 2, 3, 4]))
    # print(removeDups([1, 2, 3, 4, -5,6,8,9,2,3,4,4]))
    # print(indexOfCaps("shsdfQWRdddssY"))#[5, 6, 7, 13]
    # print(is_valid_PIN("227412"))
    # print(find_odd([1, 2, 3, 4, -5,6,8,9,2,3,4,4]))
    # print(is_symmetrical("ffff"))
    # print (findSmallestNum ([1, 2, 3, 4, -5]))
    # print (ctoa ('1'))
    # print(findLargestNum([1,2,3,4,5]))
    # print(concat([1,2,3,4,5],[1,2,3,4,5]))
    # reverse_anser([1,2,3,4,5])
    # print(tri_area({},4.2))
    # print(remainder(1,3))
    # print(animals(2.5,3,4))