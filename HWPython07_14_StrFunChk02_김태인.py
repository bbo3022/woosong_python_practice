#문자열 삽입(join)_각각의 문자 사이에 ','를 삽입

print(",".join('abcd'))

print(','.join(['a','b','c','d']))

print(['a','b','c','d'])

for idx in ['a','b','c','d']:
	print(f'{idx}',end="")

print("="*15)

#소문자 대문자로
a="hI"
print(a.upper())
print(a.lower())
