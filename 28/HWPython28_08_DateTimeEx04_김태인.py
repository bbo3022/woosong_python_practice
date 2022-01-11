'''
# 날짜 --> 문자 
** 날짜/시간 객체를 문자열로 만들기
    반대로 datetime 객체를 문자열로 만들 수도 있습니다. 이때는 strftime 메서드를 사용합니다.
형식 ] datetime객체.strftime('포맷')

'''
import datetime,time

vDay=datetime.datetime.today()
print(vDay)
print(vDay.strftime("%Y-%m-%d"))
print(vDay.strftime("%c"))

print(type(vDay.strftime("%Y-%m-%d")))
print(type(vDay.strftime("%c")))