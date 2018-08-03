# -*-coding:utf-8-*-


# 按照日期排列

def date(list):
    dict = {}

    for tmp in list:
        if len(tmp) != 2:
            continue

        staff_id = tmp[0]
        date = tmp[1]

        key = (date[0],date[1],date[2])
        if dict.__contains__(key):
            array = dict[key]
            array.append(tmp)
        else:
            dict[key] = [tmp]

    return dict


# 按照员工排列
def staff(list):
    dict = {}

    for tmp in list:
        if len(tmp) != 2:
            continue

        staff_id = tmp[0]
        date = tmp[1]

        if dict.__contains__(staff_id):

            array = dict[staff_id]
            array.append(date)

        else:

            dict[staff_id] = [date]

    return dict




