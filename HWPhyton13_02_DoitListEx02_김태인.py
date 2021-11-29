#형식:리스트명=[요소1, 요소2, 요소3,...]

a=[1,2,3,['a','b','c']]
print(a[0])#1
print(a[-1])#['a','b','c']
print(a[3])#['a','b','c']
print('-'*15)

print(a[-1][0])#'a'
print(a[-1][1])#'b'

a=[1,2,['a', 'b', ['life','is']]]
print(a[2][2][0])#'life'

print('-'*15)