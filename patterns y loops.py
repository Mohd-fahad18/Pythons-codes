#for patterns we need nested loop
#1 loop for rows and second for columns and empty ()for chane line
#*****
#*****
#*****
#*****
#*****
'''for i in range(1,6):   #loop 1 for rows
    for j in range (1,6):    # loop 2 for coumns  
        print("*",end=" ")   # end= to print in same line
    print()                   # empty ()for line change'''


#1
#12
#123
#1234
#12345

#q2
'''for i in range(1,6):
    for j in range(1,i+1):  #i=2,(1,3) means range will 1 2 as 3 exclude in row 2
        print(i,end=" ")
    print()'''

#q3
#12345
#1234
#123
#12
#1

#same question for reverse 
'''for i in range (6,0,-1):
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()  '''

#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15
'''x=1
n=5
for i in range(n):
    for j in range(i+1):
        print(x,end=" ")
        x+=1
    print()'''

#pyramid
#    *
#   * *
# *  *  *
'''n=5
for i in range(n):
    for j in range(i,n):  #reverse zada se kum hoga
        print(" ",end="")
    for j in range(i):    #kum se zada
        print("*",end="")
    for j in range(i+1):  #kum se zada
        print("*",end="")
    print() ''' 

#*         *
#* *     * *
#* * * * * *
'''n=5
for i in range(n):
    for j in range(i+1):  #kum se zada necche no of star brhenge
        print("*",end=" ")
    for j in range(i,n):  #zada se kum
        print(" ",end=" ")
    for j in range(i+1,n):  #zada se kum
        print(" ",end=" ")
    for j in range(i+1):  #kum se zada
        print("*",end=" ")
    print()'''


#MAKING OF DIAMOND

n= int(input("enter the n :"))
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

    print()

