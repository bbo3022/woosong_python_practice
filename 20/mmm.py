try:
	file=open("./../_dateSet02Mem/MemV03.txt","r")
except FileNotFoundError:
	file=open("./../_dateSet02Mem/MemV03.txt","a")
	file=open("./../_dateSet02Mem/MemV03.txt","r")
else:
	line=file.readlines()
finally:
	file.close()