#수정이 불가항목들 튜플을 사용해서 표현
'''
t1=(1,2,3,4)
t2=tuple()
print(t1)
print(t2)
t3=1,2,3,4,5,3,3,10,3
print(type(t3))
print(t3.count(3))
print(t3.index(3))

t4=1,2,3,4,5,3,3,10,3
#sorted() #원본유지
#lst.sort() #원본이 바뀜
print(tuple(sorted(t4)))
'''
#dictionary
dic1={1001:'홍길동',1002:'김길동',1003:'박길동',1004:'고길동'}
print(dic1[1001])
d2=dict()
d2['강좌명']='파이썬'
d2['개설요일']='화요일'
d2['년도']=2003
d2['수강생']=['김','이','박']
print(d2)
print(len(d2))
print('-------------------------------------------------------')
dic2={1:'1월',2:'2월',3:'3월',4:'4월',5:'5월',6:'6월',7:'7월',8:'8월',9:'9월',}
'''
print(len(dic2))
for i in range(1,len(dic2)+1):

print(dic2.keys())
print(dic2.values())
print(dic2.items())

for i in dic2.values() :
   print(i)
'''
'''
for i in dic2.items():
    print(i[1])

for k,v in dic2.items():
    print(v)

for i in dic2:
    print(i)
    print(dic2[i])


print(dic2.pop(9))
print(dic2.popitem())

print(dic2.update({3:'march'}))
print(dic2)
dic2.update({150:'15월'})
print(dic2)

print(dic2.get(1))
'''
# dictionary - tuple -list 변환
# list - tuple -dictionary 변환
# seq=['a','b','c','d']
# seqt=tuple(seq)

# seql2=list(seqt)
# print(seql2)

# seqd=dict(enumerate(seq))
# print(seqd)
'''
li=['1조','2조','3조']
YA=['홍','김','이']
YB=['최','한','James']
z= zip(li,YA,YB)
print(z)
print(list(z))
print(tuple(zip(li,YA,YB)))
print(z)

# 제일 짧은 리스트에 맞춰서 한다.
l10=['한식','양식','중식','분식']
l11=['전주식당','닥터로빈','취영루','토마토']
l12=['제육','파스타','짬뽕','김밥']

print(list(zip(l10,l11,l12)))
l100=list(zip('ABCD',l10,l11,l12))
for i in l100:
    print(i[0],i[1],i[2])

a=dict(zip(l10,l11))
print(a)
print(dict(zip(l10,zip(l11,l12))))
print(list(enumerate(l11)))
print(dict(enumerate(l11)))

'''

l21=['파이썬','C','C++','Java','AI']
l22=[101,102,103,104,105]
a=dict(zip(l21,l22))
print(a)
while True :
    b=input('강의명')
    if(b in l21):
        print(a.get(b))
    elif(b=='quit'):
        break
    else:
        print('그런과목 없어')
    