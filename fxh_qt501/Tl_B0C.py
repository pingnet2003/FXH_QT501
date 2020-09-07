# -*- coding:utf-8 -*-
import cx_Oracle    #pip3 install cx_Oracle
import pandas as pd
import os

os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'
# os.environ['TNS_ADMIN'] = 'D:\program\instantclientx64_jb51\instantclient_11_2'
# os.environ['Path'] = 'D:\program\instantclientx64_jb51\instantclient_11_2'

host = "127.0.0.1"   #数据库ip
port = "1521"        #端口
sid = "orcl"         #数据库名称
dsn = cx_Oracle.makedsn(host, port, sid)

# scott是数据用户名，tiger是登录密码（默认用户名和密码）
conn = cx_Oracle.connect("scott", "tiger", dsn)

# 以普通方式读取 结果
# cursor = conn.cursor()
# cursor.execute('select sysdate from dual')
# cursor.close()

# 以 panda 方式读取 结果集
sql='select * from employee'
data_df=pd.read_sql(sql,conn)

conn.close()
print(data_df.info())
