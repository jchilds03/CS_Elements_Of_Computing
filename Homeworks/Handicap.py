# File: Handicap.py
# Student: Jordan Childs
# UT EID: jac22829
# Course Name: CS303E
#
# Date: 09/11/2022
# Description of Program: Calculate a Bowler's Handicap



def main():

    #step 1: Ask for bowler and bowler's scores
    print()
    name = input("Enter bowler's name: ")

    game1 = int( input("Enter Game 1: ") )
    game2 = int( input("Enter Game 2: ") )
    game3 = int( input("Enter Game 3: ") )
    print()

    #step 2: Calculate avg and handicap
    average = int( (game1 + game2 + game3) / 3 )
    handicap = int( (200 - average) * 0.80 )

    #step 3: print results using format statements
    print( "Handicap report for " + name + ":" )
    print( format("  " + name + "\'s average is: " + str(average), "40s"), \
        format("\n  " + name + "\'s handicap is: " + str(handicap), "40s") \
            + "\n" + \
                "\nIt's time to Bowl!")
    print()

main()
