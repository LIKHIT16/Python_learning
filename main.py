i = 10
i = 10.5
i = "hello"

print("The value of i is", i) #"hello"
j = 10
print("i=", i, " j=", j)

'''
This is a multi line comment
'''

# int float complex
i=10
i=10.5
i=3.14j

# string
#"good morning"
#"0123456789
str1 = "good morning"
print(str1)
print(str1[0]) # g
print(str1[2:5]) #  "od "
print(str1[2:]) #  "od morning"
print(str1[:5]) #  "good "
print(str1*3) # 3 times good morning
print(str1 + "Citi")

str1 = str1.upper()
print(str1)
print(str1.title())

# upper lower title capitalise
str1.isdigit() # false

#index
#malayalam
#012345678
str1 = "malayalam"
# print the various pos where a is there in the string
# traverse through the string
pos1=str1.index("a") # return the pos of the first occurence of the substring in the given string; 1
'''
while(pos1 >= 0):
    print(pos1)
    pos1=str1.index("a",pos1 + 1)
'''
pos1=str1.find("a") # return the pos of the first occurence of the substring in the given string; 1

while(pos1 >= 0):
    print(pos1)
    pos1=str1.find("a",pos1 + 1)

print("Position of z in str1",str1.find("z"))
print("Position of l in str1",str1.find("l",3,5))  # -1
print("Position of y in str1",str1.find("y",0,4)) # -1;4 ;
str1="malayaLAm"
print(len(str1)) #9
print(max(str1)) #  y
print(min(str1)) #  A
# A - 65
# a - 97

print(str1.startswith("mal")) # true
print(str1.startswith("lay",2)) # true

str1="good morning Citi"
print(str1.split())
print(str1.split("o"))
print(str1.split(" ", 1))

list1=[10,20,30,40,50]
list2=["apple","strawberry","pineapples"]
list3=[101,"Sara",67.67,True]
print(list1)
print(list1[2:4]) # [30,40]
print(list1[3]) # 40
print(list1[3:]) # [40,50]
print(list1[:3]) # [10,20,30]

# list - mutable
list1[3]=1000
print(list1) #[10,20,30,1000,50]

list1=[10,20,30,40,50]
list1[2:4]=[100]
print(list1)

list1=[10,20,30,40,50]
list1[2:4]=[100,200,300,400,500]
print(list1)

list1=[10,20,30,40,50]
list1[2:4]=["hello",False]
print(list1)

list1=[10,20,30,40,50]
del list1[2]
print(list1)

list1=[10,20,30,40,50]
list1.remove(50)
print(list1)

list1=[10,20,30,40,50]
print("Popped out element:",list1.pop()) #50
print(list1)
#IndexError: pop index out of range
list1=[10,20,30,40,50]
print("Popped out element:",list1.pop(1)) # 20;
print(list1)
# 0 1 2 3 4
#-5-4-3-2-1
list1=[10,20,30,40,50]
print("Popped out element:",list1.pop(-3)) # 30
print(list1)

list1=[10,20,30,40,50]
print(list1[-3]) # 30

list1=[10,20,30,40,50]
list1.append(60)
print("Appended list",list1) #[[10,20,30,40,50,60]

# insert at a particular pos
list1.insert(3,35)
print(list1) # [10,20,30,35,40,50,60]

list1=[1,2,3,1,3,1]
print(list1.count(1))

print(list1.index(1))

list1=[10,20,30,40,50]
list1.append([60,70])
print("Appended list",list1) # [10,20,30,40,50,[60,70]]

list1=[10,20,30,40,50]
list1.extend([60,70])
print("Appended list",list1) # [10,20,30,40,50,60,70]

list1.extend(list2)
print(list1)

list1=[10,30,20,40,50]
list1.sort()
print(list1)

list1.reverse()
print(list1)

list1=[101,20,10,111,25,99]
list1.sort()
print(list1) #[10,20,25,99,101,111]
'''
list1=[101,20,10,111,True,"hello"]
list1.sort()
print(list1) # error
'''

list1=[101,20,10,111,True]
list1.sort()
print(list1) # [True, 10,20,101,111]

list2.sort()
print(list2) #

# Tuples
# enclosed in paranthesis
# immutable

tuple1=(10,20,30,40,50)
print(tuple1)
print(tuple1[0]) # 10
print(tuple1[2:4]) # 30,40

# tuple1[0]=1000; error

#del tuple1[0]

del tuple1 # successful

tuple1=(1,2,3,4,5)
# use cases
# gender =("M","F","O")
tuple2=(1,"M",77)
print(tuple2)

list10=[100]
print(list10)
tuple2=(10)
print(tuple2)

# dictionary
# object in OOPs
# key value
# {}
# key -- immutable datatype(number, string, tuple)
# value -- any of datatypes
# mutable


dict1={"empId" : 101, "empName" : "Sara", "salary":67.89 }
print(dict1)
print(dict1["empId"]) #101

dict1["empId"]=999
print(dict1)
dict1["location"]="Pune"
print(dict1)

del dict1["salary"]
print(dict1)

'''
del dict1 #remove the entire dict
dict1.clear()
'''

keyList=dict1.keys()
print(keyList)

for key1 in keyList:
    print(key1, end=";")
print()

for i in range(len(list1)):
    print(list1[i], end= " ")
print()

valueList=dict1.values()
for value1 in valueList:
    print(value1, end=";")
print()

itemsList=dict1.items()
print(itemsList)
for (key1,value1) in itemsList:
    print(key1," : ", value1) # EmpId: 101; EmpName: "sara"
print()

dict2={1:101,"empName":"Tara"}
#dict3={["grades"]:[10,20,30],"studId":109} # error list is mutable which is not allowed
dict4={"empId":"101","empName":"Sara","salary":5555,"empId":777,"empId":777}
print(dict4) ;# {777, Sara,5555}

print(dict4.get("empId",666))
print(dict4.get("deptId","Not Assigned"))

dict4.setdefault("empId",555)
dict4.setdefault("deptId","D1")
print(dict4)
dict4["empId"] =555
dict4["deptId"]="D1"

# list of dicts
empArr=[{"empId":101,"empName":"Sara"},{"empId":102,"empName":"Tara"},{"empId":103,"empName":"Lara"}]

key1=("studId","studName","marks")
dict5=dict.fromkeys(key1)
print(dict5)

dict6=dict.fromkeys(key1,101)
print(dict6)

value1=(101,"sara",88)
dict7=dict.fromkeys(key1,value1)
print(dict7)
dict7["studName"]="sara"

# copy ; shallow copy; deep copy

fruits=["apples","mangoes","guavas"]
myFruits=fruits # reference
myFruits[0]="pineapples"
print("Fruits",fruits)
print("MyFruits",myFruits)
#list ; references
# tuples ; copy
#dict -- references

empDict={"empId":101,"empName":"sara"}
empDict2=empDict
empDict2["empId"]=777
print("EmpDict",empDict)
print("EmpDict2",empDict2)

empDict3=empDict2.copy()
empDict3["empId"]=333
print("EmpDict3",empDict3)
print("EmpDict2",empDict2)

# create a list which is a copy of another list











