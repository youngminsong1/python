'''
리스트 김,이,박,최
['김','이','박','최']

튜플
{'김','이','박','최'}

딕셔너리->사전
address={'홍길동' : '서울' ,'김길동' : '부천','james' : '미국'}
address['홍길동']


lst=[10,20,30,40,50]
print(type(lst))
print(lst[0]," " ,lst[1]," ",lst[len(lst)-1] )

list1=[]
list2=list()
list1.append('python')
list1.append('java')
list1.append('c++')
list1.append('python')
list1.append('python')
list1.append('python')
list1.append('python')
print(list1)
for i in range(len(list1)):
    print(list1[i])
print('---------------------------------------------------')
for i in list1:
     print(i)


print(list1.count('python'))
print(list1.index('python'))
list1[0]='AI'
list1[2]='iot'

#수정 불가 -> ,append,insert,값변경 .
list2=list1[0:3:1]
list2=list1[1:5:1]
list2=list1[2:6:3]
list2=list1[::-1]
print(list2)

#list1의 일부를 list3에 대입
list2=list1[2:6:3]
list3=[1,2,3,4,5,6,7,8]
list3[1:2]=list2
print(list3)




food=[]
food.append('짜장면')
food.append('샌드위치')
food.insert(0,'파스타')
food.insert(0,'제육')

print(food)
food.remove("제육")
print(food)
print(food.pop())
print(food.pop())

# extend
print(food)
dessert=['커피','케익','와플']


food_list = food +dessert
print(food_list)
food_list.reverse()
print(food_list)


# food.extend(dessert)
# print(food)

# food.clear()
# del()
# print(food)


l1=['oranage','apple','banana','mango']
print(sorted(l1))
l1.sort()
print(l1)
'''


'''
# 리스트 컴프리핸션
l3=[i for i in range(11)]
print(l3)



##10
l4=[i**2 for i in range(11)]
print(l4)

food=[]
food.append('짜장면')
food.append('샌드위치')
food.insert(0,'파스타')
food.insert(0,'제육')
dessert=['커피','케익','와플']
Fl=food+dessert
food.extend(dessert)

print(Fl==food)



'''
'''
#0~10 숫자의 제곱을 나타내기 리스트로 
#짝수의 제곱만

l1=[i**2 for i in range(11) if i%2==0 ]
l1=[i**2 for i in range(2,11,2)]
print(l1)

'''
#deepcopy 
food=[]
food.append('짜장면')
food.append('샌드위치')
food.insert(0,'파스타')
food.insert(0,'제육')
print(food)
#shallowcopy

wishlist=food
print(wishlist)


food.pop()
print(food)
print(wishlist)


print(food is wishlist)


#deep copy
print('===========================================================')

food2=food[:]
food3=list(food)
food3=food.copy()
print(food3)
print(food2)
print(food)

food.pop()

print(food2)
print(food)
print(food is food2)


food.append("라볶이")

print(food2)
print(food)
print(wishlist)






