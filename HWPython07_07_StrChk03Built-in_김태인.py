#연습1
a = "Hello, World!"
print(a.upper())
#모든 문자를 '대문자'로
print('='*30)

#연습2
a = "Hello, World!"
print(a.lower())
#모든 문자를 '소문자'로
print('='*30)

#연습3
a = "       Hello, World!       "
print(a.strip())
print(f'woosong{a}woosong')
print(f'woosong{a.strip()}woosong')
#불 필요한 공백을 지워줌
print('='*30)

#연습4
a = "Hello, World!"
print(a.replace("H", "J"))
#a.replace("H", "J")>H를 J로 치환해라
print('='*30)

#연습5
a = "Hello, World!"
b = a.split(",")
print(b)
print(type(b))