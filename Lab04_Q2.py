#!/usr/bin/env python
# coding: utf-8


# 2.1
import random

#while 1:
#    a = input("Press Enter to continue")
#    if a == "end":
#        break
#    else:
#        print(random.randint(1, 6))

import msvcrt

while True:
    msvcrt.getch()
    print(random.randint(1, 6))


# 2.2
a = input("Enter a number: ")
b = input("Enter a number: ")
a = int(a)
b = int(b)

if a < b:
    t = a
    a = b;
    b = t;
    
while b>0:
    q = a//b
    r = a%b;
    a = b
    b = r
    
print(a)



# 2.3
import datetime 

epoch_time = int(input("Enter the time in seconds: "))
datetime_time = datetime.datetime.fromtimestamp(epoch_time)
print(datetime_time)



# 2.4
def LVdistance(a,b):    
    if min(len(a),len(b))==0:
        return max(len(a),len(b))
    elif a[0]==b[0]:
        return LVdistance(a[1:],b[1:])
    L = 1 + min(LVdistance(a,b[1:]), LVdistance(a[1:],b), LVdistance(a[1:],b[1:]))     
    return(L)

print(LVdistance("kitten","sitting"))


# 2.5
def Collatz(n):
    out =[]
    counter = 0;
    while(n > 1):
        out.append(n)
        counter = counter + 1
        if n%2 == 0:
            n = int(n/2)
        else:
            n = 3*n+1
    out.append(1)
    counter = counter + 1
    return counter, out


import numpy as np
Collatz_Sequence_Length = np.zeros(1000)
Collatz_Sequences = []


for i in range(1,1000):
    Collatz_Sequence_Length[i], Collatz_Sequence = Collatz(i)
    Collatz_Sequences.append(Collatz_Sequence)
    
    
n = Collatz_Sequence_Length.argmax()
print(n+1)
print(int(Collatz_Sequence_Length[n]))
print(Collatz_Sequences[n])

