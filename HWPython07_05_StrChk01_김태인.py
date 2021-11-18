#연습1
print('hello')
print("hello")
# ""/''둘다 상관없다.
print('='*30)
#연습2
a = "apple"
print(a)
#a에 "apple"을 할당해줘서 프린트시 'apple'로 출력
print('='*30)
#연습3
a = """안녕하세요 저는 김태인입니다.
저는 대전에 살고 있습니다. 현재는 파이썬
을 공부 중입니다. """
print(a)
# 여러 줄의 문자열은 """으로 사용
print('='*30)
#연습4
a = '''안녕하세요 저는 김태인입니다.
저는 대전에 살고 있습니다. 현재는 파이썬
을 공부 중입니다. '''
print(a)
#'''도 상관없음
print('='*30)
#연습5
a = "Hello, World!"
print(a[1])
#인덱싱도 가능(인덱스는 0부터 시작/그래서 'e'로 출력)
print('='*30)
#연습6
for x in "banana":
  print(x)
 #문자열도 루프 가능
print('='*30)
 #연습7
a = "Hello, World!"
print(len(a))
#문자열 len 사용 가능
print('='*30)
#연습8
txt = "The best things in life are free!"
print("free" in txt)
#문자열 안에 찾고 싶은 단어 체크 가능
print('='*30)
#연습9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#if 문도 사용 가능
print('='*30)
#연습10
txt = "The best things in life are free!"
print("expensive" not in txt)
#not in도 가능
print('='*30)
#연습 11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  #if not in 도 물론 가능