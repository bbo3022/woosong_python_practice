import csv

file=open('./../_dateSetGilBut01/gwangju.csv','r')
gwangju_csv=csv.reader(file)
vHeader=next(gwangju_csv)

tempFileList=[]
vtempFileList=[]

for tempList in gwangju_csv:
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
f=open("./../_dateSetGilBut01/gwangjuNullChk.csv","a")
f=open("./../_dateSetGilBut01/gwangjuNullChk.csv","w")
for lastNullChk in range(len(vtempFileList)):
  vList=",".join(vtempFileList[lastNullChk])+"\n"
  f.write(vList)
f.close()