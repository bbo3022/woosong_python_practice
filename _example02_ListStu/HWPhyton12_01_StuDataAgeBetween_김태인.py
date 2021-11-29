import csv
file=open('./../_dataSet01/StuDataSet02.csv','r')

stu_csv=csv.reader(file)

while True:
	minn=int(input('검색할 연령 하한값을 입력 하세요:'))
	maxx=int(input('검색할 연령 상한값을 입력하세요:'))
	if minn < maxx:
		break
	print('다시 입력하세요!~')

print("")
print('##',minn,'~',maxx,'인 학생 리스트')
print("-"*50)
print('이름','\t','나이','\t','통신사','   ','전화번호')
print("-"*50)

for idx in stu_csv:
	if int(idx[2][7]) == 1 or int(idx[2][7]) == 2:
		age = 2022 - (1900+int(idx[2][:2]))
	else:
		age = 2022 - (2000+int(idx[2][:2]))
	if int(age) >= minn and int(age) <= maxx:
		print(idx[1],'\t',age,'\t',idx[4],'\t',idx[3])
print("-"*50)