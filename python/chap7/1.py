#함수
#input 을 주면  output 이 나옴 
'''
input 숫자
output 숫자
이런 기능을 하는 function -multi
'''

def multi(num1) :
    ouput_num=num1*3
    print("여기는 multi 함수 안입니다.")
    return ouput_num

print(multi(10))

def Hello(name1,name2) :
    print("안녕" ,name1)
    print("안녕 ",name2)
Hello('송영민','absc')

def sum1(a,b) :
    ham=0
    ham=a+b
    print(ham)

sum1(1,4)

def sum2(a,b) :
    return print(a+b)

sum2(1,4)
#전역 변수 지역변수
def addone():
    num=10
    print("addone",num+1)

addone()

def Hello2(*n) :
    for i in n:
        print('hello',i)

Hello2('ad','abc','ab2ee')

def sumall(*v):
    sum=0
    for i in v:
        sum+=i
    return sum
print(sumall(1,2,3,4,5,6,7,8,9,10))
lst1=[1,2,3,4,5,6,7,8,9,10]
print(sumall(*lst1))
coffe={'아메':2000,'라떼':3000,'티':2500}
def printmenu(**ab) :
    for i in ab:
        print(i,ab[i])

printmenu(**coffe)
printmenu(아메=2000,라떼=3000,티=2500)

def fun1(*num,**menu) :
    sum=0
    for i in num:
        sum+=i
    print(sum)
    for i in menu:
        print(i,menu[i])
fun1(1,2,3,4,5,6,아메=2000,핫초코=3000,티=2500)
fun1(*lst1,**coffe)

#lambda 함수

print((lambda x : x+1)(100))
print((lambda x ,y : x+y)(100,200))
lst2=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x+1,lst1)))
print(list(map(lambda x,y:x+y,lst1,lst2)))




    