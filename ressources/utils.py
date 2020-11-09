#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt, floor
import random
import numpy as np


def swapPos(list, pos1, pos2): 
    """Swap two elements in list."""
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def euclid(a:int,b:int,Verbose=False):  
    
    """Find the Greatest Common Divisor of number a and b."""
    
    # The GCD of two relative integers is equal to the GCD of their absolute values.
    a,b=abs(a),abs(b) 

    # The largest of the two numbers is replaced by the remainder of the Euclidean division of the larger 
    # number by the smaller one. 
    if (b==0) :
        return a
    elif (b>a) :
        return euclid(b,a,Verbose)
    else:
        r=a%b

        if Verbose:
            q=a//b
            print(f"{a} = {b}*{q} + {r}")
        
        return euclid(b,r,Verbose)


def euclid_ext(a:int,b:int):
    
    """Extension to the Euclidean algorithm, and computes, in addition to the greatest common divisor of integers a and b, also the coefficients of Bézout's identity, which are integers x and y such that a x + b y = gcd ( a , b )."""
    x0, x1, y0, y1 = 0, 1, 1, 0
    a_buffer,b_buffer=a,b
    n=1 # iterations
    
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, (y0 - q * y1)
        x0, x1 = x1, (x0 - q * x1)
        n+=1
    
    s=f"gcd({a_buffer},{b_buffer})={a_buffer}.{x0}+{b_buffer}.{y0}"
    
    return b, x0, y0, s, n
    
def inv(a:int,m:int):
    """If a and m are prime to each other, then there is an a^(-1) such that a^(-1) * a is congruent to 1 mod m."""
    
    if euclid(a,m) != 1 :
        print(f"gcd({a},{m}) != 1 thus you cannot get an invert of a.")
        return None
    
    # Modular inverse u solves the given equation: a.u+m.v=1 
    # n number of iterations
    _,u,_,_,_=euclid_ext(a,m)
    
    if u < 0 : u+=m
    
    return u,f"u = {u} + {m}k, k in Z"    
    
def primeFactors(n:int):
    
    """
    Decomposes an integer n into prime factors and calculates Euler’s Totient Function.
    
    Output: prime factors , Totient Function , Coprimes numbers
    """
    
    if n < 2 : 
        print("By definition, A prime number (or prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.")
        # 1 is primary with itself
        return None,1   
    
    ####
    # Euler’s Totient Function
    # To do before changing n value succently 
    ####
    
    phi_of_n=1
    coprimes=[1]
    
    # a and b are said to be coprime if the only positive integer (factor) that divides both of them is 1.
    for i in range(2,n):
        if euclid(i,n) == 1 :
            coprimes.append(i)
            phi_of_n+=1
    
    
    res=[]
    
    #While n is divisible by 2, print 2 and divide n by 2
    while n%2 == 0:
        res.append(2)
        n=n/2

    # n must be odd at this point (difference of two prime factors must be at least 2)
    # so a skip of 2 ( i = i + 2) can be used 
    
    # Running the loop till square root of n not till n.
    # почему ? Let's says that a.b=n. If a>sqrt(n) and b>sqrt(n) then a.b>sqrt(n).sqrt(n). Let a.b>n.
    # QED ad absurdum
    
    for i in range(3,int(sqrt(n))+1,2): # From 3 to
        # while i divides n , print i ad divide n 
        while n % i== 0:
            res.append(int(i))
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        res.append(int(n))

    prime_decompo = dict()

    # Return unique numbers in list.
    unique = []
    for number in res:
        if number not in unique:
            unique.append(number)

    for elt in unique:
        prime_decompo[elt]=prime_decompo.get(elt,res.count(elt))
    

    return prime_decompo,phi_of_n,coprimes
        
def exp_mod(a,exp,mod):
    """General method for fast computation of large positive integer powers of a number"""

    if mod == 1:
        return 0

    res=1
    a=a%mod
    
    while (exp>0) :

        # (exp%2==1)
        # same as : (exp & 1) == 0
        # least significant bit of any decimal odd number is one

        if exp & 1:
            res=(res*a)%mod
        
        # Deleting LSB
        # exp=floor((exp/2))
        exp >>=1

        # Updating a
        a=(a*a)%mod
    
    return res

def fastPower(a,n):
    if(n==0):
      return 1
    x=a**(n/2)
    x=x*x
    if(n%2==1):
      x=x*a
    return x

    
def millerR (n:int, s=40):

    """Use Rabin-Miller algorithm to return True (n is probably prime) or False (n is definitely composite)."""

    if n<4 or n%2 :
        print("Error: n>3 and n need to be odd.")
        return -1

    def millerT(n:int):
        if n<6: # Shortcut for small cases here
            return [False,False,True,True,False,True][n]

        # Initialisation -> 2^0*d=n-1
        d = n - 1
        power = 0

        while d%2 == 0:
            d = d/2
            # c factors of 2
            power+=1

        import random as r
        import math as m

        a = r.randint(2, n-2)
        x = exp_mod(a,d,n)

        if(x == 1 or x == n - 1):
            return False
        else:
            for _ in range(0,power):
                x = fastPower(x,2) % n
                if(x == n - 1):
                    return False
            return True

    # Trying s times to check

    for _ in range(1, s):
        if millerT(n):
            return False

    return True