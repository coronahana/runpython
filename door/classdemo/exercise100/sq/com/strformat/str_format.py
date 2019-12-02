strtemp = input("请输入学生信息\n")
#strtemp="Jack Green ,21 ; Mike Mos,9;"
if(strtemp.count(";")==2 and strtemp.count(",")==2):
    temp = strtemp.strip().replace(",",":").split(";")
    for stu_info in temp:
        if(stu_info.__contains__(":")):
            stu = stu_info.strip().split(":")
            # print(stu)
            name = stu[0]
            age = str(stu[1])
            print('{:<20}:{:0>2};'.format(name,age))
else:
    print("请重新输入")
