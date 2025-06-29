"""#Q1:
f=open("practice.txt","w")
data=f.write("Hi everyone \nwe are learning I/O\nusing Java\nI like programming in Java")
print(data)"""

#xxQ2:
with open("practice.txt","r") as f:
    data=f.read()
new_data = data.replace("java","python")    
print(new_data)
with open("practice.txt","w") as f:
    f.write(new_data)

#Q3::
def check_for_word():
    word=" learning"
    with open("practice.txt","r") as f:
        data=f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("Not found")
check_for_word()
