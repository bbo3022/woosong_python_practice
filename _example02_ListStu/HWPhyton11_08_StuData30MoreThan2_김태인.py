#나이가 30세 이상이고 통신사sk인 학생들 리스트

import csv
file=open('./../_dataSet01/StuDataSet02.csv','r')

stu_csv=csv.reader(file)
#list_stu=list(stu_csv)

print(stu_csv)

print('='*50)
print('이름','\t','나이','\t','통신사','  ','전화번호')
print('='*50)

for idx in stu_csv:
   if int(idx[2][7]) == 1 or int(idx[2][7]) == 2:
      age = 2022 - (1900+int(idx[2][:2]))
   else:
      age = 2022 - (2000+int(idx[2][:2]))
   if age >= 30 and str(idx[4].strip())=='sk':
		   print(idx[1],'\t', age,'\t', idx[4],'\t', idx[3])
	 