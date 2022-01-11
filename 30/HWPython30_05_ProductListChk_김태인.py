import csv

file=open("product.csv","r", encoding="utf8")
prod=csv.reader(file)
next(prod)
for vprod in prod:
  print(vprod)