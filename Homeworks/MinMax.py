# File: MinMax.py
# Student: Jordan Childs
# UT EID: jac22829
# Course Name: CS303E
# 
# Date: 09/19/2022
# Description of Program: MinMax program


def Min_Max():
    #Create variable num and enter an initial value.
    num = input( "Enter a an integer or \'stop' to end: ") 
    count = 0
    #integer_num = int(num)
    #Maximum_num 
    


    #check if num's initial value is stop
    if(count == 0 and num == 'stop'): # and num == 'stop')
        print("You didn't enter any numbers")

    else:
        while(num != 'stop'):
            num = input ("Enter an integer or \'stop\' to end: ") 
            #integer_num = int(num)
            count += 1
            #maximum_num = integer_num

            #Create if statement that will set maximum num equal to num if less than num else do something else
            #if(maximum_num >= integer_num):
            #    maximum_num = maximum_num
            #else:
            #    maximum_num = num
                
                
            #I can't figure out how to change my condition to allow for num to accept a string, 
            # after turning into an int.
            if( num == 'stop'):
                print("You entered " + str(count) + " numbers.")
            #    print("Maximum is: ", maximum_num)
                
Min_Max()





"""def Min_Max():

    num = input("Enter an integer or \'stop\' to end: ")
    stop_now = False


    while(stop_now == False):

        if(num == "stop"):
            stop_now = True
            print("You didn't enter any numbers")
    
        else:
            while(num != "stop" ):
                num = input("Enter an integer or \'stop\' to end: ")
                #int_num = int(num)

                for num in range("stop"):
                    print(num)

Min_Max()








def Min_Max():
    #create input variable, that counts number of inputs
    guess = input( "Enter an integer: ")

    #store number of integers"""


















"""def Max_Min():

    #Create variable num and enter an initial value.
    num = input( "Enter a an integer or \'stop' to end: ") 
    count = 0
    is_string = True
    
    
    #while(is_string == True):
    #check if num's initial value is stop
    while(is_string == True):
        if(count == 0 and num == 'stop'):
            is_string = True 
            print("You didn't enter any numbers")
            

        #while(is_string == False):

        else:
            is_string = False
            while(is_string == False):
                
                num = int( input("Enter an integer or \'stop' to end: ") )
                count += 1
                #print(num)
                #print(count)
                #print(type(num))

                if(num == type(str)):
                    is_string = True
                    break
                
            print(count)
        

Max_Min()"""