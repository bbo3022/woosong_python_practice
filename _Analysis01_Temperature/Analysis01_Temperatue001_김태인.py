import csv
file=open('./../_dateSetGilBut01/Seoul.csv','r')

Seoul_csv=csv.reader(file)
for tempList in Seoul_csv:
	print(tempList)