'''
# 문자 --> 객체
** 문자열로 날짜/시간 객체 만들기
strptime 메서드를 사용하면 문자열 형태의 날짜를 datetime.datetime 객체로 만들 수 있습니다. 
이때는 날짜/시간 포맷을 지정해줘야 합니다.

형식 ] datetime.datetime.strptime('날짜문자열', '포맷')

'''
import datetime,time

vDay=datetime.datetime.strptime('2022-1-5', '%Y-%m-%d')
print(vDay)