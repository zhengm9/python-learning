import keyword
import sys
#keyword.kwlist
print ("Hello, Python!") ;
if True:
	print("true");
else:
	print("false");
str="hello world";
print("test result:"+str[0:-1]);
print("命令行参数为：");
for i in sys.argv:
	print (i);
print("\npython·路径为：",sys.path);