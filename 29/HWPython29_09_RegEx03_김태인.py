import re

patt01=re.compile('ca{2}t')

print(patt01.match('cat'))
print(patt01.match('caat'))
print("-"*50)

patt02=re.compile('ca{2,5}t')

print(patt02.match('cat'))
print(patt02.match('caat'))
print(patt02.match('caaaaat'))
print(patt02.match('caaaaaat'))
print("-"*50)

patt03=re.compile('ab?c')

print(patt03.match('abc'))
print(patt03.match('ac'))
print(patt03.match('abbc'))
print("-"*50)

patt04=re.compile('ca{2,}t')

print(patt04.match('cat'))
print(patt04.match('caat'))
print(patt04.match('caaaat'))
print("-"*50)

patt05=re.compile('ca{,5}t')

print(patt05.match('ct'))
print(patt05.match('caat'))
print(patt05.match('caaaaat'))
print(patt05.match('caaaaaat'))