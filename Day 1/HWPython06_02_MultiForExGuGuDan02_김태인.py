print('='*120, end='\n\n')

for a in range(2,10):
	print(a,'단', end='\t\t')

print('\n'+'='*120)

for x in range(2,10):
	for y in range(2,10):
		print(x,'X',y,'=',(x*y), end='\t')
	else:
		print()