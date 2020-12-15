def myFunc(p1,p2):
    "Return the floor division of the params"
    return p1//p2 # floor division

res=myFunc(10,3)
print("Result = ",res)

# required params, optional parameters; default values; variable length args

myFunc(20,6) # positional args
myFunc(p2=6,p1=20)  # keyword args
myFunc(10,p2=6) # first pos args followed by keyword args
#myFunc(p2=6,10)

def myFunc2(p1=2,p2 = 20):
    "Print all prime numbers between p1 and p2"
    for i in range(p1,p2):
        flag=0
        for j in range(2,(i//2 +1)):
            if(i%j == 0):
                flag=1
                break
        if( flag ==0):
            print(i)

myFunc2(10,30)
print("*"*30)
myFunc2(10)
print("*"*30)
myFunc2(p2=100,p1=50)
myFunc2()
myFunc2(p2=77)

# var length args
def myFunc3(*vartuple, **dictKeywordargs):
    print("The positional arguements in the function call are",vartuple)
    print("The keyword args are",dictKeywordargs)

myFunc3(1,2,3)
myFunc3(1)
myFunc3()
myFunc3(p1=10)
myFunc3(1,p1=10)

# example
def spliceFunc(myList,modifyPos,deleteCount,*insertTuple):
    # pop, del remove
    del myList[modifyPos:modifyPos+deleteCount]
    #for i in range(modifyPos,modifyPos+deleteCount):
    #    myList.pop(modifyPos)

    if(len(insertTuple) >0):
        for i in range(len(insertTuple)):
            myList.insert(modifyPos+i, insertTuple[i])
    return myList

# list,index,deleteCount, insertelements.....
list1=[10,20,30,40,50]
res=spliceFunc(list1,1,2) # [10,40,50]

print(res)
list1=[10,20,30,40,50]
res=spliceFunc(list1,1,2,99) # [10,99,40,50]
print(res)
list1=[10,20,30,40,50]
res=spliceFunc(list1,1,2,99,100) # [10,,99,100,40,50]
print(res)
list1=[10,20,30,40,50]
res=spliceFunc(list1,1,0,55,66) # [10,55,66,20,30,40,50]
print(res)






