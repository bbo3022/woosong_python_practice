vId = 'Orange'
vPwd = '1234'

Id = input("Id를 입력하세요 : ")
Pwd = input("Pwd를 입력하세요 : ")

if Id  == vId:
	if Pwd == vPwd:
		print("Orange님 로그인 성공")
	elif Pwd != vPwd:
		print("패스워드를 확인하세요")

elif Id != vId:
	if Pwd != vPwd:
		print("Id를 확인하세요")
