a='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=html&oquery=server&tqi=hifgBdp0YihssifaW6GssssstdK-497397'

print(a)
print('='*100)
firsts=a.split('?')
seconds=firsts[1].split('&')

print('url:',firsts[0])
print('Query String')
for x in range(len(seconds)):
	print(" ",seconds[x])
print('##Query String:',len(seconds))