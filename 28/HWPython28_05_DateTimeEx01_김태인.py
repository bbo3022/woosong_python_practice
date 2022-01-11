'''
** datetime 모듈로 현재 날짜와 시간 구하기
이번에는 datetime 모듈의 datetime 클래스를 사용해보겠습니다. 
datetime.datetime으로 현재 날짜와 시간을 구할 때는 today 메서드를 사용합니다
(현재 시간대 기준, KST).

'''
import datetime,time

print(datetime.datetime.today())
