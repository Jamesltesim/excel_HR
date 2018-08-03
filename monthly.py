# -*-coding:utf-8-*-

standard_morning_time = (9, 0,0)
standard_afternoon_time = (18, 0,0)



# print(dict)

def staff_everyday_record(dict):

    staff_record = []

    date_dict = {}
    for key, value in dict.items():

        # before_work_time = (25, 61, 61)
        # later_work_time = (25, 61, 61)
        staff_dict = {}
        # date_dict[key] = staff_dict
        # # 得到 每个员工 每一天的 打卡记录
        for i, val in enumerate(value):
            # print(i,'->',val)
            staff_id = val[0]
            time = val[1]
            if staff_dict.__contains__(staff_id):
                array = staff_dict[staff_id]
                array.append(time)
            else:
                staff_dict[staff_id] = [time]
            date_dict[key] = staff_dict
    return date_dict



def all_valid_worktime(dict):


    record = staff_everyday_record(dict)

    re = {}
    for key,value in record.items():
        oneday_allstaff_dict = value

        # print(key, '->', value)
        dict = {}
        for k,v in oneday_allstaff_dict.items():
            oneday_onestaff_array = v
            # print(k, '--->', v)

            staff_id = k
            valid_morning_time = (-1, 0, 0)
            valid_afternoon_time = (-1, 0, 0)


            if len(oneday_onestaff_array) > 2:

                tmparray = []
                one = oneday_onestaff_array[0]
                two = oneday_onestaff_array[1]
                tmparray.append((one[3],one[4],one[5]))
                tmparray.append((two[3],two[4],two[5]))

                for i in range(2, len(oneday_onestaff_array)):
                    time = oneday_onestaff_array[i]
                    tmp_time1 = tmparray[0]
                    tmp_time2 = tmparray[1]

                    hour = time[3]
                    minute = time[4]
                    second = time[5]

                    tmp_hour1 = tmp_time1[0]
                    tmp_minute1 = tmp_time1[1]
                    tmp_second1 = tmp_time1[2]
                    tmp_hour2 = tmp_time2[0]
                    tmp_minute2 = tmp_time2[1]
                    tmp_second2 = tmp_time2[2]

                    number1 = hour*60*60 + minute*60 + second*60
                    number2 = tmp_hour1 * 60 * 60 + tmp_minute1 * 60 + tmp_second1 * 60
                    number3 = tmp_hour2 * 60 * 60 + tmp_minute2 * 60 + tmp_second2 * 60

                    if number1 < number2:
                        tmparray[0] = (hour,minute,second)

                    if number1 > number3:
                        tmparray[1] = (hour,minute,second)

                valid_morning_time = tmparray[0]
                valid_afternoon_time=tmparray[1]

            elif len(oneday_onestaff_array) == 2:
                tmparray = []
                one = oneday_onestaff_array[0]
                two = oneday_onestaff_array[1]
                tmparray.append((one[3], one[4], one[5]))
                tmparray.append((two[3], two[4], two[5]))

                tmp_time1 = tmparray[0]
                tmp_time2 = tmparray[1]

                tmp_hour1 = tmp_time1[0]
                tmp_minute1 = tmp_time1[1]
                tmp_second1 = tmp_time1[2]
                tmp_hour2 = tmp_time2[0]
                tmp_minute2 = tmp_time2[1]
                tmp_second2 = tmp_time2[2]

                number2 = tmp_hour1 * 60 * 60 + tmp_minute1 * 60 + tmp_second1 * 60
                number3 = tmp_hour2 * 60 * 60 + tmp_minute2 * 60 + tmp_second2 * 60

                if number2 > number3:
                    valid_morning_time = tmp_time2
                    valid_afternoon_time = tmp_time1
                else:
                    valid_morning_time = tmp_time1
                    valid_afternoon_time = tmp_time2


            elif len(oneday_onestaff_array) == 1:
                time = oneday_onestaff_array[0]
                valid_morning_time = (time[3],time[4],time[5])
            elif len(oneday_onestaff_array) == 0:
                pass

            dict[staff_id] = [valid_morning_time,valid_afternoon_time]
        re[key]=dict
    return re



