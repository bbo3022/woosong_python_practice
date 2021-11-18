grade=[90,30,60,50,80]

hap="합격"
for idx in range(len(grade)):
	if grade[idx] < 60:
		continue
	print("%d번 학생 %2d점 %3s 입니다."%(idx+1, grade[idx], hap))