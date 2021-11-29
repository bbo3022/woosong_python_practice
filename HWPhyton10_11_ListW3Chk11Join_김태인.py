##join List
#몇가지 방법이 있는데 

#연습1('+' operator)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#list1뒤에 list2가 붙는다


#연습2(one by one_append)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#lisr2의 요소들을 list1의 append한다.

#연습3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# 요소 단위가 아닌 리스트 단위도  .extend()로 join가능