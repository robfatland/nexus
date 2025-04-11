from os import environ
from math import sqrt
import boto3
import requests
import sys

a = int(environ["START_INDEX"])

print(a)

s = ''

def IsPrime(n):
    if n < 2: return False
    if n == 2: return True
    if not n%2: return False
    ul = int(sqrt(n))
    for c in range(3, ul, 2):
        if not n % c: return False
    return True
    
for i in range(a*100, (a+1)*100):
    if IsPrime(i): s += str(i) + '\n'

def WriteSolutionFile(s, f):
    with open(f, "w") as file: file.write(s)


WriteSolutionFile(s, "/out/primes_" + str(a*100) + "_" + str((a+1)*100) + ".txt")

print(s)

sys.exit(1)
    