import csv

file=open('./../_dateSetGilBut01/Seoul.csv','r')
Seoul_csv=csv.reader(file)
vHeader=next(Seoul_csv)
allData=0
Hdata=0
Ldata=0
Adata=0
for tempList in Seoul_csv:
  #print(tempList)
  allData+=1 #총 데이터 개수
  if tempList[2] =="":
    Adata+=1
  if tempList[3] =="":
    Ldata+=1
  if tempList[4] =="":
    Hdata+=1

print("데이터 총 개수:",allData)
print("최고 기온 중 null개수:",Hdata)
print("최저 기온 중 null개수:",Ldata)
print("평균 기온 중 null개수:",Adata)