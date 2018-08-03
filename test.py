# -*-coding:utf-8-*-

import excel
import according
import monthly


list = excel.read('aaa.xlsx')


dict =according.date(list)


# 得到每一天所有员工 早上第一次和晚上最后一次的打卡记录
print(monthly.all_valid_worktime(dict))
