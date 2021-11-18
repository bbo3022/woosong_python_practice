#1번
a = "Life is too short, you need python"

if "wife" in a: print("wife")  #--1번
elif "python" in a and "you" not in a: print("python")#--2번
elif "shirt" not in a: print("shirt")#--3번
elif "need" in a: print("need")#--4번
else: print("none")#--5번

# 3,4번이 참이지만 3번이 먼저기 때문에 'shirt' 출력
print('='*40)
#2번
#while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

result = 0
i = 1
while i<=1000:
    if i%3==0: 
        result+=i
    i+=1

print(result) 
print('='*40)
#3번
'''
while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

*
**
***
****
*****
'''
i=0
while True:
	i+=1	
	if i>5:
		break
	print(i*'☆')
print('='*40)
#4번
#for문을 사용해 1부터 100까지의 숫자를 출력해 보자.

for result in range(1,101):
	print (result)
print('='*40)
'''
Q5
A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

for문을 사용하여 A 학급의 평균 점수를 구해 보자.
'''
score=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result=0

for whole in score:
	result+=whole

vudrbs=result /len(score)
print(vudrbs)
print('='*40)
'''
Q6
리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.

numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
'''

numbers=[1,2,3,4,5]
result=[n*2 for n in numbers if n%2==1]
print (result)