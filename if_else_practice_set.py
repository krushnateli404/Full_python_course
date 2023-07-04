from cgi import print_directory


# n1 = int(input("Enter number 1:"))
# n2 = int(input("Enter number 2:"))
# n3 = int(input("Enter number 3:"))
# n4 = int(input("Enter number 4 :"))

# if(n1>n2):
#     f1 = n1
# else:
#     f1 = n2

# if(n3>n4):
#     f2 = n3
# else:
#     f2 = n4

# if(f1>f2):
#     print(f1,"is the gratest number")
# else:
#     print(f2,"is the greatest number")


#Problem:2




# n1 = int(input("Enter number 1:"))
# n2 = int(input("Enter number 2:"))
# n3 = int(input("Enter number 3:"))
# n4 = int(input("Enter number 4 :"))

# if(n1>n2):
#     f1 = n1
# else:
#     f1 = n2

# if(n3>n4):
#     f2 = n3
# else:
#     f2 = n4

# if(f1>f2):
#     print(f1,"is the gratest number")
# else:
#     print(f2,"is the greatest number")


#Problem:2

sub1 = int(input("Enter the marks of sub1:"))
sub2 = int(input("Enter the marks of sub2:"))
sub3 = int(input("Enter the marks of sub3:"))

if(sub1<33 or sub2<33 or sub3<33):
    print("Your are fail...cause yor get per subject marks less than 33%")
elif (sub1+sub2+sub3)/3<44:
    print("Your are failed...beacause your total persentage is less than 44%")
else:
    print("Congratulations! Your are passeed...")