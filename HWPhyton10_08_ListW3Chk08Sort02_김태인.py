#연습1
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#아스키 코드엔 대 소문자 구분이 있기 때문에 오름차순으로 분류해도 예상값과 다르게 나온다.

#연습2
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#연습 1의 경우를 피하기 위해 키값을 주는데 str.lower사용해 모두 소문자로 만들고 정렬한다.()는 쓰지 않음!

#연습3
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#reverse는 알파벳 순서 상관없이 현재 보여지는 리스트의 역순으로 출력되게 해준다.