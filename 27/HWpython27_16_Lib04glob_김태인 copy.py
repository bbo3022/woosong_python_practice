"""
glob(pathname) - 디렉터리에 있는 파일들을 리스트로 만들기
  가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다. 이럴 때 사용하는 모듈이 바로 glob이다.
    wildcard 사용가능 >>OS기준
    -*:임의 모든 문자
    -?:1개 문자
"""

import  glob
# result=glob.glob("*")
# print(type(result))
# print(len(result))
# print(result)

imgList=glob.glob("imgV02/*")
for x in imgList:
  print(x)