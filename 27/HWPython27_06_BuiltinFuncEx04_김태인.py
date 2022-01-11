"""
*abs(x): 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수
*abs(x): 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
*any(x): 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대
*chr(i):  유니코드(Unicode) 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
    ※ 유니코드는 전 세계의 모든 문자를 컴퓨터에서 일관되게 표현하고 다룰 수 있도록 설계된 산업 표준이다.
*ord(c): 문자의 유니코드 값을 돌려주는 함수이다.
    ※ ord 함수는 chr 함수와 반대이다.
    print(chr(65))
    print(chr(97))
    print(chr(44032))
    print(ord('A'))
    print(ord('a'))
*pow(x, y):  x의 y 제곱한 결괏값을 돌려주는 함수
    print(pow(2,4))
*range([start,] stop [,step] ): for문과 함께 자주 사용하는 함수이다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.
    print(list(range(0,8)))
*round(number[, ndigits]): 숫자를 입력받아 반올림해 주는 함수
    print(round(4.6))
    print(round(4.2))
*sorted(iterable): 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수/sorted(iterable, *, key=None, reverse=False)
    ※ 리스트 자료형에도 sort 함수가 있다. 하지만 리스트 자료형의 sort 함수는 리스트 객체 그 자체를 정렬만 할 뿐 정렬된 결과를 돌려주지는 않는다.
    print(sorted((3, 2, 1)))
    print(sorted((3, 2, 1),reverse=True))
*str(object): 문자열 형태로 객체를 변환하여 돌려주는 함수
*sum(iterable): 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수
*tuple(iterable): 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다. 만약 튜플이 입력으로 들어오면 그대로 돌려준다.
  List >> is a collection which is ordered and changeable. Allows duplicate members.
  Tuple >> is a collection which is ordered and unchangeable. Allows duplicate members.
  Set >> is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
  Dictionary >> is a collection which is ordered** and changeable. No duplicate members.
*type(object): 입력값의 자료형이 무엇인지 알려 주는 함수이다.
*zip(*iterable): 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
    ※ 여기서 사용한 *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미이다.
    print(list(zip([1, 2, 3], [4, 5, 6])))
*dir: 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다.
*divmod(a, b): 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수
*enumerate: "열거하다"라는 뜻이다. 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
    ※ 보통 enumerate 함수는 다음 예제처럼 for문과 함께 자주 사용한다.
*eval(expression ): 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수
*filter(function, iterable): 무엇인가를 걸러낸다는 뜻으로 filter 함수도 동일한 의미를 가진다.
          filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 
          그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.
          Construct an iterator from those elements of iterable for which function returns true.
*map(f, iterable): 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다./Return an iterator that applies function to every item of iterable, yielding the results.
        def positive(l): 
        result = [] 
        for i in l: 
            if i > 0: 
                result.append(i) 
        return result

    print(positive([1,-3,2,0,-5,6]))

    def positive2(x):
        return x > 0

    print(list(filter(positive2, [1, -3, 2, 0, -5, 6])))
    print(type(filter(positive2, [1, -3, 2, 0, -5, 6])))
*hex(x): 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수

        print(hex(234))


        #234
        -2진수:11101010
        -8진수:352
        -16진수: ea
*id(object): 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수
*input([prompt]): 사용자 입력을 받는 함수
*int(x): 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그대로 돌려준다.
*isinstance(object, class ): 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다. 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
"""
class person:
  pass

class child:
  pass

class child2(person):
  pass

a=person()
b=child()
c=child2()

print(isinstance(a,person))
print(isinstance(b,person))
print(isinstance(c,person))