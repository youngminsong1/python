'''
print("Hello \v world")
print("Hello \n world")
print("Hello"+ "\b"+ "world")
print("aaaaaa\'bbbbbb\'cccc")
print("aaaaaa\"bbbbbb\"cccc")

str_var="하하하"
print(str_var.replace("하","호"))

a="안녕하세요. 파이썬,파이썬 수업입니다."
b=a.replace("파이썬","자바",1)
print(a.replace("파이썬","자바"))
print(b)
'''
a=input("실수를 입력해")
a=str(a)
a=a.replace(".","")
print(int(a[0])+int(a[1])+int(a[2])+int(a[3])+int(a[4])+int(a[5]))
