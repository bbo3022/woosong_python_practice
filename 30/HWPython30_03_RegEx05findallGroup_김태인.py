import re

patt=re.compile('[a-z]+')

result=patt.findall("life is too short 3Exam Nice")
print(result)
print("="*30)

result=patt.finditer("life is too short")
print(result)
print("="*30)
for r in result:
  print(r)
  print(r.group())
print("="*30)

mapp=patt.match("have a nice day")
print(mapp.group())
print(mapp.start())
print(mapp.end())
print(mapp.span())
print("="*30)