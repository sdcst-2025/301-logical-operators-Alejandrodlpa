#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
import math 
x=int(input("An integer "))
y=int(input("Another integer "))
z=int(input("One Last inegert "))
high=max(x,y,z)
low=min(x,y,z)
if (x==low and y==high) or (y==low and x==high):
    mid=z
if (y==low and z==high) or (z==low and y==high):
    mid=x
if (z==low and x==high) or (x==low and z==high):
    mid=y
if ((low**2)+(mid**2))**(1/2)==high:
    print(f"{x},{y},{z} form a Pythagorean triple")
else:
    print(f"{x},{y},{z} do not form a Pythagorean triple")