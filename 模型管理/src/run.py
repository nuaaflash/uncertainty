#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector
from mysql.connector import Error
import config

def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
        
        
def read_blob(project, filename):
    # select photo column of a specific author
    query = "SELECT c_path, b_pyfile FROM t_file WHERE c_project = %s"
 
    # read database configuration
    db_config = config.datasourse
 
    try:
        # query blob data form the authors table
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, (project,))
        result = cursor.fetchone()
        print result[0]
        # write blob data into a file
        write_file(result[1], filename)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
        
def run():
    filename = "test2"
    method = "function"
    variable = [1,2,3]

    obj = __import__(filename) # import module
    c = getattr(obj,method)
    print c(x = variable) # call def

 
if __name__ == '__main__':
    read_blob("一元非线性回归","test2.py")
    run()
