"""
tempfile
파일을 임시로 만들어서 사용할 때 유용한 모듈이 바로 tempfile이다. tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.

import  tempfile

filename=tempfile.mkstemp()
print(filename)

calendar
calendar는 파이썬에서 달력을 볼 수 있게 해주는 모듈이다.
calendar 모듈의 또 다른 유용한 함수를 보자. weekday(연도, 월, 일) 함수는 그 날짜에 해당하는 요일 정보를 돌려준다. 월요일은 0, 화요일은 1, 수요일은 2, 목요일은 3, 금요일은 4, 토요일은 5, 일요일은 6이라는 값을 돌려준다.
"""

import calendar

# calendar.prcal(2022)
# calendar.prmonth(2022,4)
#print(calendar.weekday(2022,1,4))
# print(calendar.monthrange(2022,1))
# a=int(input("년도를 입력 하세요(ex2022):"))
# b=int(input("월을 입력 하세요(ex1):"))
# c=int(input("일을 입력 하세요(ex4):"))

# if calendar.weekday(a,b,c) == 0:
#   print(f"{a}년 {b}월 {c}일은 월요일")
# elif calendar.weekday(a,b,c) == 1:
#   print(f"{a}년 {b}월 {c}일은 화요일")
# elif calendar.weekday(a,b,c) == 2:
#   print(f"{a}년 {b}월 {c}일은 수요일")
# elif calendar.weekday(a,b,c) == 3:
#   print(f"{a}년 {b}월 {c}일은 목요일")
# elif calendar.weekday(a,b,c) == 4:
#   print(f"{a}년 {b}월 {c}일은 금요일")
# elif calendar.weekday(a,b,c) == 5:
#   print(f"{a}년 {b}월 {c}일은 토요일")
# elif calendar.weekday(a,b,c) == 6:
#   print(f"{a}년 {b}월 {c}일은 일요일")


# if calendar.weekday(int(a[0]),int(a[1]),int(a[2])) == 0:
#   print(f"{a}은 월요일")
# elif calendar.weekday(int(a[0]),int(a[1]),int(a[2])) == 1:
#   print(f"{a}은 화요일")
# elif calendar.weekday(int(a[0]),int(a[1]),int(a[2])) == 2:
#   print(f"{a}은 수요일")
# elif calendar.weekday(int(a[0]),int(a[1]),int(a[2])) == 3:
#   print(f"{a}은 목요일")
# elif calendar.weekday(int(a[0]),int(a[1]),int(a[2])) == 4:
#   print(f"{a}은 금요일")
# elif calendar.weekday(int(a[0]),int(a[1]),int(a[2])) == 5:
#   print(f"{a}은 토요일")
# elif calendar.weekday(int(a[0]),int(a[1]),int(a[2])) == 6:
#   print(f"{a}은 일요일")
while True:
  day=["월","화","수","목","금","토","일"]
  a=input("년월일을 입력하세요(ex:2022,1,4):").strip().split(",")

  date=calendar.weekday(int(a[0]),int(a[1]),int(a[2]))
  print(f"{a[0]}년 {a[1]}월 {a[2]}일은 {day[date]}요일입니다.")
