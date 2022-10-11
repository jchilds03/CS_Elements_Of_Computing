# File: Student.py
# Student: Jordan Childs
# UT EID: jac22829
# Course Name: CS303E
# 
# Date: 10/08/22
# Description of Program: Use classes to make a student class with name and exam scores as objects.

#create Student class, with parameters

ERROR = "Some exam grades are not available."

class Student:

    def __init__(self, name, Exam1 = None, Exam2 = None):
        self.__name = name
        self.__Exam1 = Exam1
        self.__Exam2 = Exam2
        
    def getName(self):
        return self.__name

    def getExam1Grade(self):
        return self.__Exam1 

    def setExam1Grade(self, Exam1):
        self.__Exam1 = Exam1
    
    def getExam2Grade(self):
        return self.__Exam2

    def setExam2Grade(self, Exam2):
        self.__Exam2 = Exam2

    def getAverage(self):
        if( self.__Exam1 == None or self.__Exam2 == None):
            print(ERROR)
        else:
            return( (self.__Exam1 + self.__Exam2) / 2)

    def __str__(self):
        return "Student:  " + str(self.__name) + \
            "\n  Exam 1: " + str(self.__Exam1) + \
            "\n  Exam 2: " + str(self.__Exam2)

"""#Run in main function
def main():

    #Susie Object
    susie = Student("Susie Q.")
    print( susie )

    print( susie.getName() )

    #Set Susie's 1st Grade
    print(susie.getExam1Grade() )
    susie.setExam1Grade(100)
    print(susie.getExam1Grade())
    print(susie)

    #Set Susie's 2nd Grade
    susie.setExam2Grade(87)
    print(susie)

    #print out average for Susie
    print(susie.getAverage() )

    #Create Bob object
    bob = Student("Bobbie D.", 47, 92)
    print(bob)
    print(bob.getAverage())

    #Create Clark object
    clark = Student("Clark K.", 100)
    print(clark)

main()"""

