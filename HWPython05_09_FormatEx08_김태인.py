d={'name':'홍길동', 'age':30}
result=f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
print(result)

result= f'{"hi":<10}' #왼쪽정렬
print(result)

result= f'{"hi":>10}' #오른쪽 정렬
print(result)

result= f'{"hi":^10}' #가운데정렬
print(result)
