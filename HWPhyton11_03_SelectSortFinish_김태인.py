a = [75,65,100,80,90,55,95,30,20,50]

print('sort전 데이터:',a,end='\n\n')

for outerLoop in range(len(a)-1):
	for innerLoop in range(outerLoop+1,len(a)):
		if a[outerLoop]>a[innerLoop]:
			a[outerLoop],a[innerLoop]=a[innerLoop],a[outerLoop]

print('오름차순으로 sort한 데이터:',a,end='\n\n')

for outerLoop in range(len(a)-1):
	for innerLoop in range(outerLoop+1,len(a)):
		if a[outerLoop]<a[innerLoop]:
			a[outerLoop],a[innerLoop]=a[innerLoop],a[outerLoop]

print('내림차순으로 sort한 데이터:',a,end='\n\n')
