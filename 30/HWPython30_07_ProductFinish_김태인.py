import csv
import re

productFile=open("product.csv","r", encoding="utf8")
productList=productFile.readlines()

productList.pop(0)

def productChk(vItem):
	patt=re.compile('Mirror|Chair|Table|Sofa')
	splitChk = vItem.split(',')
	vresult=""
	vItem=patt.search(vItem)
	if vItem:
		if vItem.group()=='Mirror':
			vresult='거울'
		elif vItem.group()=='Chair':
			vresult='의자'
		elif vItem.group()=='Table':
			vresult='테이블'
		elif vItem.group()=='Sofa':
			vresult='소파'
	elif re.search("^\d+$",splitChk[2]):
		vresult='품목 에러 확인'
	else:
		vresult='품목 미체크 확인'
	return vresult

result=list(map(productChk, productList))
print(result)
#print(productList)
productChkList = []
for idx, idxItem in enumerate(productList):
	tempList = idxItem.split(',')
	tempList.insert(-1, result[idx])
	productChkList.append(tempList)

print(productChkList)