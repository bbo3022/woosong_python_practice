import re

patt=re.compile(r"\w+\s+\d+[-]\d+[-]\d+")

mapp=patt.search("Kim 010-1234-1234")

print(mapp)
print("="*30)

patt=re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")

mapp=patt.search("Kim 010-1234-1234")

print(mapp.group(1))
print("="*30)


patt=re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")

mapp=patt.search("Kim 010-1234-1234")

print(mapp.group(2))
print("="*30)


patt=re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")

mapp=patt.search("Kim 010-1234-1234")

print(mapp.group(3))
print("="*30)

