"""Write program tha tcalculates energy needed
to heat water from an initial temperature."""

#formula to compute is Q = M * (tfinal - tinitial) * 4184
#M is weight of water in kilograms
#tinitial  is initial temp in degrees celcius
#tfinal is final temp in degrees celcius
#Q is energy measured in joules. 

#input weight of water in kilograms as float
M = float( input() )

#input initial temperature as float
t_initial = float( input() )

#input final temperature as float
t_final = float( input() )

#constraints M >= 0 and t_f >= t_i >= 0
if(M < 0 or t_final < t_initial or t_initial < 0):
    print("Error.")
else:
    Q = M * (t_final - t_initial) * 4184.0
    print( round(Q,1) )
