"""Write a program that reads the subtotal 
and the gratuity rate and computes the gratuity
and total."""

"""Input: First line will contain the subtotal
(float)"""
from os import sep


subtotal = float( input() )

"""Second line contains the grauity rate (float)"""
gratuity = float( input() )


#constraint: subtotal >= 0 and rate >= 0
if(subtotal < 0 or gratuity < 0):
    print("Error. Broke Boi.")
else:
    gratuity = subtotal * (gratuity/100)
    subtotal = gratuity + subtotal
    round(gratuity, 2) 
    round(subtotal * gratuity) 
    print( "$",format(gratuity, "1.2f"), sep = "" )
    print( "$",format(subtotal, "1.2f"), sep = "" )