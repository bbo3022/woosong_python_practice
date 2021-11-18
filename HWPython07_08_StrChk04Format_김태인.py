#String Concatenation
#연습1
a = "Hello"
b = "World"
c = a + b
print(c)
#a 와 b 를 합쳐서 보여줌

#연습2
a = "Hello"
b = "World"
c = a +" " + b
print(c)
#중간에 띄어쓰기를 넣고싶으면 이런 방식으로

#Format-Strings
#연습1
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

'''
age = 36
txt = "My name is John, I am " + age
print(txt)
문자와 숫자를 연산할 수 없기 때문에(+넣으면 연산으로 인식) .format으로  해줌'''

#연습2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#각 자리에 표시됨

#연습3
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#인덱스로 배치해줘도 가능(인덱스는 0번부터)

#Escape Character\
#연습1
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
#""안에 ""를 사용 못함. 그래서 \를 사용

#연습2
txt = 'We are the so-called "Vikings" from the north.'
print(txt)
#또'' 안에 ""를 사용하면 됨