#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer

Enter a number: 2.4
2.4 is not a positive integer

Enter a number: 5
5 is a positive integer

Enter a number: 4.0
4.0 is a positive integer
"""
import math

x=float(input("Give a number of any type: "))
if (x-1)==(round(x,1)-1) and x>0:
    print(f"{x} is a positive integer")
else:
    print(f"{x} is not a positive integer")