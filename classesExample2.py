class Shape:
    #class var - shared by all the objects; one copy for all the objects
#   #instance var -- for each and every obj exclusively
    ctr=10 # class var
    def __init__(self,s1,s2):
        #self - this - object on which this method is being called
        self.side1=s1
        self.side2=s2
        self._protectVar=1000
    def printDetails(self):
        print("Side 1",self.side1)
        print("Side 2", self.side2)

class Cuboid(Shape):
    def __init__(self,p1,p2,p3):
        self.side3=p3
        #Shape.__init__(self,p1,p2)
        super().__init__(p1,p2)

    def display(self):
        #print("Side 1",self.side1)
        #print("Side 2", self.side2)
        super().printDetails()
        #Shape.printDetails(self)
        print("ProtectVar",self._protectVar)
        print("Side 3", self.side3)

c1=Cuboid(10,20,30)
c1.display()
c1.printDetails()


# simple Cuboid(Shape)
# multilevel inheritance GrandDad ; Dad(GrandDad); Child(Dad)
# multiple inheritance Dad, Mom; Child(Dad,Mom)
# Java, .net - allow multiple inheritance super(); ambiguity

class Colour:
    def __init__(self,hexaDecCode):
        self.myColour=hexaDecCode
    def printDetails(self):
        print("Colour:",self.myColour)
    def changeColur(self,p1):
        self.myColour=p1

class Polygon(Shape,Colour):
    def __init__(self,s1,s2,s3):
        Shape.__init__(self,s1,s2)
        Colour.__init__(self,s3)

    def display(self):
        self.changeColur("orange")
        Colour.changeColur(self,"blue")
        Shape.printDetails(self)
        Colour.printDetails(self)
    def area(self):
        print("Area =",self.side1*self.side2)


poly1=Polygon(10,20,"pink")
poly1.display()
poly1.area()
print("*"*30)
poly1.changeColur("cyan")
poly1.display()

# polymorphism
# overloading --
# multiple functions but all will have the same name with different parameter sign
# parameter sign -- number of args, order of args, type of args
# overloading is not supported in python


class Student:
    def __init__(self,p1,p2):
        self.studId=p1
        self.marks=p2
    def calcAvg(self):
        tot1=0
        for i in range(len(self.marks)):
            tot1+=self.marks[i]
        print("Average",tot1/len(self.marks))
    # overwrite
    def calcAvg(self,weightage):
        tot1 = 0
        for i in range(len(self.marks)):
            tot1 += (self.marks[i]*weightage[i])
        print("Average", tot1 / len(self.marks))


george=Student(101,[10,20,30])
#george.calcAvg();# 20
george.calcAvg([5,5,5]) # 100
i=10
i=20
print(i)

# overriding
# Inheritance
# same member with the same name and same sign

class Base:
    def display(self):
        print("Base method called")

class Derived(Base):
    def display(self):
        print("Derived method called")

derObj1=Derived()
baseObj1=Base()
baseObj1.display()
print("*"*30)
derObj1.display()

