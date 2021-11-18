'''
문제]
-총 [5명]의 학생이 시험을 보았는데
-시험 점수가 60점이 넘으면 합격이고
-그렇지 않으면 불합격이다. 

-print("%d번 학생 %3d 점 %3s 입니다."%(_,_,_)) 적용

Data] grade=[90, 30, 60, 50, 80]

sample Run]
1번 학생 90점 합  격 입니다.
2번 학생 30점 불합격 입니다.
3번 학생 60점 합  격 입니다.
4번 학생 50점 불합격 입니다. 
5번 학생 80점 합  격 입니다.
'''
grade = [90, 30, 60, 50, 80]

for idx in range(len(grade)): #range(5)>>01234
	if (grade[idx]>=60):
		print("%d번 학생 %2d점 %3s 입니다."%(idx+1, grade[idx], "합  격"))
	else:
		print("%d번 학생 %2d점 %3s 입니다."%(idx+1, grade[idx], "불합격"))

#idx 0부터 시작. 그래서 +1 해줌.

print('#'*30)

for idx in range(len(grade)):
	if (grade[idx]>=60):
		hap='합격
	else:
		hap='불합격'
	print("%d번 학생 %2d점 %3s 입니다."%(idx+1, grade[idx], hap))
