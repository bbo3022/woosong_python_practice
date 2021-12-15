'''
1. readline() 함수 이용하기
    - 첫 번째 줄 읽어 출력
2. readlines함수 사용하기
    -파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
3. read 함수 사용하기
 -파일의 내용 전페를 문자열로 돌려준다.
'''

f1=open('파일생성하기연습.txt','r')
line=f1.readline()
print(line)
f1.close()
print()

f2=open('파일생성하기연습.txt','r')
while True:
	line=f2.readline()
	if not line:break
	print(line,end="")
f2.close