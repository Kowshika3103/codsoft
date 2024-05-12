def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
print("please select operation 1.add 2.subtact 3.multiplication 4.division")
select=int(input("select operations from 1,2,3,4:"))
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
if select==1:
    print(num1,"+",num2,"=",add(num1,num2))
elif select==2:
    print(num1,"-",num2,"=",subract(num1,num2))
elif select==3:
    print(num1,"*",num2,"=",multiplication(num1,num2))
elif select==4:
    print(num1,"/",num2,"=",division(num1,num2))
else:
    print("Invalid input")
