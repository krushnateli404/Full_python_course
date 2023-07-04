num = int(input("Enter the number: "))
# for i in range(0,num+1):
#     print("*" * (i+1))

for i in range(4):
    print(" " * (num-i-1),end="")
    print("*" * (2*i-1),end="")
    print(" " * (num-i-1))