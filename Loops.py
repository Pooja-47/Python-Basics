"""Loops are used to run a program repeatedly . For this purpose we have two funs in python:
while and for loop ."""

#WHILE LOOP::

i=1       #iterate declaired.
while i<=5:     #condition must terminate at a point. othw it will run infinitely.
    print("hello")
    i+=1        #one time condn check(one output) is one iteration.
print("loop ended")

j=1
while j<=151:
    print("Jai Shree Ganesh",j)
    j+=1
print("loop ended")

x=1000
while x>=1:
    print(x)
    x-=1
print("loop ended")

#QUESTIONS:::
#Q3:
n=int(input("n:"))
a=1
while a<=10:
    print(n*a)
    a+=1
print("loop ended")

#Q4:
k=1
while k<=10:
    print(k**2)
    k+=1

list=[1,4,9,16,25,36,49,64,81,100]
h=0
while h<len(list):
    print(list[h])
    h+=1

#Q5:
tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("x:"))
idx=0
while idx<len(tup):
    if(tup[idx]==x):
        print("found at idx",idx)
    idx+=1

#Break & Continue:::
u=1
while u<=5:
    if(u==4):
        break  #stops when u=4
    print(u)
    u+=1

f=1
while f<=5:
    if(f==4):
        f+=1
        continue #jumps to next value skips 3
    print(f)
    f+=1


#FOR LOOP:::
veggies=["tomato","potato","brinjal"]
for sabji in veggies:    #We use for loop for traversing string,list,tuple. 
    print(sabji)
else:
    print("end")

"""for sabji in veggies:
    if(sabji=="potato"):
        print("found")
        break
    else:
        print("end")"""


#QUESTIONS::
#Q1:
nums=[1,4,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)
else:
    print("END")


#Q2:
tupl=[1,4,9,16,25,36,49,64,81,100]
x=int(input("x:"))
for el in tupl:
    if(el==x):
        print("el found")
        break
else:
    print("not")



#RANGE()::
print(range(6))

seq=range(9)
for el in seq:
    print(el)

for el in range(10):
    print(el)

for i in range(1,99,5):    #range(start,stop,step)
    print(i)

#QUESTIONS::
#Q1:
for i in (range(1,101,1)):
    print(i)

#Q2:
for j in (range(100,0,-1)):
    print(j)

#Q3:
n=int(input("enter number:"))
for h in range(1,11):
    print(n*h)

#Qs1:
a=int(input("a:"))
sum=0
l=1
while l<=a:
    sum=l+sum
    l+=1
print(sum)


#Qs2:
n=int(input("n:"))
fact=1
for a in range(1,n+1):
    fact*=a
print(fact)
    

