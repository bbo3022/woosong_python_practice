'''
Copy List

cannot copy a list simply by typing list2=list1
because: list2 will only be a reference(참조) to list1

for ex)
01. result01=list([1,2,3])     result 01                     [               ]->10(주소값)
                                                  null<-10                              └>list([1,2,3])

      result02=list([1,2,3])    result 02                     [               ]->20(주소값)
                                                  null<-20                              └>list([1,2,3])


02. result02=result01 
        10                10      -> 즉 주소값 10 이 같아지는 것이므로. 카피가 아님. 
		
		                                         result 01                     [               ]->10(주소값)
                                                 null<-10                              └>list([1,2,3])

												 result 01                     [               ]->20(주소값)
                                                 null<-                                   └>list([1,2,3])
												 20이 아닌 10이됨                             
'''
#연습1
result01=[1,2,3]
result02=[1,2,3]
 
result02=result01
print(result01)
print(result02)

result01[1]='apple'
print(result01)
print(result02)

#연습2
result01=[1,2,3]
result02=[1,2,3]
 

print(result01)
print(result02)

result01[1]='apple'
print(result01)
print(result02)