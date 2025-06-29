#DICTIONARIES:::

info={
    "key" : "value",
    "name" : "Pooja",
    "cgpa" : 9.5,
    "marks":[90,98,97],
}
print(info)
"""In dictionaries we can store values of any datatype (int,float,str,) even lists and tuples also.
Dict. stores values like in real life dict. stores meanings of words.
In dictionaries there is no index as strings,lists,tuples etc.[unordered]
Mutable.
Keys cant be repeated.
Accessing and assigning new value to a key & creating new key:value pair is possible.
Null dict can also be created."""

print(info["name"])
info["cgpa"]=9.6
print(info)

null_dict={}
print(null_dict)

#NESTED DICTIONARY:;
"""Use a key as dict name"""
student={
    "name":"Priya",
    "subjects":{"chem":97,
                "phy":98,
              "maths":100
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

#DICTIONARY METHODS:;
 
print(info.keys()) #returns all the keys::[dict.keys()],do not return the nested keys.
print(student.keys())

print(info.values()) #returns all values::[dict.values()].
print(student.values())

print(info.items()) #returns the dict itself in tuple form.

"""There are two methods to access value in dict."""
print(info["name"])
print(info.get("name"))

"""Both returns same value but if we bymistake mention a key which is not present in dict then

[info.get("key")]  :: will return none whereas;
{info["key"]}      :: will give error.  

and when compiler gets error in any statement it stops there
and do not execute further even the remaining code is fully correct."""

info.update({"city":"jaipur"})
print(info)

info["city"]="udaipur"
print(info)

new_dict={"name":"priya","age":16} #for same keys values are overwritten new key is not formed.
info.update(new_dict)
print(info)

print(list(info.items())) #typecasting
print(tuple(student))
print(tuple(student.items()))
print(len(info))
print(list(student["subjects"]))
print(tuple(student))
print(len(info))
print(len(list(info.items())))


#SETS::::

"""Each element is unique and immutable.;
SET is mutable."""
price={600,680,"costly","cheap",99.99,True,(3,4)}
print(price)
print(type(price)) #unordered results.

""" we can store int,float,str,tuple in sets as they are immutable but
 not list & dict they are mutable."""

collection ={44,44,26,"hello","hello"} #ignores the repeated values.
print(collection)
print(len(collection))  # it also ignores the repeated values.

#SET METHODS::
collection.add(9) #adds a value to set {set.add(el):::adds el to set.}
print(collection)

price.remove(680) #removes an element {set.remove(el)}
print(price)

"""price.clear()  #makes a set empty.
print(price)"""

#print(collection.pop())  #it removes random values from set.

print(price.union(collection)) #returns comination of two sets in a new set.

print(price.intersection(collection)) 
#returns common values of two sets in a new set. 
#if no common values return null set.

#PRACTICE QUESTIONS::
#Q1:
dict={"table":["a piece of furniture","list of facts and figures"],
      "cat":"a small animal"}

print(dict)

#Q2::
set={"python","java","c++","python","javascript","java","python","java","c","c++","c"}
print("no. of classrooms required=",len(set))

#Q3::

subjects={}

subjects[str(input("S1:"))]=99
subjects[str(input("S2:"))]=97
subjects[str(input("S3:"))]=100

print(subjects)

#Q4::

values={(9,9.0)}    #values={9,"9.0"} ; values={("int",9),("float",9.0)}
print(values)

values={9,9.0} #9



