"""
OS : 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈

함수	설명
os.mkdir(디렉터리)	디렉터리를 생성한다.
os.rmdir(디렉터리)	디렉터리를 삭제한다.단, 디렉터리가 비어있어야 삭제가 가능하다.
os.unlink(파일)	파일을 지운다.
os.rename(src, dst)	src라는 이름의 파일을 dst라는 이름으로 바꾼다.

"""



import  os
'''
print(os.getcwd()) 자신의 디렉터리 위치를 돌려준다.
os.chdir("./../../") 자신의 디렉터리 위치를 돌려준다.
print(os.getcwd())
'''
os.system("dir")
f = os.popen("dir")
# print(f.read())
# os.mkdir("새파일")
# os.rmdir("새파일")
# os.unlink("222.txt")
os.rename("test.txt","after.txt")