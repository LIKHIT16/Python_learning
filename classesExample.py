#classes, objects, inheritance,abstraction,encapsulation,polymorphism, decorators

class Shape:
    #class var - shared by all the objects; one copy for all the objects
#   #instance var -- for each and every obj exclusively
    ctr=10 # class var
    def __init__(self,s1,s2):
        #self - this - object on which this method is being called
        self.side1=s1
        self.side2=s2
    def printDetails(self):
        print("Side 1",self.side1)
        print("Side 2", self.side2)

square1=Shape(10,10)
square1.printDetails() # Shape.printDetails(square1)
print("The value of ctr is", Shape.ctr)
print("The value of ctr is", square1.ctr)
rect1=Shape(22,33)
rect1.printDetails()
print("The value of ctr is", rect1.ctr)
Shape.ctr=1000
#rect1.ctr=1000 # adding a new instance field which is ctr
print("The value of ctr with square1 is", square1.ctr)
print("The value of ctr with rect1 is", rect1.ctr)
rect1.area=100

# public -- accessible everywhere
# private -- accessible only within the class; not by the objects of that class also
# protected -- accessible within the class; accessible by the derived classes

class Example:
    def __init__(self):
        self.publicVar=100
        self.__privateVar=200
        self._protectedVar=300

    def modifyValues(self):
        self.publicVar+=1
        self.__privateVar+=1
        self._protectedVar+=1

    def printDetails(self):
        print("Public var",self.publicVar)
        print("Private var", self.__privateVar)
        print("Protected var", self._protectedVar)

obj1=Example()
obj1.modifyValues()
obj1.printDetails()
obj1.publicVar=1000
obj1._protectedVar=3000
#obj1.__privateVar=2000
obj1.printDetails()
del obj1

i=10
j=100
if(i <j):
    print("The value of i is",i)
    print("The value of j is", j)
    temp=i
    i=j
    j=temp
    print("The swapped values are")
    print("The value of i is", i)
    print("The value of j is", j)


class Emp:
    def __init__(self,p1,p2,p3,p4):
        self.empId=p1
        self.empName=p2
        self.__salary=p3
        self.__bonus=p4
    # getter and setter functions for the private function
    def getSalary(self):
        return self.__salary
    def setSalary(self,value):
        if(value>0):
            self.__salary=value
        else:
            raise ValueError("Salary cannot be less than zero")
    @property
    def Bonus(self):
        return self.__bonus
    @Bonus.setter
    def Bonus(self,value):
        if(value>0):
            self.__bonus=self.__salary*value
        else:
            self.__bonus=self.__salary*.3


tom=Emp(101,"Tom",1000,0)
print("Salary",tom.getSalary())
print("Bonus",tom.Bonus) # Bonus.getter
tom.Bonus=100 # Bonus.setter
print("Modified Bonus",tom.Bonus)

try:
    tom.setSalary(-1500)
    print("Salary",tom.getSalary())
except ValueError:
    print("Salary Without modification", tom.getSalary())



