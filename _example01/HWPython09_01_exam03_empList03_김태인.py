'''
01.파일 오픈_
	_dataset01\emp2.csv
02. read
03. Type Chk
'''

import csv
file=open('./../_dataSet01/emp2.csv','r')

emp_csv=csv.reader(file)
list_emp=list(emp_csv)

emp=str(input('검색할 사원명을 입력하세요:'))

for x in range(len(list_emp)):
	if list_emp[x][1]==emp.upper():
		print(f'{emp.upper()}사원의 연봉은 {list_emp[x][-3]}입니다.')


'''
print("-"*30)
print('사원명   연봉')
print("-"*30)

for empList in emp_csv:

	print(empList[1], '\t',empList[5])
'''