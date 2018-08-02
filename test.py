# -*-coding:utf-8-*-

import excel
import according


list = excel.read('aaa.xlsx')

print(according.date(list))

# excel.write('../bb.xlsx')
