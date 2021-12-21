import csv

file=open('./../_dateSetGilBut01/seoulNullChk.csv','r')
Seoul_csv=csv.reader(file)
vHeader=next(Seoul_csv)
print(Seoul_csv)

tempFileList=[]
vMax=-99999
vMin=+99999
vMax_temp=""
vMin_temp=""

for tempList in Seoul_csv:
  tempFileList.append(tempList)
for i in tempFileList:
  #print(type(float(tempFileList[i][3])))
  if vMax < float(i[4]):
    vMax=float(i[4])
    vMax_temp=i[0]
  if vMin > float(i[3]):
    vMin=float(i[3])
    vMin_temp=i[0]
print("기상 관측 이래 서울 최고기온은",vMax_temp,vMax,"도 입니다.")
print("기상 관측 이래 서울 최저기온은",vMin_temp,vMin,"도 입니다.")
