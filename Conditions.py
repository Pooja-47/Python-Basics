"""In some programs we need to define an appropriate condition to get wanted output.
In Python we use the following conditional statements>>>>

if-elif-else

Syntax:
if(condition1):
    print(statement1)
elif(condition2):
    print(statement2) #we can use elif statements as many times we need.

-
-
-
else:
    print(statementN) #there is no condition check in else.else is always written at last.
  """



#Q1:
marks=int(input("marks="))
print("marks obtained =",marks)
if(marks>=90):
    print("Grade=A")
elif(90>marks>=80):
    print("Grade=B")
elif(80>marks>=70):
    print("Grade=C")
elif(70>marks>=60):
    print("Grade=D")
else:
    print("Fail")


#NESTING>>>>>
""" writing if statement in another if statement
#Syntax:
if(cond):
    if(cond1):
         print(s2)
     else:         #this else for 2nd if.
        print(s3)
else:
    print(s4)  #this else for first if. """

#Q2:
age=int(input("age is:"))
print("As per given age:",age)
if(age>=18):
    if(age>=90):
        print("Not allowed")
    else:
        print("allowed")
else:
    print("lack of driving lisence")


# PRACTICING QUESTIONS Q3:
a=int(input("enter any number:"))
print("a=",a)  
if(a%2==0):
    print("a is an even number.") 
else:
    print("a is an odd number.")

#Q4:
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

if(a>b and a>c):
    print("a is greatest")
elif(b>c):
    print("b is greatest")
else:
    print("c is greatest")

#Q5:
a=int(input("enter any number:"))
print("a=",a)
if(a%7==0):
    print("multiple of 7")
else:
    print("not a multiple of 7")

#Q6:
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=int(input("d:"))

if(a>b and a>c):
    print("a is greatest")
elif(b>c and b>d):
    print("b is greatest")
elif(c>d):
    print("c is greatest") 
else:
    print("d is the largest")   






