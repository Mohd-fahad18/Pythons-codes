# 1 calculator'''

'''ope =input("entre the ope (+-*?) :")
a=float(input("enter no 1: "))
b =float(input("enter no 2: "))

if ope=="+":
    print(a+b)

elif ope == "-":
    print(a-b)

elif ope == "*":
    print(a*b)

elif ope == "/":
    print(a/b)

else:
    print(f"it is invalid ope {ope}")'''

#2 Weight conversion'''

'''weight =float(input("enter your weight :"))
unit =input("enter the unit kg or lbs :")

if unit == "kg":
    weight*=2.205
    unit="lbs"

elif unit=="lbs":
    weight/=2.205
    unit ="kg"

else :
    print("enter correct unit")

print(f"your weight is {weight:.2f} {unit}")'''

#3 greter three digit no'''

'''a=int(input("entre a : "))
b=int(input("entre b : "))
c=int(input("entre c : "))

if a>b and a>c:
    print("a is gretest")
    
elif b>c and b>a:
    print("b is gretest")

elif c>b and c>c:
    print("a is gretest")'''
    
#4 int is pos+ or neg-

'''a=int(input("entre a :"))

if a>0:
    print(f"{a} is positive")

elif a<0:
    print(f"{a} is negative")

else :
    print("the input value is zero")'''

#5) check of a leap year

'''year = int(input("enter the year :"))

if year%4==0:
    if  year%100==0:
         if year%400==0:
            print("year is leap year")
         else:
            print("is not a leap year")

    else:
        print("is a leap year")


else: 
    print("not a leap year")'''

#6) area of fig
'''
import math
fig=input("entre fig for area (circle,rec,sq,tri) :")

if fig=="circle":
    r=int(input("enter the radiu :"))
    print(math.pi*r**2)

elif fig == "rec":
    l=int(input("length :"))
    b=int(input("bredth :"))
    print(l*b)

elif fig == "sq":
    l=int(input("length :"))
    print(l**2)

elif fig == "tri":
    h=int(input("height :"))
    b=int(input("base :"))
    print(b*h/2)

else:
    print("enter a valid fig")'''


#diamond

'''n= int(input("enter the n :"))
for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")

    for j in range(i):
        print("*",end=" ")

    for j in range(i-1):
        print("*",end=" ")


    print()

for i in range(n+1):
    for j in range(i+1):
        print(" ",end=" ")
    
    for j in range(i,n-1):
        print("*",end=" ")

    for j in range(i,n-2):
        print("*",end=" ")

    print()'''

#TABLE OF ANY NUMBER

'''number=int(input("enter the no :"))
n=0                  
for x in range(1,11):
    x*=number
    n+=1
    print(f"{number} X {n} = {x}")'''


#define function 

'''def fxn(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
a,b,c,d=fxn(20,10)

print(f"add is {a} \nsub is {b} \nand div is {d}")'''

#define function (area of fig)

'''def area():
    n=input("enter the area of dig cir,rec , sq , tri :")
    if n=="cir":
        r=int(input("enter the radius :"))
        print(3.14*r*r)

    elif n == "rec":
        l=int(input("length of rec :"))
        b=int(input("length of rec :"))
        print(l*b)

    elif n == "sq":
        l=int(input("enter the side :"))
        print(l**2)

    elif n == "tri":
        h=int(input("hight of tri :"))
        b=int(input("base of tri :"))
        print(h*b/2)

    else:
        print("enter invalid dig ")

area()'''


#factorial

'''def factorial(n):
    #n=int(input("enter th value :"))
    x=1
    for i in range(1,n+1):
        x*=i
    return x

print(factorial(6))
    '''

#timer count down

'''import time

def countR(start,end):
    for X in range(start,end+1):
        print(X)
        time.sleep(3)
    print("SO JAA BABA !")

countR(0,455)
'''

#ROCK PAPER SCISSOR GAME

'''import random

opt=("rock","paper","scissor")
player=None
comp=random.choice(opt)

print("---LET'S PLAY---\n")

while player not in opt:
    player=input("enter your choice rock,paper,scissor :")
print(f"player choice is {player}\ncomp choice is {comp}")

if player=="rock" and comp == "paper":
    print("YOU WIN ! TRY AGAIN")

elif player == "paper" and comp == "scissor":
     print("YOU WIN ! TRY AGAIN")

elif player == "scissor" and comp == "rock":
     print("YOU WIN ! TRY AGAIN")

else :
    print("\n YOU LOSE\nTRY AGAIN!")'''


#global and nonlocal
'''x=10
def outer():
    y=20
    def inner():
        nonlocal y
        y+=10
        print(f"nonlocal y is : {y}")
    print(y)
    inner()

    print(f"global x is {x}")
    
outer()'''

#recursion
#1factorial using recursion

'''def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print(f"factorial  is : {fact(5)}")'''

#2fibonacci

'''n= int(input("enter the range for series :"))
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

for i in range(n+1):
    print(fibo(i),end=" ")
'''
#sum of digits
'''def sum(n):
    if n == 0:
        return 0
    else:
        return n+sum(n-1)

print(f"sum  is : {sum(50)}")'''

#anonymous fxn

#lambda and filter(make new list which suit the condition)

#even and odd
'''no=[1,2,3,4,5,6,7,8,9,11,13,17,12,19,24,65,33]

even=list(filter(lambda n:n%2==0,no))
odd=list(filter(lambda n:n%2==1,no))
print("***LIST IS***")
print(no)

print(f"\n---FILTER LIST IS BELOW---\n")
print(f"list of even is = {even}\nlist of odd is ={odd}")'''

#str lenth less than 5
'''
word=['apple','coconuts','apple juice','banana','berry','org']

fruit=list(filter(lambda word:len(word)<=5,word))
print(fruit)
'''

#MAP (check ever elemnt and modify to make new list)
#temp conversion using map

'''no=[10,20,4,33,45]
temp=list(map(lambda x:(9/5)*x+32,no))

print(f"temp in fahranhite is {temp} ")'''

#adding of 2 list using map

'''l1=[10,20,30,40,50,1]
l2=[21,31,41,51,61,2]

add=list(map(lambda x,y:x+y,l1,l2))

print(add)'''


#captilize first letter
'''
listtt=['apple','banan','graphs']

capt=list(map(str.capitalize,listtt))

print(capt)'''

#reduce () (use to reduce list and single output)
#find prduct of all no in list

'''from functools import reduce
gr=[2,3,5,7,9]

product=reduce(lambda x,y:x*y,gr)
print(product)'''

#max no in list

'''from functools import reduce
no=[10,20,31,44,56,6,78]

nofilt=list(filter(lambda x:x>30,no))

gr_no=reduce(lambda x,y:x if x>y else y,no)

print(f"no greter than 30 are = {nofilt}\nno gretest is ={gr_no}")'''

#sum of sq
'''from functools import reduce
no=[1,3,4,6]
sum_sq=reduce(lambda x,y:x+y**2,no)
print(sum_sq)'''


