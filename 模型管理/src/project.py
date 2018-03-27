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

if __name__ == '__main__':
    insert_project('模型1')