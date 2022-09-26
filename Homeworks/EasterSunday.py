# File: EasterSunday.py
# Student: Jordan Childs
# UT EID: jac22829
# Course Name: CS303E
# 
# Date: 09/05/2022
# Description of Program: Guess what day Easter Sunday will fall on.


#STEP 1: Ask user for year

y = int( input("Enter year: "))
#print("It is year: ",y)

#STEP 2: Divide y by 19, call remainder a

a = y % 19
#print("a = ", a)

#STEP 3: Divide y by 100 to get a quotient b and a remainder c

b = y // 100
#print("b = ", b)

c = y % 100
#print("c = ", c)

#SSTEP 4: Divide b by 4 to get a quotient d and a remainder e

d = b // 4
#print("d = ", d)

e = b % 4 
#print("e = ", e)

#STEP 5: Divide (8 * b + 13) by 25 to get a quotient g. Ignore remainder

g = (8 * b + 13) // 25
#print("g = ", g)

#STEP 6: Divide (19 * a + b - d - g + 15) by 30 to get remainder h. Ignore quotient

h = (19 * a + b - d - g + 15) % 30
#print("h = ", h)

#STEP 7: Divide c by 4 to get a quotient j and a remainder k

j = c // 4
#print("j = ", j)

k = c % 4
#print("k = ", k)

#STEP 8: Divide(a + 11 * h) by 319 to get a quotient m. Ignore remainder

m = (a + 11 * h) // 319
#print("m = ", m)

#STEP 9: Divide(2 * e + 2 * j - k - h + m + 32) by 7 to get remainder r. Ignore Quotient

r = (2 * e + 2 * j - k - h + m + 32) % 7
#print("r = ", r)

#STEP 10: Divide (h - m + r + 90) by 25 to get a quotient n. Ignore remainder

n = (h - m + r + 90) // 25
#print("n = ", n)

#STEP 11: Divide (h - m + r + n + 19) by 32 to get a reaminder p. Ignore quotient

p = (h - m + r + n + 19) % 32
#print("P = ", p)


print("In ",y, " Easter Sunday is on month ", n, " and day ", p)