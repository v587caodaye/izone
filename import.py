#!/usr/bin/python
#encoding:utf-8
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DevOps.settings")# project_name 项目名称
django.setup()

import sys,pymysql
import xlrd,datetime,time
from datetime import date,datetime,timedelta
from xlrd import xldate_as_tuple
from Precord.models import *
from users.models import User
#data_list=[]
#data_list.extend(table.row_values(0))
#for item in data_list:
#  print(item)
data=xlrd.open_workbook(sys.argv[1])
for num in range(data.nsheets):
  table=data.sheet_by_index(num)
  if table.ncols >15:
    for rownum in range(table.nrows):
      if rownum < 2: continue
      x=table.row_values(rownum)
#      Error_Type.objects.get_or_create(type=x[5])
#      Classification_FIRST.objects.get_or_create(type=x[7])
      id_support_object=PersonInfo.objects.get(YU_NAME="cWX331849").id
      id_department_five=PersonInfo.objects.get(YU_NAME="cWX331849").department_five_id
      id_department_six=PersonInfo.objects.get(YU_NAME="cWX331849").department_six_id
#      id_department_five=Department_FIVE.objects.get(department_five="test").id
#      id_department_six=Department_SIX.objects.get(department_six="test").id
      id_type=Error_Type.objects.get(type=x[5]).id
#      id_classification_first=Classification_FIRST.objects.get(type=x[7]).id
#      id_classification_two=Classification_TWO.objects.get(type=x[8]).id
      id_classification_first=Classification_FIRST.objects.get(type='其他').id
      id_classification_two=Classification_TWO.objects.get(type='其他').id
      id_author=User.objects.get(name=x[11]).id
      record_date=datetime(*xldate_as_tuple(x[1],0)).strftime('%Y-%m-%d')
#     Classification_TWO.objects.get_or_create(type=x[8],classification_first_id=id_classification_first)
      RecordOfSupportproblem.objects.get_or_create(record_date=record_date,support_object_id=id_support_object,department_five_id=id_department_five,department_six_id=id_department_six,type_id=id_type,description=x[6],classification_first_id=id_classification_first,classification_two_id=id_classification_two,cause_or_solution=x[9],version_id=4,author_id=id_author,blocking_time_id=1,positioning_time_id=1,is_Closed=True,Failed_link=x[15])
  

#try:
#  con=pymysql.connect('localhost','root','root','DevOps')
#  print('OOK')
#  cur=con.cursor()
#  data=xlrd.open_workbook('test.xlsx')
#  table=data.sheet_by_name(u'personinfo')
#  for rownum in range(table.nrows):
#    x=table.row_values(rownum)
#    exec_cmd="""insert into DevOps_personinfo(FULL_NAME,YU_NAME,DEPARTMENT_MIN_id) values('%s','%s','%d');"""%(x[0],x[1],int(x[2]))
#    try:
#      cur.execute(exec_cmd)
#      con.commit()
#    except:
#      con.rollback()
#  cur.close()
#  con.close()
#except:
#  print("mysql Error")
