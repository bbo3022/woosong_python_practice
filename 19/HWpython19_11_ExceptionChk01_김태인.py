#ZeroDivisionError
print(100/0)

#FileNotFoundError

with open("없는파일.txt","r") as f:

#NameError

X="안녕하세요"
print(x)


#Type Error

x=10
print(x+"띠용")

#Key Error

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["color"]
print(x)

#Index Error

a=[1,2,3,4,5]
print(a[5])