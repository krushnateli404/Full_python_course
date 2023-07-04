from ast import operator


a = int(input("Enter the number: "))
# This is for AND operators
# if(a>34 and a<56):
#     print("Ths number is valid")
# else:
#     print("The condition is invalid")

# This is for or oprators
if(a>34 or a<56):
    print("Ths number is valid")
else:
    print("The condition is invalid")


# IS operator

x = None
if(x is None ):
   print("Yes")
else:
    print("No...")

#IN OPERATOR
y = [12,23,34,34]
print(12 in y)