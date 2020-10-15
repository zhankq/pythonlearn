import os,sys

#ret = os.access("foo.txt", os.F_OK)
#print ("F_OK - 返回值 %s"% ret)

path = "/tmp"

# 查看当前工作目录
retval = os.getcwd()
print ("当前工作目录为 %s" % retval)

# 修改当前工作目录
os.chdir( path )

# 查看修改后的工作目录
retval = os.getcwd()

print ("目录修改成功 %s" % retval)