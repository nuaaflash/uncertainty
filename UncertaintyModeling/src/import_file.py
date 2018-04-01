#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector
from mysql.connector import Error
import config
import os

def read_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data
 
def insert_blob(project, _dir):
    
#     _dir = unicode(_dir,"utf-8")

    query = "insert into t_file(c_project, c_dir, c_filename, b_pyfile) " \
            "values(%s, %s, %s, %s)"
 
    db_config = config.datasourse
 
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        for (root, dirs, files) in os.walk(_dir):
            for _file in files:
                absPath = os.path.join(root, _file)
                relDir = root.split(_dir, 1)[1]
                data = read_file(absPath)
                args = (project, relDir, _file, data)
                cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    insert_blob(project='test', _dir =r"E:\MyEclipse 2015 CI\test\src\model")

# try:
#     cnn = mysql.connector.connect(**conconf# except mysql.connector.Error as e:
#     print('connect fails!{}'.format(e))
#   
#       
# cursor = cnn.cursor()
# try:
#     sql_query = 'select c_id, c_name, c_filename from model ;'
#     cursor.execute(sql_query)
#     for id, name, filename in cursor:
#         print (id, name, filename)
# except mysql.connector.Error as e:
#     print('query error!{}'.format(e))
# finally:
#     cursor.close()
#     cnn.close()