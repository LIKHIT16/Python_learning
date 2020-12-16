list1=[10,20,30,40,50]
list2=list1.copy()
list3=[]
list3.extend(list1)
list4=[]
for i in range(len(list1)):
    list4.append(list1[i])
list5=list1[:]

def myFunc1(myList):
    myList.append(100)

myFunc1(list1)
print("List1",list1) #[10,20,30,40,50,100]

def myFunc2(**dictkeywordargs):
    for(k,v) in dictkeywordargs.items():
        print(k, " : ", v)
    print("*"*30)

myFunc2(s1=100,s2=10)
myFunc2(s2=99)
myFunc2(s3=30,s1=10,s2=20)

def myFunc3(p1):
    print("Value of p1",p1)
    def innerFunc():
        print("Value of p1 in the inner func",p1)
        if(p1==10):
            return True
        else:
            return False
    return innerFunc

f1=myFunc3(10)
res=f1()
print("Result=",res) # True
f1=myFunc3(100)
res=f1()
print("Result=",res) #False
#closure function example
def myFunc4(p1):
    def innerFunc1():
        #p1=10000 # local var of innerFunc1; not the param p1
        print("Value in the innerFunc2",p1)
        return p1
    return innerFunc1

re1=myFunc4(10)
re1(); #10


square1=0
def myFunc5(s1):
    # declare a new local var square1
    square1=s1*s1
    print("Value of square1 inside the function",square1) #100

myFunc5(10)
print("Square1",square1) # 0 global var

square2=0
def myFunc6(s1):
    # use the global var square2
    global square2
    square2=s1*s1
    print("Value of square2 inside the function",square2) #100

myFunc6(10)
print("Square2",square2) # 100 global var

# anonymous function
sumFunction=lambda p1,p2: p1+p2

print("Sum of 10,20 is",sumFunction(10,20))

