#연습1
score=[80,75,55]
totalSc=0
subject=(len(score))
for total in score:
	totalSc+=total
average=totalSc/subject
print("홍길동의 평균점수는",average,"입니다.")


print()
print()
print('='*50)


#연습3
hong="881120-1068234"
vhong=hong.split("-")

print("홍길동의 생년월일은",vhong[0],"입니다")
if vhong[1][0]=='1' or vhong[1][0]=='3':
	print("홍길동은 남성입니다.")
elif vhong[1][0]=='2' or vhong[1][0]=='4':
	print("홍길동은 여성입니다.")

print()
print()
print('='*50)

#연습2
while True:
	num=int(input("확인하고자 하는 숫자를 입력하세요:"))
	if num%2==1:
		print("홀수 입니다.")
	else:
		print("짝수 입니다.")


print()
print()
print('='*50)

