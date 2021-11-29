#python - Unpack Tuples

#연습1(unpacking)
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#언팩킹을 할 때는 요소 순서대로 배정된다(수가 일치해야함)

#연습2(Asterisk*)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#변수의 수가 적을 때는 *를 사용해 나머지를 한번에 리스트로 언팩킹한다.

#연습3
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#만약 *가 중간에 오게 되면 처음과 마지막 변수가 각각의 값의 요소를 갖고(green=apple/red=cherry) 나머지 가운데 요소들을 tropic에 저장한다.