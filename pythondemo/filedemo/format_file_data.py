"""
现有文件1（如下，请保存到文件file1.txt中）， 记录了公司员工的薪资，其内容格式如下

name: Jack   ;    salary:  12000
 name :Mike ; salary:  12300
name: Luk ;   salary:  10030
  name :Tim ;  salary:   9000
name: John ;    salary:  12000
name: Lisa ;    salary:   11000

每个员工一行，记录了员工的姓名和薪资，
每行记录 原始文件中并不对齐，中间有或多或少的空格

现要求实现一个python程序，计算出所有员工的税后工资（薪资的90%）和扣税明细，
以如下格式存入新的文件 file2.txt中，如下所示

name: Jack   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Mike   ;    salary:  12300 ;  tax: 1230 ; income:  11070
name: Luk    ;    salary:  10030 ;  tax: 1003 ; income:   9027
name: Tim    ;    salary:   9000 ;  tax:  900 ; income:   8100
name: John   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Lisa   ;    salary:  11000 ;  tax: 1100 ; income:   9900

要求像上面一样的对齐
tax 表示扣税金额和 income表示实际收入。注意扣税金额和 实际收入要取整数
"""


'''
mind:
1、读取文件内容
2、读取每行数据
    计算出 税金
    计算出实收
    组装好每条数据，并存入文件

    
'''
def format_file_data(file_r):
    file_r = open (file_r, "r")
    file_w = open ("file2.txt", "w+")
    lines = file_r.readlines ()
    # print (lines)
    for linedata in lines:
        # print(linedata)
        linelist = linedata.replace("\n", " ").strip().split(";")
        name_str = (linelist[0]).strip ().ljust (10)
        salary_str = "\tsalary:\t" + str ((((linelist[-1]).split(":"))[-1])).rjust (10)
        income = int ((((linelist[-1]).split (":"))[-1])) * 0.9
        tax = int (((linelist[-1]).split (":"))[-1]) * 0.1
        income_str = ";\tincome:\t" + str (int (income)).rjust (10)
        tax_str = "\t;\ttax:\t" + str (int (tax)).rjust (10)
        newlinedata = name_str + salary_str + tax_str + income_str
        file_w.write (newlinedata + "\n")
        print(newlinedata)
    file_r.close ()
    file_w.close ()
    return  file_w

format_file_data("file1.txt")
"""

name: Jack	salary:	     12000	;	tax:	      1200;	income:	     10800
name :Mike	salary:	     12300	;	tax:	      1230;	income:	     11070
name: Luk 	salary:	     10030	;	tax:	      1003;	income:	      9027
name :Tim 	salary:	      9000	;	tax:	       900;	income:	      8100
name: John	salary:	     12000	;	tax:	      1200;	income:	     10800
name: Lisa	salary:	     11000	;	tax:	      1100;	income:	      9900
"""
