from math import factorial


def factorial_cal(num):
    product = 1
    
    for i in range(num):
        product = product*(i+1)
    return product
print(factorial_cal(5))