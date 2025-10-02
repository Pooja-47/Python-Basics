#1-Take input from user:
name=str(input("Enter your name:"))
print(name)

#2-Table print:
num=int(input("Enter any number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
    i+=1

#3-Grade calculater:
marks=int(input("Enter marks:"))
if(90<=marks<=100):
    print("A")
elif(80<=marks<90):
    print("B")
elif(70<=marks<80):
    print("C")
elif(60<=marks<70):
    print("D")
elif(0<=marks<60):
    print("F")
else:
    print("Out of range")

#4-Leap year checker:
year=int(input("Enter the year:"))
if((year%4==0 or year%100!=0)and year%400==0):
    print(year,"is leap year.")
else:
    print(year,"is not leap year.")

#5-Triangle classifier:
s1=int(input("Enter the side of triangle:"))
s2=int(input("Enter the side of triangle:"))
s3=int(input("Enter the side of triangle:"))
if(s1==s2==s3):
    print("Equilateral triangle.")
elif(s1==s2 or s2==s3 or s1==s3):
    print("Isosceles triangle.")
else:
    print("scalene triangle.")

#6-FizzBuzz test:
for num in range (1,101):
    if(num%3==0 and num%5==0):
        print("FizzBuzz")
    elif(num%3==0):
        print("Fizz")
    elif(num%5==0):
        print("Buzz")
    else:
        print(num)

#7-Prime number cheker:
num=int(input("Enter any number:"))
for i in range(2,num):
    if(num%i==0):
        print("Not prime")
        break
else:
    print("prime")

#8-Palindrome Checker:

word=str(input("Enter a string:"))
reverse=word[ : :-1]   #slicing
if(reverse==word):
    print("Yes,it is Palindrome.")
else:
    print("No,it is not Palindrome.")

#9-list questions:
"""Reverse list"""
info=["Pooja","second year","ACEIT","Jaipur"]
marks=[98,99,89]
print(info)

info.reverse() #makes changes in original list
print(info)
reversed_info = list(reversed(info)) #creates new list
print(reversed_info)



"""Sort list"""
info.sort()
print(info)
marks.sort()
print(marks)

"""Merge list"""
print(info+marks)

"""Most frequent element in list"""
from collections import Counter
list1=[1,3,4,45,44,54,44,66,44]
print(list1)
res=Counter(list1)
num=res.most_common(1)[0][0]
print(num)

def most_freq():   #another approach
    nums=[23,65,56,56,77,56,89,56]
    count=0
    num=nums[0]
    for i in nums:
        occ=nums.count(i)
        if(occ>count):
            count=occ
            num=i
    return num
print(most_freq())


#10-Star Patterns:
for i in range(5):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,5):
        print("*",end=' ')
    print()

for i in range(5):
    for j in range(i,5):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()

for i in range(5):
    for j in range(i):
        print("",end=' ')
    for j in range(i,5):
        print("*",end=' ')
    print()

for i in range(5):
    for j in range(5):
        print("*",end=' ')
    print()

for i in range(4,0,-1):
    for j in range(i):
        print("#",end=" ")
    print()

for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()

#11-String Reverse:
string=input('Enter any string:')
reverse=string[ : :-1]
print(reverse)

#12-Count vowels and consonants in strng:
sent=input("Enter the sentence:")
S=sent.lower()
print(S)
vowel=0
cons=0
for i in range(0,len(sent)):
    if(sent[i]!=' '):
        if(S[i]=='a'or S[i]=='e'or S[i]=='i'or S[i]=='o'or S[i]=='u'):
            vowel+=1
        else:
            cons+=1
print("Total vowels:",vowel)
print('Total consonants:',cons)

 #13-Duplicate String:
sen=input("Write anything:")
w=''
for i in sen:
    if i not in w:
        w+=i
print(w)

#14-Anagram checker
w1=input("Enter the word: ")
w2=input("Enter another word: ")
if sorted(w1)==sorted(w2):
    print("The two words entered are anagram.")
else:
    print("Not anagram.")

