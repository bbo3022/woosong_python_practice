word = ['winter', 'cold', 'positive', 'negative', 'positive']

wordSet=list(set(word))
print(wordSet)

vMax=-99999
vMin=+99999
vMax_word=""
vMin_word=""


for idx in wordSet:
  if vMax < len(idx):
    vMax=len(idx)
    vMax_word=idx
  elif vMax==len(idx):
     vMax_word=","+idx

  if vMin > len(idx):
    vMin=len(idx)
    vMin_word=idx


print(f"가장 긴 단어는{vMax}글자인 {vMax_word}입니다.")
print(f"가장 짧은 단어는{vMin}글자인 {vMin_word}입니다.")