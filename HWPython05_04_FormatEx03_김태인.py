test1= "Error is %d%%." %89
print(test1)

#오른쪽 정렬
test2= "%10s"%"hi1234"
print(test2)

#왼쪽 정렬
test3= "%-10s" %"hi1234"
print(test3)

#소숫점 자리수
test4="%0.4f" %3.141592990
print(test4)

#십의 자리와 소숫점 자리수
test5="%10.4f" % 3.14189843782
print(test5)