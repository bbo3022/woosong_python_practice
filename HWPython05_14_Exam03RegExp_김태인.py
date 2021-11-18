grade=[90, 30, 60, 50, 80]

for idx in range(len(grade)):
	jumsu=grade[idx]

	print(f'{idx+1}번 학생 {jumsu}점 합격' if jumsu >= 60 else f'{idx+1}번 학생 {jumsu}점 불합격')


print('#'*30)
grade=[90, 30, 60, 50, 80]

for idx in range(len(grade)):
	jumsu='합격' if grade[idx]>=60 else '불합격'

	print("%d번 학생 %3d 점 %3s입니다."%(idx+1, grade[idx], jumsu))