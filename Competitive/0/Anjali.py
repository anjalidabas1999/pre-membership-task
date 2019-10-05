Problem 0

You are required to write a program for `Egyptian Fractions`

##The problem statement

> For a given fraction p/q in it's simplest form express it as a summation of fractions having 1 as their numerator

> You need to find a set of fractions such that it's `length is minimum`.
import math  
def egyptianFraction(num, dem): 
    print("The Egyptian Fraction Representation"+
          "of {0}/{1} is".
                  format(num,dem))  
    d = [] 
    while num != 0: 
        x = math.ceil(dem / num) 
        d.append(x) 
        num = x * num - dem 
        dem = dem * x 
    for i in range(len(d)): 
        if i != len(d) - 1: 
            print(" 1/{0} +". 
                    format(d[i]), end='') 
        else: 
            print(" 1/{0}".
                    format(d[i])) 
a=int(input("Enter numerator: "))
b=int(input("Enter denominator: "))
egyptianFraction(a, b)
