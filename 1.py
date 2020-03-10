# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/02/21 08:53:43
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
tup = (91,92,93,94,100)
# print(max(tup))

dict1 ={'学号':'0133','姓名':'hz','班级':'1801','年龄':18}
dict1['年龄']=23
dict1['身高']=173
del dict1['身高']
print("dict1 :",dict1)
print(dict1['年龄'])


