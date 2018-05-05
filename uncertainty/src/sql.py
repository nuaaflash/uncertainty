#!/usr/bin/python
# -*- coding: UTF-8 -*-
import config
import mysql.connector

def selectSql(args=(), sql=''):
    db_config = config.datasourse
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        record = cursor.fetchall()
    except mysql.connector.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return record

loginSql = "SELECT c_account, c_password FROM t_user WHERE c_account = %s"

modelSql = "SELECT n_id, c_project, n_pid FROM t_project"