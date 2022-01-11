#result01=filter(함수, Collection)
result01= filter(lambda x: x>0,[1,-3,2,0,-5,6])
print(type(result01))
print(list(result01))

result02=map(lambda a: a*2, [1,2,3,4])
print(type(result02))
print(list(result02))