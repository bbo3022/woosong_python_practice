word = ['winter', 'cold', 'positive', 'negative', 'positive']

wordSet=list(set(word))
print(wordSet)

wordDict={}
for idx in wordSet:
  wordDict[idx]=word.count(idx)

print(wordDict)

for idx in wordDict:
  print(f"{idx}단어의 개수는 {wordDict[idx]}입니다.")