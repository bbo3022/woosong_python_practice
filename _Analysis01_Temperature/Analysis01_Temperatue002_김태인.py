import csv

file=open('./../_dateSetGilBut01/Seoul.csv','r')
Seoul_csv=csv.reader(file)
vHeader=next(Seoul_csv)
#print(vHeader)

for tempList in Seoul_csv:
	print(tempList)