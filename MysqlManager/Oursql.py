#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector
from mysql.connector import Error
import config


def insert_project(project):
    query = "insert into t_project(c_project) values(%s)"

    args = (project,)

    db_config = config.datasourse

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# 在表目录中加入 新建的抽样结果表
def insert_sr_result_table(tablename = "sampling_result"):
    query = "insert into Contents_Of_Sampling_Result(tablename) values("+ tablename +")"
    print("这里是" + query)

    db_config = config.datasourse

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# 默认存到sampling_result 数据库
# 如果传进参数 将按照 抽样方法 加 下划线 加 分布类型的模式命名表
def insert_sampling_result(result=[],type = "",method = "sampling_result", name_by_type = 0):
    line = ""  # 默认没有下划线
    if (name_by_type != 0):  # 如果分布类型不是默认值 说明要按命名方式加入下划线,则 下划线为"_"
        line = "_"

    # 组成表名 默认会组成 sampling_result
    tablename = method + line + type

    if (IsTheTableInTheDB(tablename) == False):
        # 表不存在创建表 并加入表索引
        create_table_for_sampling_result(tablename)
        insert_sr_result_table(tablename)

    result = list(result)
    id = 1
    for i in result:
        query = "insert into "+ tablename +"(result_value,result_id,sampling_method,distribution_type) values(%s,%s,%s,%s)"

        args = (float(i),id,method,type)
        id = id + 1
        db_config = config.datasourse

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

# 展示sampling_result 数据库
# 如果传进参数 将按照 抽样方法 加 下划线 加 分布类型的模式命名表
def show_sampling_result(showset = "0", distribution_type = "", sampling_method = "sampling_result"):
    line = ""  # 默认没有下划线
    if (showset != 0):  # 显示设置 不是默认值 0 说明要按命名方式加入下划线,则 下划线为"_"
        line = "_"

    # 组成表名 默认会组成 sampling_result
    tablename = sampling_method + line + distribution_type

    if (IsTheTableInTheDB(tablename)):
        # 表存在才查找返回表信息
        query = "select * from " + tablename + " order by result_id"
        print(query)
        try:
            db_config = config.datasourse
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute(query)
            # 获取所有记录列表
            results = cursor.fetchall()
            return results

        except Error as e:
            print(e)
        cursor.close()
        conn.close()

# 命名方式同上
def clear_sampling_result( type = "",method = "sampling_result",name_by_type = 0):
    line = ""  # 默认没有下划线
    if (name_by_type != 0):  # name_by_type 不是默认值 说明要按命名方式加入下划线,则 下划线为"_"
        line = "_"

    # 组成表名 默认会组成 sampling_result
    tablename = method + line + type

    print("这里是"+tablename)

    if (IsTheTableInTheDB(tablename) == True):
        # 表存在 再清除数据

        query = "delete from  " + tablename
        print("这里是" + query)
        db_config = config.datasourse

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

# 查看表是否存在于数据库中
def IsTheTableInTheDB(tablename = "sampling_result"):
    # 从数据库work中查找表名为tablename的表
    query = "SELECT table_name FROM information_schema.TABLES WHERE table_schema = 'work' and table_name ='"+ tablename +"';"
    print("这里是" + query)
    try:
        db_config = config.datasourse
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        if(len(results) != 0):# 如果有结果返回True
            return True
        else:             # 否则返回False
            return False

    except Error as e:
        print(e)
    cursor.close()
    conn.close()

# 根据表名创建抽样结果表
def create_table_for_sampling_result(tablename="samplingresult"):
    # 根据表名创建存储抽样结果的数据库表
    query = "CREATE TABLE `"+ tablename +"`  (`result_id` int(11) NOT NULL AUTO_INCREMENT,`result_value` float(9, 3) NOT NULL,`sampling_method` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,`distribution_type` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,PRIMARY KEY (`result_id`) USING BTREE) ENGINE = MyISAM AUTO_INCREMENT = 939 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;"
    try:
        db_config = config.datasourse
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query)
    except Error as e:
        print(e)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_table_for_sampling_result("test_ADD")
    if(IsTheTableInTheDB("test_ADD")):
        print("test_ADD is in the DB")
    if(IsTheTableInTheDB("test_not_in") == False):
        print("test_not_in is not in the DB")

    list = 1,3,5,7,9
    insert_sampling_result(list,"sometype", "somemethod", 1)