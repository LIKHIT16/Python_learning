def wrapperFunc(f1):
    def innerFunc(*positionalArgs,**Dictkeywordargs):
        if(positionalArgs[1] ==0):
            myList1=list(positionalArgs)
            myList1[1]=1
            tuple1=tuple(myList1)
            res = f1(*tuple1, **Dictkeywordargs)
        else:
            res=f1(*positionalArgs,**Dictkeywordargs)
        return res
    return innerFunc

# custom decorators
@wrapperFunc
def divTwoNumbers(p1,p2):
    print("Division is",p1/p2)
    return p1/p2

@wrapperFunc
def mulThreeNumbers(p1,p2,p3):
    print("Multiplication:",p1*p2*p3)
    return p1*p2*p3

mulThreeNumbers(10,0,3)

# multiple decorators for the same func



divTwoNumbers(10,0) # 10
# divTwoNumbers will be sent as a parmeter to wrapperFunc decorator and wrapperFunc would get executed
# it will also trigger the call to the innerFunc(10,0)

'''
innerF1=wrapperFunc(divTwoNumbers)
r1=innerF1(10,2)
print("R1=",r1) #5

r1=innerF1(10,0)
print("R1=",r1) # 10

'''
