#연습1(index로 change)
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#index를 사용해 리스트 내 요소를 바꿀 수 있다.

#연습2(range로 change 01)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#range를 이용해 해당 범위 내 요소를 바꿀 수 있다. 

#연습3(range로 change 02)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#range를 이용해 바꿀 때 원래의 요소가 바꾸려는 요소보다 적어도 가능.(1개의 요소와 2개의 요소 교체 가능)

#연습4(range로 change 03)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#연습3번과 반대의 상황에도 가능.

#연습5(replace 아닌 insert())
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#교체가 아닌 index를 사용해 중간에 삽입도 가능.