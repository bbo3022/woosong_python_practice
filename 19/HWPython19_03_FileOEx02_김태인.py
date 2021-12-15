
'''
f=open("foo.txt","w")
f.write("life is too short, you need python")
f.close()

#-------------------------------------------------------

with문을 사용하면 with 블록을 벗어나는 
순간 열린 파일 객체 f가 자동으로 close되어 편리하다.
'''

with open("foo.txt","w") as f:
	f.write("life is too short, you need python")