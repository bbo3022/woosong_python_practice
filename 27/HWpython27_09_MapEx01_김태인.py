"""
map(f, iterable): 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
"""

def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times2(x): 
  return x*2

result=map(two_times2, [1, 2, 3, 4])
print(type(result))
print(list(result))