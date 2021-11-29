#나이가 30세 이상인 학생들 리스트

import csv
file=open('./../_dataSet01/StuDataSet02.csv','r')

stu_csv=csv.reader(file)
#list_stu=list(stu_csv)

print(stu_csv)




for idx in stu_csv:

   if int(idx[2][7]) == 1 or int(idx[2][7]) == 2:
      age = 2021 - (1900+int(idx[2][:2]))+1
   else:
      age = 2021 - (2000+int(idx[2][:2]))+1
   if age >= 30:
	   print(idx[1],end='\t')
	   print(age)