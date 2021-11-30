Recommend=('민교','강경태', '고재호', '김태인', '한현기','재호','민교','재호','선웅','박연희','민교', '선웅', '강경태', '고재호', '김태인', '한현기', '이준혁','민교', '선웅','임재우'
,'민교','강경태','경태','경태')

Rec=list(Recommend)
x=[]

for Name in Rec:
	if len(Name)==3:
		x.append(Name[1:])
	else:
		x.append(Name)
print(x)


x2=set(x)
print(x2)