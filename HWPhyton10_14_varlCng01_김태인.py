'''
변수의 값 서로 변경
'''

var01=100;
var02=200;

print(var01)
print(var02)

print('='*30)
var01=var02

print(var01)
print(var02)
#이렇게 하면 var01값 100이 날아감.
print('='*30)

var01=100;
var02=200;

temp=var01
var01=var02
var02=temp

print(var01)
print(var02)
#temp로 임시 저장해주는 방식으로 해줘야 서로 변경됨!