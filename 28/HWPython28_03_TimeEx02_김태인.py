'''
**  날짜와 시간 형태로 변환하기
time 모듈의 localtime 함수를 사용하면 time에서 반환한 값을 날짜와 시간 형태로 변환해줍니다. 
특히 localtime이라는 이름 그대로 현재 지역의 시간대를 사용합니다. 
우리나라에서 실행했다면 UTC에 9시간을 더한 KST(Korea Standard Time, 한국 표준시)를 사용합니다(UTC+09:00).
 월 ~ 일 :  0 ~ 6
  tm_yday : 1월 1일부터 경과한 일수 
  m_isdst : 섬머타임 여부
'''
import time

#ex1> 1970년 1월 1일 0시 0분 0초 이후 경과한 시간을 초단위로 반환
print(time.localtime(time.time()))