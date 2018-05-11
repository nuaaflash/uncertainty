#!/usr/bin/python
# -*- coding: UTF-8 -*-
import config
import mysql.connector

loginSql = "SELECT c_account, c_password FROM t_user WHERE c_account = %s"

modelSql = "SELECT n_id, c_project, n_pid FROM t_project"

selectProj = "SELECT n_id, c_project, n_pid FROM t_project where c_project = %s"\
             "and n_pid = %s"

insertProj = "insert into t_project(c_project, n_pid, c_descr) values(%s, %s, %s)"

importSql = "insert into t_file(n_project, c_dir, c_filename, b_pyfile) " \
            "values(%s, %s, %s, %s)"
            
exportSql = "SELECT c_dir, c_filename, b_pyfile FROM t_file WHERE n_project = %s"

model_d_Sql = "SELECT arg_name FROM model_arg ORDER BY arg_id"

get_model_Sql = "SELECT m.model_name, a.arg_name, a.dis_type, a.dis_arg FROM model_arg a, model m  WHERE m.model_id = a.model_id AND a.arg_name = "

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

def insertSql(args=(), sql=''):
    db_config = config.datasourse
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except mysql.connector.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
