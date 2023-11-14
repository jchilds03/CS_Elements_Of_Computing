# File: Project1.py
# Student: Jordan Childs    
# UT EID: jac22829
# Course Name: CS303E
# 
# Date: 10/01/2022
# Description of Program: Use course info to create a Grade calculator

from math import *

#Error Messages
HW_ERROR_MESSAGE = "  Grade must be in range [0..10]. Try again."

EXAM_ERROR_MESSAGE = "  Grade must be in range [0..100]. Try again."

PR_ERROR_MESSAGE = "  Grade must be in range [0..100]. Try again."

#computes homework average
def compute_hw_avg(x1, x2, x3):
    return 10 * (x1 + x2 + x3) / 3

#computes projects average
def compute_pr_avg(x1, x2):
    return (x1 + x2) / 2

#computes exam average
def compute_exam_avg(x1, x2):
    return (x1 + x2) / 2

#computes course average
def compute_avg_grade(x1, x2, x3):
    return (x1 * .3) + (x2 * .4) + (x3 * .3)

#computes letter grade
def compute_letter_grade( x ):
    if(x >= 90):
        return "A"
    elif(x < 90 and x >= 80):
        return "B"
    elif(x < 80 and x >= 70):
        return "C"
    elif(x < 70 and x >= 60):
        return "D"
    else:
        return "F"

#prints grade report
def print_grade_report(s, h, p, e, avg, let):
    print()
    print("Grade report for:", s)
    print("   Homework average (30% of grade):", format(h, "0.2f") )
    print("   Project average (30% of grade):", format(p, "0.2f") )
    print("   Exam average (40% of grade):", format(e, "0.2f") )
    print("   Student course average:", format(avg, "0.2f") )
    print("   Course grade (CS303E: Fall, 2022):", let)
    print()

def main():

    while True:

        student = input( "Enter the student's name (or \'stop\'): ")

        #checks if stop is entered
        if( student == 'stop'):
            print("Thanks for using the grade calculator!  Goodbye.")
            print()
            break

        #if stop not entered began asking user for inputs
        else:
            #Input Homework Grades with Parameters:
            print()
            print("HOMEWORKS:")
            hw1 = int( input("  Enter HW1 grade: ") )
            while(hw1 < 0 or hw1 > 10):
                print(HW_ERROR_MESSAGE)
                hw1 = int( input("  Enter HW1 grade: ") )
                

            hw2 = int( input("  Enter HW2 grade: ") )
            while(hw2 < 0 or hw2 > 10):
                print(HW_ERROR_MESSAGE)
                hw2 = int( input("  Enter HW2 grade: ") )
                

            hw3 = int( input("  Enter HW3 grade: ") )
            while(hw3 < 0 or hw3 > 10):
                print(HW_ERROR_MESSAGE)
                hw3 = int( input("  Enter HW3 grade: ") )

            #Input Project Grades with parameters
            print()
            print("PROJECTS:")
            pr1 = int( input("  Enter Pr1 grade: ") )
            while(pr1 < 0 or pr1 > 100):
                print(PR_ERROR_MESSAGE)
                pr1 = int( input("  Enter Pr1 grade: ") )
                

            pr2 = int( input("  Enter Pr2 grade: ") )
            while(pr2 < 0 or pr2 > 100):
                print(PR_ERROR_MESSAGE)
                pr2 = int( input("  Enter Pr2 grade: ") )

            #input Exam Grades with Parameters
            print()
            print("EXAM:")
            ex1 = int( input("  Enter Ex1 grade: ") )
            while(ex1 < 0 or ex1 > 100):
                print(EXAM_ERROR_MESSAGE)
                ex1 = int( input("  Enter Ex1 grade: ") )
                

            ex2 = int( input("  Enter Ex2 grade: ") )
            while(ex2 < 0 or ex2 > 100):
                print(EXAM_ERROR_MESSAGE)
                ex2 = int( input("  Enter Ex2 grade: ") )
                
            #Set Function outputs to variables
            hw_avg = compute_hw_avg(hw1, hw2, hw3)
            pr_avg = compute_pr_avg(pr1, pr2)
            ex_avg = compute_exam_avg(ex1, ex2)
            stu_avg = compute_avg_grade(hw_avg, ex_avg, pr_avg)
            letter = compute_letter_grade(stu_avg)

            #print grade report function
            print (print_grade_report(student, hw_avg, pr_avg, ex_avg, stu_avg, letter) )

main()
