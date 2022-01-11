"""
shutil은 파일을 복사해 주는 파이썬 모듈이다.

다음 예시는 src라는 이름의 파일을 dst로 복사한다. 만약 dst가 디렉터리 이름이라면 src라는 파일 이름으로 dst 디렉터리에 복사하고 동일한 파일 이름이 있을 경우에는 덮어쓴다.

"""



import  shutil
shutil.copy("original.txt","original-2.txt")
