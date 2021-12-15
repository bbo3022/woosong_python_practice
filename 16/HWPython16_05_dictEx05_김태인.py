#Nested Dictionaries

#연습1

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#Dictionaries는 중첩해서 사용이 가능합니다. 


#연습2
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

#가독성이 편하도록 미리 딕셔너리들을 생성해 놓은 다음 다른 딕셔너리에 넣는 방식으로 해도 같은 결과.