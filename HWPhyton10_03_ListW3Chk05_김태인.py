#연습1(item_remove())
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#.remove()를 사용해 원하는 요소를 지울 수 있다.

#연습2(index_pop()01)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#.pop()으로 인덱스를 지정해 원하는 요소를 빼낼 수 있다.
#연습 1과 같은 결과로 보여지나. 1은 지우는 개념, 2는 빼내는 개념

#연습3(last_pop()02)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#인덱스를 생략하면 마지막 요소가 빼내진다.

#연습4(del_index)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#del[]인덱스를 사용해 원하는 요소 제거 

#연습5(del_indexX_구조삭제)
thislist = ["apple", "banana", "cherry"]
del thislist
#del은 리스트를 삭제도 가능()

#연습6(clear()_list still remains)
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#.clear() 사용 시 리스트가 비워지는 결과(리스트는 요소가 없어진 채로 남아있음.)
