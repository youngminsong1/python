# 제어문
'''
hour =15

if hour < 12 :
    print("오전입니다.")
elif hour<18 :
    print("오후입니다.")
else :
    print("저녁입니다.")


score = input("점수")
intscore=int(score)
if intscore <200:
    print(50)
elif intscore < 400 :
    print(100)
else :
    print(1000)




rice = input("밥먹어?")

if rice =="yes" :
    print("8호관 1층")
else :
    rerice=input("학식")
    if rerice=="yes" :
        print('8호관 3층')
    else :
        print("안먹어")
'''


# 반복문
'''
for i in 1,3,4,5,6 :
    print(i)

for i in range(0,11,2) :
    print(i)

s=0
for i in range(1,11) :
   s=s+i  
else :
    print(s)


i=10
while i>5 :
    print(i,"는 5보다 크다")
    i-=1

#n=1~5까지 찍어보는 것
n=1
while n < 6 :
    print(n,end=' ** ')
    n=n+1
else :
    print("while이 잘 끝남. 현재 n의 값은 ", n ,"입니다.")



n=0
while n<4 :
    m=input("키를 입력하세요")
    intm=int(m)
    if intm >150 :
        n=n+1
    print("현재 " ,n, "명입니다." )
else :
    print("놀이기구 출발")
'''

while True :
    str=input("단어 입력")
    if str =='exit' :
        print('exit 합니다')
        break
    else :
        if str =='apple' :
            print('apple을 입력했다.')
            continue
        else :
            print(str*3)


'''
while True :
    str =input("단어를 넣으세요")
    if str=='exit' :
        print('종료합니다.')
        break
    else :
        if str=='apple' :
            print('apple을 입력받았다')
            print("continue를 실행함")
            continue
        print(str ,"을 선택함")
    print('저는 아직 while 안에 있습니다.')
print('while이 종료됨')
'''