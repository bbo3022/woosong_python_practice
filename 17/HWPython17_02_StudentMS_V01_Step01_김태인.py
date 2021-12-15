menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;


def stuTitle():
	print("="*90)
	print("{0:^80}".format(">>학생관리시스템v01<<"))
	print("="*90)
	for vMenu in menu:
		print("   ",vMenu, end="")
	print("\n")
	print("="*90)

while True:
	stuTitle()
	print("\n\n")
	num=input("{0:^30}".format("번호입력:"))
	print()
	if num=='1':
		print()
		print("{0:^60}".format("1. 탈퇴학생 Algorithm Chk"))
		print()
	elif num=='2':
		print()
		print("{0:^60}".format("2. 추가등록 Algorithm Chk"))
		print()
	elif num=='3':
		print()
		print("{0:^60}".format("3. 학생목록 Algorithm Chk"))
		print()
	elif num=='4':
		print()
		print("{0:^60}".format("4. 합격생목록 Algorithm Chk"))
		print()
	elif num=='9':
		print()
		print("{0:^60}".format("종료합니다."))
		print()
		break
	else:
		print()
		print("{0:^60}".format("선택지의 숫자를 입력하세요."))
		print()
