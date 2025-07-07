#Q1:To check if a number is odd or even?

"""Let our number is num"""

num=int(input("Enter any number:"))
print("num=",num)

if(num%2==0):
    print("Entered number:",num,"is EVEN.")
else:
    print("Entered number:",num,"is ODD.")

#Q2:Maximum of two numbers-
"""Let the two numbers be num1 and num2"""

num1=int(input("Enter any number:"))
num2=int(input("Enter second number:"))

if(num1>num2):
    print(num1,"is maximum.")
else:
    print(num2,"is maximum.")

#Q3:Minimum of two numbers-
"""Let the two numbers be N1 and N2"""

N1=int(input("Enter any number:"))
N2=int(input("Enter second number:"))

if(N1<N2):
    print(N1,"is minimum.")
else:
    print(N2,"is minimum.")

#Q4:Check prime number-
"""Let the number is a"""

a=int(input("Enter a number:"))
for i in range(2,a):
    if(a%i==0):
        print(a,"is not prime number.")
        break
else:
    print(a,"is a prime number.")

#Q5:Printing pyramid patterns-

#A::
j="*"
for i in range(1,6):
    print(j)
    j+="*" 

#B::
rows=5
for i in range(1,6):
    print(" "*(rows-i)+"*"*i)

#C::
rows=5
b="***"
for i in range(1,3):
    print(" "*(rows-i)+"*"*i)
for i in range(3,6):
    print(" ",b)
    b+="*"

#Q6:Interchange first and last elements in list

list=[1,2,3,4,5,]
list[0]=list[len(list)-1]
list[len(list)-1]=1
print(list)







        

        

    







