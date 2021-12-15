try:
	print(100/0)

#	f1=open('파습.txt','r')
#	f1.close()

#	X="안녕하세요"
#	print(x)

#	x=10
#	print(x+"띠용")


#	thisdict = {
#	  "brand": "Ford",
#	  "model": "Mustang",
#	  "year": 1964
#	}
#	x = thisdict["color"]
#	print(x)

#	a=[1,2,3,4,5]
#	print(a[5])



#except ZeroDivisionError:
	print("ZeroDivisionError 발생 확인")
except FileNotFoundError:
	print("FileNotFoundError 발생 확인")
except NameError:
	print("NameError 발생 확인")
except TypeError:
	print("Type Error 발생 확인")
except KeyError:
	print("Type Error 발생 확인")
except IndexError:
	print("Index Error 발생 확인")
except:
	print("확인되지 않은 에러 발생 확인")