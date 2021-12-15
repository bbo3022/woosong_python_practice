#1번 .주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
'''
def is_odd():
	num=int(input("자연수를 입력하세요:"))
	if num%2==0:
		print('짝수 입니다.')
	elif num%2==1:
		print('홀수입니다.')
while True:
	is_odd()
'''

#2번. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자
'''
def mAvg(*args):
	result=0
	for i in args:
		print(i, end="  ")
		result=result+i
	return result/len(args)

result1=mAvg(70,80,90,100)
print("=>평균은 %d 입니다."%result1)
'''

#3번. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자
'''
num1=int(input("첫번째 숫자를 입력하세요:"))
num2=int(input("두번째 숫자를 입력하세요:"))
total = num1 + num2
print("두 수의 합은 %s 입니다" % total)
'''

#4.다음 중 출력 결과가 다른 것 한 개를 골라 보자.
'''
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")#쉼표는 띄어쓰기로 출력
print("".join(["you", "need", "python"]))
'''

#5. 
'''
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
'''

#6.사용자의 입력을 파일(test1.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
'''
while True:
	text=input("내용을 입력하세요:")
	f1 = open("test1.txt", 'a')
	f1.write(text)
	f1.write("\n")
	f1.close()
'''

#7. 다음과 같은 내용을 지닌 파일 test2.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
'''
f=open('test2.txt','r')
data=f.read()
print(data)
print("-"*30)
Ndata = data.replace("java", "python")
print(Ndata)
f.close()
'''