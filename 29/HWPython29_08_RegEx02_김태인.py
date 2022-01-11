import re

patt01=re.compile('a.b')
patt02=re.compile('ca*t')
patt03=re.compile('ca+t')

print(patt01.match('aab'))
print(patt01.match('a0b'))
print(patt01.match('a000b'))
print(patt01.match('abc'))

print(patt02.match('ct'))
print(patt02.match('cat'))
print(patt02.match('caaat'))

print(patt03.match('ct'))
print(patt03.match('cat'))
print(patt03.match('caaat'))
