str="파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 "
'''
print('{}+{}={}'.format(2,3,5))
a,b=5,10.0
print('{}+{}={}'.format(a,b,a+b))
print('{0}+{1}={2}'.format(a,b,a+b))
print('{0:d}+{1:f}={2:f}'.format(a,b,a+b))
print('{0:d}+{1:f}={2:f},{3:s}'.format(a,b,a+b,"hdhd"))




newstr=str.replace("파이썬","자바")
print("str : ",str)
print("newstr : ", newstr)

print('str.count("파이썬") : ', str.count("파이썬"))


print('**'.join(str))

print(str.find("파이썬")) 
print(str.find("파")) 
print(str.find("썬")) 

# find는 -1을 반환하고 index는 에러가 나온다.

print(str.index("파이썬"))
print(str.index("파"))
print(str.index("썬"))

print(str.split())
print(str.split(""))
'''

value = False
print(type(value))
print(int(value))

print(bool(0),bool(1),bool(1.2222),bool(-12))
print(bool("hello"),bool("-1"),bool(""))


