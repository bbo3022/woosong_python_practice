var01=100
var02=200

print('변경 전')
print("var01:",var01)
print("var02:",var02)

var01,var02=var02,var01

print('변경 후')
print("var01:",var01)
print("var02:",var02)

#valcng01번은 기본 방법이고 이렇게 간단하게 할 수 도 있음.