#!/usr/bin/python
#encoding:utf-8
import sys,pymysql
con=pymysql.connect('localhost','root','root','test')
cur=con.cursor()
cur.execute('select * from DevOps_classification_one;')
R=cur.fetchall()[0]
print(R)
