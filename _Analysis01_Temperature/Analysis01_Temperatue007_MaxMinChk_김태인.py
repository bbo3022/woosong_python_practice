vList=[100, 90, 80, 30, 95, 20]
#최대값 최소값을 출력하세요.

vMax=-99999
vMin=+99999
for idx in vList:
  if vMin > idx:
    vMin=idx
  if vMax < idx:
    vMax=idx
print("최소값은",vMin)
print("최대값은",vMax)

print(min(vList))
print(max(vList))
