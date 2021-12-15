f=open('파일생성하기연습.txt','r')
lines=f.readlines()
print(lines)

for line in lines:
    print(line)
f.close()