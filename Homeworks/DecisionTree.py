# File: DecisionTree.py
# Student: Jordan Childs
# UT EID: jac22829
# Course Name: CS303E
# 
# Date: 09/14/22
# Description of Program: Decision Tree for buying computer


def buy_decision():
    #create input variables
    age = int( input ("Please enter person's age: " ) ) 
    income = str( input("Person's income (High, Medium, Low): ") )
    student = str ( input("Is this person a student (Yes or No)? ") )
    credit = str (input("Does this person have good credit (Yes or No)? ") )
    
    #Group if-else checks by age
    #Develop check for <= 30
    if(age <= 30):
        if(student == "Yes"):
            print("This person will purchase a computer.")
        else:
            print("This person will not purchase a computer.")
    #check for 31-40
    elif(age > 30 and age < 41):
        print("This person will purchase a computer.")
    #check for 40
    else:
        if(credit == "No"):
            print("This person will purchase a computer.")
        else:
            print("This person will not purchase a computer.")

buy_decision()
