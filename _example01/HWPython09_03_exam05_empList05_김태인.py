import csv
file=open('./../_dataSet01/emp2.csv','r')
emp_csv=csv.reader(file)
list_emp=list(emp_csv)

print('사원 중 보너스가 0이 아닌 사원 리스트 출력')

print("")
print('##보너스 확인')
print("-"*30)
print('사원명','\t','보너스')
print("-"*30)


for x in range(len( list_emp)):
	if int(list_emp[x][2][:2])!=0:
		print(list_emp[x][1], '\t',list_emp[x][6])
