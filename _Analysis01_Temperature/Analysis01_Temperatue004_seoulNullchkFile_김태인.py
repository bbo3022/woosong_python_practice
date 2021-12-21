import csv

file=open('./../_dateSetGilBut01/Seoul.csv','r')
Seoul_csv=csv.reader(file)
vHeader=next(Seoul_csv)

tempFileList=[]
vtempFileList=[]

for tempList in Seoul_csv:
	tempFileList.append(tempList)
file.close()

print("전처리 전 ",len(tempFileList))
#for vtempList in tempFileList:
 # if vtempList[2]=="":
for nullChkData in tempFileList:
  if nullChkData[2]=="" or nullChkData[3]=="" or nullChkData[4]=="":
    del (nullChkData)
  else:
    vtempFileList.append(nullChkData)
print("전저리 후 ",len(vtempFileList))
f=open("./../_dateSetGilBut01/seoulNullChk.csv","a")
f=open("./../_dateSetGilBut01/seoulNullChk.csv","w")
for lastNullChk in range(len(vtempFileList)):
  vList=",".join(vtempFileList[lastNullChk])+"\n"
  f.write(vList)
f.close()