#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import imp
import mysql.connector
from mysql.connector import Error
import config

def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
        
        
def read_blob(project, filename):
    # select photo column of a specific author
    query = "SELECT c_dir, c_filename, b_pyfile FROM t_file WHERE c_project = %s"
 
    # read database configuration
    db_config = config.datasourse
 
    try:
        # query blob data form the authors table
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, (project,))
        for c_dir, c_filename, b_pyfile in cursor.fetchall():
            _dir = os.path.join(os.getcwd(), project)
            _dir = _dir + c_dir.encode("utf-8")
            _dir = unicode(_dir, "utf-8")
            if not(os.path.exists(_dir)):
                os.makedirs(_dir)
            path = _dir + "\\" + c_filename.encode("utf-8")
            write_file(b_pyfile, path)
        # write blob data into a file
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
        
def run():
    sys.path.append(r"E:\MyEclipse 2015 CI\test\src\test")
    print sys.path
#     kNN=imp.load_source('kNN', 'E:\MyEclipse 2015 CI\test\src\一元非线性回归\test.py')
    filename = "test1"
    method = "function"
    variable = [1,2,3]

    obj = __import__(filename) # import module
    c = getattr(obj,method)
    print c(x = variable) # call def

def init_param():
    db_config = config.datasourse
    query = "insert into t_param_model(c_project, c_description, c_modeltype) " \
            "values(%s, %s, %s)"
    sys.path.append(r"E:\MyEclipse 2015 CI\test\src\test")
    print sys.path
#     kNN=imp.load_source('kNN', 'E:\MyEclipse 2015 CI\test\src\一元非线性回归\test.py')
    filename = "test1"
    method = "description"
    variable = [1,2,3]

    obj = __import__(filename) # import module
    c = getattr(obj, method)
    c = getattr(c, method)
    params = c()
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        for param in params:
            cursor.execute(query, ("test", param, "1"))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
            

 
if __name__ == '__main__':
    read_blob("test","test1.py")
    init_param()
    run()
