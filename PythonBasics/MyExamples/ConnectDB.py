#!/usr/bin/env python3
import os
import cx_Oracle
import sys
import traceback

os.environ["PATH"] = os.environ["PATH"] + ";E:\OracleClient\instantclient_18_5"

def open_conn():
    try:
        dbname='orcl'
        dbconn = cx_Oracle.connect('sys/Welcome1@localhost:1521/'+dbname,mode=cx_Oracle.SYSDBA)
        print("Connection Done")
        print("DB Version: {}".format(dbconn.version))
        return dbconn
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        traceback.print_exc()
        exit(1)

def close_conn(dbconn):
    try:
        dbconn.close()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        traceback.print_exc()
        exit(1)

def cursor_cmd(dbconn,cmd):
    try:
        cursor=db.cursor()
        cursor.execute(cmd)
        return cursor
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        traceback.print_exc()
        exit(1)

if __name__=='__main__':
    cmd = 'select instance_name, version, status, con_id from v$instance'
    db = open_conn()
    cursor = cursor_cmd(db,cmd)
    for result in cursor:
        print(result)
    close_conn(db)
