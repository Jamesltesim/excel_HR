# -*-coding:utf-8-*-


def read(xlsx_name):

    import xlrd
    from xlrd import xldate_as_tuple

    # xlsx 表格式

    # 打开文件
    data = xlrd.open_workbook(xlsx_name)
    # 打开工作表
    # table = data.sheets()[0]
    table = data.sheets()[1]
    # 获得所有行数
    nrows = table.nrows



    nrows = table.nrows
    ncols = table.ncols

    record = []
    for i in range(nrows):
        # 每一条打卡记录的list
        list = table.row_values(i)

        rowlist = []
        for i, val in enumerate(list):
            # 如果val为float 表示是打卡数据 否则是 标题
            if isinstance(val, float):

                #i==0 表示 读取的字段是 员工id
                if i == 0:
                    rowlist.append(int(val))
                # i==1 表示 读取的字段是 员工打卡日期
                elif i==1:
                    rowlist.append(xldate_as_tuple(val, 0))
            # else:
            #     rowlist.append(val)

        if len(rowlist) != 0:
            record.append(rowlist)
    return record



# 写到excel path为位置以及 名字
def write(path_name):

    import xlwt
    # 新建一个excel文件
    file = xlwt.Workbook()
    # 新建一个sheet
    table = file.add_sheet('info', cell_overwrite_ok=True)
    # 写入数据table.write(行,列,value)
    table.write(0, 0, 'wangpeng')
    # 保存文件
    # file.save('file.xls')
    file.save(path_name)