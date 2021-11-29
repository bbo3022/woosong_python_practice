import csv
file=open('./../_dataSet01/emp2.csv','r')
emp_csv=list(csv.reader(file))


job=input('검색할 직업을 입력하세요:')
splitSearchjob=job.split(",")

print("")
print('#직업이',job,'인 직원 리스트')
print("-"*30)
print('사원명','\t','직업','\t\t','급여')
print("-"*30)

for OuterEmpList in emp_csv:
	for InnerEMpList in splitSearchjob:
		if OuterEmpList[2]==InnerEMpList.strip().upper():
			print(f'{OuterEmpList[1]:<10}{OuterEmpList[2]:<10}{OuterEmpList[5]:<10}')