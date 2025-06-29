"""Functions are used to perform a same task many times in the same program as per requirement."""
 
def calc_sum(a,b):    #defined func name with parameters a,b.>>func definition
    sum=a+b           #task that has to be performed.
    print(sum)         #prints sum of parameters.
    return sum        #returns the value of sum.

calc_sum(4,5)         # func call with arguments 4,5
calc_sum(9,85)
calc_sum(78,85)

def say():           #functions with no parameters and return are possible.
    print("hello")

say()
say()
say()
say()

def averg(a,b,c,d):
    avg=(a+b+c+d)/4
    print(avg) 
    return avg

averg(3,4,5,6)
averg(9,8,6,4)


#QUES1:
list=["Pooja","2nd year",19,"Jaipur"]
movies=["Holiday","Housefull4","Juliet","Romeo","Welcome"]

def length(list):
    print(len(list))
    return length

length(list)
length(movies)

#Q2:
cities=["jaipur","udaipur","jodhpur","bikaner"]

def elem(list):
    for el in list:
        print(el,end=" ")   #end=" " to print output in same line.
        
elem(cities)
elem(list)

#Q3:

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
factorial(int(input("n:")))

#Q4:
def convert(usd_val):
    inr_val = usd_val*83
    print(usd_val,"USD=",inr_val,"INR")

convert(6)
convert(823)
convert(8345)
convert(83)

#Q5:
def evod(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")
evod(int(input("n:")))

#RECURSION::: fn calls itself repeatedly.
def show(n):
    if(n==0):
        return     #if condn true fn returns i.e. stops. and return condn is must.This cond is BASE CASE.
    print(n)
    show(n-1)      #recursive fn. func k andar fn ko call karna.

show(9)

def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n
print(fact(7))

#Q1:
def sum(n):
    if(n==0):
        return 0
    return sum(n-1) + n
print(sum(9))

#Q2:
alc=["a","b",9,8]
def elem(list,idx=0):
    if(idx==len(alc)):
        return
    print(list[idx])
    elem(list,idx+1)

elem(alc)
