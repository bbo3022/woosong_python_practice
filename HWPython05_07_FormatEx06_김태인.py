alignLeft     ="{1:<10}".format("niceday","hi")
alignRight   ="{:>10}".format("niceday")
alignCenter  ="{0:^10}".format("niceday")

#공백채우기
spaceFill01="{0:*^10}".format("hi")

print(alignLeft)
print(alignRight)
print(alignCenter)
print(spaceFill01)

x=3142523452
y=3.142523452

floatEx1="{0:0.4f} {1:,d}" .format(y,x)
floatEx2="{0:10.4f}".format(y)

print(floatEx1)
print(floatEx2)