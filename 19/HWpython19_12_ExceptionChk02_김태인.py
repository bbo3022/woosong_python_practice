#ZeroDivisionError
try:
	print(100/0)
except:
	print("ZeroDivisionError 발생 확인")

#FileNotFoundError
try:
	f1=open('파습.txt','r')
	line=f1.readline()
	print(line)
	f1.close()
except:
	print("FileNotFoundError 발생 확인")

#NameError
try:
	X="안녕하세요"
	print(x)
except:
	print("NameError 발생 확인")

#Type Error
try:
	x=10
	print(x+"띠용")
except:
	print("Type Error 발생 확인")

#Key Error
try:
	thisdict = {
	  "brand": "Ford",
	  "model": "Mustang",
	  "year": 1964
	}
	x = thisdict["color"]
	print(x)
except:
	print("Type Error 발생 확인")

#Index Error
try:
	a=[1,2,3,4,5]
	print(a[5])
except:
	print("Index Error 발생 확인")