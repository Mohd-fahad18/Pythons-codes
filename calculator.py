operator=input("enter an operator(+-*/):")
num1=float(input("enter the 1 number:"))
num2=float(input("enter the 2 number:"))

if operator=="+":
    result = num1+num2
    print(result)

elif operator =="*":
    result = num1*num2
    print(result)

elif operator=="-":
    result = num1-num2
    print(result)

elif operator=="/":
    result = num1/num2
    print(result)

