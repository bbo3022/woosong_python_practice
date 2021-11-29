def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

'''
연습01
100-50=50
50-50=0
65-50=15
82-50=32
23-50=-27> but abs는 절대값으로 나타내기때문에 27.

연습02
오름차순으로 정리
0>15>27>32>50
'''