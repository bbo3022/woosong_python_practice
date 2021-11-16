vId = 'Orange'
vPwd = '1234'

Id = input("Id를 입력하세요 : ")
Pwd = input("Pwd를 입력하세요 : ")

if Id  == vId and Pwd == vPwd:
		print("Orange님 로그인 성공")
elif Pwd != vPwd and Id == vId:
		print("패스워드를 확인하세요")
elif Id != vId and Pwd == vPwd:
		print("Id를 확인하세요")
