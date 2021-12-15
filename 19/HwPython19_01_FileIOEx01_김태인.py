f=open("파일생성하기연습.txt","w")
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()