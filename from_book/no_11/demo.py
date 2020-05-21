import sys
print(sys.path)
f=open("somefile.txt",'w')
f.write("Hello, ")
f.write('World!')
f.close()
