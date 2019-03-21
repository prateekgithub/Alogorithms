#!/usr/bin/env python3
import os
import cx_Oracle

os.environ["PATH"] = os.environ["PATH"] + ":/Users/pppande/Downloads/instantclient_12_1/:/Users/pppande/Downloads/instantclient_18_1/"

connection = cx_Oracle.connect('sys/welcome1@slcs03adm03.usdv1.oraclecorp.com:3040/cdbae1 as sysdba')
sqlquery = "select INSTANCE_ROLE from v$instance;"
print("Connection Done")
print("DB Version: {}".format(connection.version))
