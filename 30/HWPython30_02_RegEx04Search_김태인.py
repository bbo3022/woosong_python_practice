import re

patt=re.compile('[a-z]+')

mapp=patt.match("have a nice day")
print(mapp,"\n\n\n")

mapp=patt.match("3 python")
print(mapp,"\n\n\n")

mapp=patt.match("string goes here")
if mapp:
  print("Match found:",mapp.group())
else:
  print("No match")

mapp=patt.match("have a nice day")
print(mapp,"\n\n\n")

mapp=patt.match("3 have a nice day")
print(mapp,"\n\n\n")

#-------------------------------------------------
mapp=patt.search("have a nice day")
print(mapp,"\n\n\n")

mapp=patt.search("3 have a nice day")
print(mapp,"\n\n\n")
