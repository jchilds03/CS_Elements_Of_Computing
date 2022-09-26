def main():
    num = int( input() )
    
    if (num <= 0 or num >= 1000):
        print("Error.")
    
    else:
        r1 = num % 10
        d1 = num // 10
        
        r2 = d1 % 10
        d2 = d1 // 10
        
        r3 = d2 % 10
        d3 = d2 // 10
        print(r1 + r2 + r3)
main()