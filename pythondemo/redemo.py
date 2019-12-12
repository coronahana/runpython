import re
res1 = re.findall('s*','songsin')#找出所有符合条件的内容--返回是一个列表
res2 = re.findall('s.','songsin')
res3 = re.findall('s+','songsin')
res4= re.findall('.\w','songq-n')
res5 = re.findall('.\W','songq-n')
res6 = re.findall('\d{6}','abcded123456xyz789')
res7 = re.findall('s.','songqinST',re.I)
print(f'res1={res1}')
print(f'res2={res2}')
print(f'res3={res3}')
print(f'res4={res4}')
print(f'res5={res5}')
print(f'res6={res6}')
print(f'res7={res7}')
"""
res1=['s', '', '', '', 's', '', '', '']
res2=['so', 'si']
res3=['s', 's']
res4=['so', 'ng', '-n']
res5=['q-']
res6=['123456']
res7=['so', 'ST']
"""

print(re.S)
re.findall('<span class="td">共(.+?)页，到第</span>',reps.text,re.S)