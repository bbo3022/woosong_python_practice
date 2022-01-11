'''
# 날짜 --> 객체
** 특정 날짜와 시간으로 객체 만들기
또는, datetime.datetime에 연, 월, 일, 시, 분, 초, 마이크로초를 넣어서 객체를 만들 수도 있습니다.
datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0)(현재 시간대 기준, KST).
# 문자 --> 객체
# 문자 --> 날짜

'''
import datetime,time

vDay=datetime.datetime(2022, 1, 5)
print(vDay)
print(type(vDay))

