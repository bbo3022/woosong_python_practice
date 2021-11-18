#왼쪽/오른쪽/양쪽 공백 지우기(lstrip/rstrip/strip)

a=' hi '
print(a)
print(a.lstrip()+'chk')
print(a.rstrip()+'chk')
print('chk'+a.strip()+'chk')

print("="*20)

#문자열 바꾸기
a="Life is too short"
print(a)
cng=a.replace("Life","Your leg")
print(cng)