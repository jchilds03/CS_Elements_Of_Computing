#create celcius variable and condition for celcius variable

def main():
    celsius = float(input())
    
    fahrenheit = ( (9/5) * celsius + 32 )
    print( round(fahrenheit, 1))

main()