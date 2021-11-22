#연습1(indexed)
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#index를 사용할 수 있다(index는 0부터 시작.)

#연습2(negative)
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#index를 Nagative로 사용 가능(이 때는 뒤에서부터 시작 BUT 0이 아닌 -1부터 시작)

#연습3(range())
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#range()(범위)로도 값을 출력 할 수 있다.(a:b:a부터 b까지이지만 b는 제외))

#연습4(Leaving out the start value)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#범위 지정 시 시작값을 생략하면 처음부터 시작

#연습5(Leaving out the end value)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#범위 지정 시 종료값을 생략하면 마지막까지.

#연습6(Range of Negative Indexes)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#범위도 Nagative로 지정 가능.

#연습7(in)
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
 #in 연사자 사용 가능(당연히 not in도 가능하다. )