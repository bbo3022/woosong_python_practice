import csv
file=open('./../_dataSet01/emp2.csv','r')
emp_csv=csv.reader(file)
list_emp=list(emp_csv)


minn=int(input('검색할 연봉 하한값을 입력 하세요:'))
maxx=int(input('검색할 연봉 상한값을 입력하세요:'))

print("")
print('##',minn,'~',maxx,'인 사원 리스트')
print("-"*30)
print('사원명   연봉')
print("-"*30)


for x in range(len( list_emp)):
	if minn <= int(list_emp[x][5]) and int(list_emp[x][5]) <= maxx:
		print(list_emp[x][1], '\t',list_emp[x][5])
	