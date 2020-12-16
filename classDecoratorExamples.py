class Student:
    def __init__(self,s1,s2,s3):
        self.studId=s1
        self.studName=s2
        self.grades=s3
    # constructor overloading - not allowed in python
    @classmethod
    def createStudent(cls,s1,s2,s3,s4):
        fullName=s2+s3
        stud=cls(s1,fullName,s4) # creating an object of class cls ; cls is pointing to Student
        return stud

    @classmethod
    def createStudentUsingJson(cls,obj):
        stud=cls(obj["studId"],obj["studName"],obj["grades"])
        return stud

    @staticmethod
    def compareStudents(obj1,obj2):
        if(obj1.grades>obj2.grades):
            return 1
        else:
            if(obj1.grades<obj2.grades):
                return -1
            else:
                return 0


tom=Student(101,"Tom Hanks",10)
bill=Student.createStudent(102,"bill","gates",5)
george=Student.createStudentUsingJson({"studId":101,"studName":"George","grades":"d"})

res=Student.compareStudents(tom,bill)
res1=george.compareStudents(tom,bill)

print("Result1",res1)

print("Result",res)

g1=george.createStudentUsingJson({"studId":102,"studName":"G1","grades":"d"})
print(g1.studId)
print(george.studId)
# static factory pattern
