import re


def sum_recursive(n):
    if(n==0):
        return 0
    return n + sum_recursive(n-1)
s = sum_recursive(5)
print(s)
