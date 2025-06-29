str1="Pooja Kanwar"   #We can use " ",' ',''' ''' to write a string.   
str2="Code in Python"
print(str1,str2)

str="This is a string. We write it in Python."
print(str)

"""To print the string sentences in different lines we use escape sequence characters like:
Tab:\t ;it gives a tab space.
Next line:\n ;it takes to the next line"""

str="My name is Pooja.\nI'm learning Python."
print(str) 

#<<<<<Basic operations on string:>>>>>

#Opn1>>Concatentaion: addn of two strings
str1="Pooja "
str2="Kanwar."
print(str1+str2)

#Opn2>length of string: len(str)>>>::
str3="I am a student"
print(len(str3))  #lenth includes all special chars. and spaces.

str4="<Pooja"
print(str4)

#Indexing>>: position of a char. in string strts from 0.>>>:::
str0="This is in Python"
print(str0[2]) #str[index] gives the char. present on the particular position 

"""str0[5]="-" string does not support assigning values.
print(str0) It will give error. """
#we cant modify the chars. we can only acces them.

#Slicing>>: access the part of string.>>>>>:::
str5="Apna College"
print(str5[0:len(str5)]) #str5[0:]
print(str5[1:4]) #1 is included and 4 is not.
print(str5[0:5]) #str5[:5]
print(str5[-3:-1])  #-ve indexing starts from last char(-1)

#<<<<String functions>>>>>
str6="i am a coder."
print(str6.endswith("er."))  #str.endswith("substr")::shesks if string ends with substr or not[true or false]
print(str6.capitalize()) #do not make changes in main str.capitalize()::capitalizes the first letter.
str4=str6.capitalize()
print(str4)
print(str4.replace("coder","programmer")) #str.replace("old","new")::replaces the older word with new.
print(str6.find("coder")) #str.find("word")
print(str6.count("a"))  #str.count("word"):: counts the no. of time word occurs.

#Questions>>>>>
#Q1:
str8=input("Your name is:")
print(len(str8))

#Q2:
money="1000$"
print(money.count("$"))

