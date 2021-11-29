#연습1(ascending, by default)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#기본값은 오름차순(영어는 알파벳순/한글은 ㄱㄴㄷ순)

#연습2(numerically)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#숫자의 경우 오름차순은 작은수 부터 큰것

#연습3(reverse=True)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#reverse = True는 내림차순!(오름차순의 반대)

#연습4(reverse = True)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#숫자도 마찬가지로 reverse = True(내림차순) 사용시 큰 숫자에서 작은숫자 순으로 배열

#연습5(Function)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

'''
step 01
function의 내용대로 리스트의 요소를 순서대로 대입해보면
100-50=50
50-50=0
65-50=15
82-50=32
23-50=-27> but abs는 절대값으로 나타내기때문에 27.

step 02
오름차순으로 정리
0>15>27>32>50

step 03
각 결과를 오름차순으로 도출해낸 요소 순으로 배열하면
50, 65, 23, 82, 100 으로 결과가 나오게 된다.
'''