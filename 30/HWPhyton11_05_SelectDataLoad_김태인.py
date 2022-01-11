import csv
file=open('./../_dataSet01/StuDataSet02.csv','r')

stu_csv=csv.reader(file)
# list_stu=list(emp_csv)
print(stu_csv)

for x in stu_csv:
	print(x)