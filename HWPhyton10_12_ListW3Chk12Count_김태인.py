#연습1 loop이용 cherry 갯수 반환
fruits = ["apple", "banana", "cherry", "cherry", "cherry"]

number=0
for x in fruits:
	if x=="cherry":
		number=number+1
print(number)

i=0
number=0
while i < len(fruits):
	if fruits[i]=="cherry":
		number+=1
	i+=1
else:
		print(number)
	

#연습2 count 함수 이용 cherry 갯수 반환
fruits = ["apple", "banana", "cherry", "cherry", "cherry"]
x = fruits.count("cherry")

print(x)