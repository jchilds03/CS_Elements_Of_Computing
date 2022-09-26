"""Create a program that calculates the temp in 
fahrenheit and also accounts for wind chill within
certain parameters for the degrees."""

#coldness calculation that accounts for windchill
#twc = 35.74 + 0.6215(ta) - 35.75v**0.16 + 0.4275(ta)v**0.16

#ta is the outside temperature in F degrees

#v is the wind speed in mph

#twc is wind-chill temperature.

#Formula can't be used for wind speeds < 2 mph, temp < -58 or temp > 41


def main():
    #input for temperature (float)
    ta = float ( input() )

    #input for wind speed in mph (float)
    v = float ( input() )

    #constraint
    if(ta < -57 or ta > 40 or v < 2):
        print("Error.")
    else: 
        twc = 35.74 + (0.6215 * ta) - (35.75 * v ** 0.16) + (0.4275 * ta * v ** 0.16)
        print( round(twc, 1) )
main()