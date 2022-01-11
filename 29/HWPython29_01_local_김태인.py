import csv
import time
import datetime
import locale

print(locale.getlocale()) 
# locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
locale.setlocale(locale.LC_ALL,'ko_KR.UTF-8')
print(locale.getlocale())

file=open('./../_dataSet01/emp2.csv','r')

menu=["사번", "입사일", "사원명"]

emp_csv=csv.reader(file)
#print(type(emp_csv))
#print(emp_csv)

for menuList in menu:
	print("  ",menuList, end="		 ")
print("")
print("="*50)

for empList in emp_csv:
	days=datetime.datetime.strptime(empList[4], "%Y-%m-%d")
	#print(type(empList))
	print(empList[0] ,"\t\t",days.strftime(f"%Y.%B-%d"),"\t\t",empList[1])
print("="*50)