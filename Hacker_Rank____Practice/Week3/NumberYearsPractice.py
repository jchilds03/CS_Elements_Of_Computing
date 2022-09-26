"""Write a program that reads the # of minutes
and displays the # of years and days for the minutes.
For simplicity, assume a year has 365 days."""

def main():

    #constraint minutes > 0
    minutes = int( input() )

    if(minutes <= 0):
        print("Error.")
    else:
        days_calculator = (minutes / 60) // 24
        years_calculator = days_calculator // 365
        years_and_days_calculator = days_calculator % 365
        
        #print(days_calculator)
        #print(years_calculator)
        #print(years_and_days_calculator)
        print( format(minutes, "0.0f"), "minutes is approximately", format(years_calculator, "0.0f"), "year(s) and", format(years_and_days_calculator, "0.0f"), "day(s)")
main() 