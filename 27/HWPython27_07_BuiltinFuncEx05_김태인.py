"""
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
#child2는 person을 상속받았기 때문에. true 출력