'''
**  time 모듈로 현재 시간 구하기
먼저 시간을 표현하는 time 모듈입니다. 
다음과 같이 time 모듈의 time 함수를 호출하면 
1970년 1월 1일 0시 0분 0초 이후 경과한 시간을 초단위로 반환합니다. 
시간대는 UTC(Universal Time Coordinated, 협정 세계시)를 사용합니다.
'''
import time

#ex1> 1970년 1월 1일 0시 0분 0초 이후 경과한 시간을 초단위로 반환
print(time.time())