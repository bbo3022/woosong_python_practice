import  os
resultOs=os.environ

print(type(resultOs))
print(resultOs)
print("="*20)
resultPath=resultOs["PATH"]
#pathVal01; pathVal02; ...
#path 경로 라인단위로 출력
print(type(resultPath))

for x in resultPath.split(";"):
  print(x)