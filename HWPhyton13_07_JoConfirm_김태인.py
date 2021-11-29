'''
4인 이상의 이름을 입력하세요.(종료:0):오렌지 장미 정직이
^4인 이상 명수를 확인하세요.
4인 이상의 이름을 입력하세요.(종료:0):오렌지 장미 정직이 소나무

split:X명 chk

random.randint()
'''
import random

inputName=input("\t\t>>>>>>>>>> 4인 이상의 이름을 입력하세요(종료:0):")
print("\n")
if len(inputName.split(" "))<4:
	if len(inputName.split(" "))==1:
		if int(inputName)==0:
			print('\t\t종료합니다.')
			exit()
	print("\t\t4인 이상 명수를 확인하세요~\n\n")
	continue

order=[]
while True:
	if len(order)==len(inputName.split(" ")):
		break
	ranNum=random.randint(1,len(inputName.split(" ")))
	if ranNum not in order:
		order.append(ranNum)
	print('\t\t이름=',end='\t')
for inputName in inputName.split(''):
	print(inputName,end="\t")
else:
	print("\n\t\t번호=",end="\t")
for order in order:
	print(order,end="\t")
else:
	print("\n\n")