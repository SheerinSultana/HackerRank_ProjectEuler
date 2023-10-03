#!/bin/python3
import sys
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a,b,s=1,2,0
    while a<n:
        if a%2==0:
            s+=a
        a,b=b,a+b
    print(s)     
