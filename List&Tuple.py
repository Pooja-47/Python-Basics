##LIST:>>>
"""lists are like arrays in python but they can store values of different datatypes."""

marks=[50, 60, 70, 80, 90]    #list declaired
print(marks)
Student=["Sanjay", 90, 18, "Jaipur"]
print(Student)

"""Likewise string we can access value of a particular index in list."""
print(marks[4])

"""Unlike strings we can modify the string."""
marks[4]=70
print(marks)  #gives the modified list.

print(len(marks))  #returns the length of list like string.
print(len(Student))

"""Likewise string slicing is allowed in lists also."""
print(marks[2:4])          #Ending indx is not included.
print(Student[0:4])        #same as [ :4]
print(marks[2:])          #same as [2:len(marks)]
print(Student[-4:-1])      #-ve indexing from last as-1

"""There are some functions which are list specific known as list methods."""
"""These methods make changes in the original list while in strings changes were made in a new string:"""
list=[1,5,3,4,6]

list.append(9)   #adds an element at the end.::[list.append(element)]
print(list)

list.sort()      #rewrites the list in ascending order.::[list.sort()]
print(list)

list.sort(reverse=True)     #descending order.::[list.sort(reverse=True)]
print(list)

"""Sorting is possible for strings(words,) also in lists.
> It sorts according to the alphabetical order"""

list1=["aa","Ankit","boy","girl"]
list1.sort()
print(list1)

list1.reverse()  #reverse the list.
print(list1)

list.insert(4,3) #to add element at particular index. and then returns the original list with new element inserted.
print(list)

list1.remove("aa") #removes a  given value that occurs first.
print(list1)

list.pop(3)   #removes the value from given index(3).
print(list)


##TUPLES>>>>>

tup=()  #Null tup is valid
print(tup)
print(type(tup))

tup1=("risky",)   #for single value use of , is must othwise it gives the wrong datatype.
print(tup1)
print(type(tup1))

tup2=(1,2,3,3,3,35)   #likewise string and list slicing as well as accessing values is possible.
print(tup2[3])
print(tup2[-3:-1])

"""Tuple methods :"""
print(tup2.index(3))   #returns the index of given element at which it first occurs.::{tup.index(el)}
print(tup2.count(3))    #returns no. of times given element occurs.::{tup.count(el)}


#QUESTIONS::::
#Q1:
F1=str(input("1st movie:"))
F2=str(input("2nd movie:"))
F3=str(input("3rd movie:"))

print(F1)
print(F2)
print(F3)

list3=[0,1,2]
list3[0]=F1
list3[1]=F2
list3[2]=F3

print(list3)


#Q2::
list5=[1,2,3,2,1]
copy_list5 = list5.copy()
copy_list5.reverse()
if(copy_list5 == list5):
    print("Palindrome")
else:
    print("Not a palindrome")
    

#Q3::
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))

#Q4::
list6=["C","D","A","A","B","B","A"]
list6.sort()
print(list6)

