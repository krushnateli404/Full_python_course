import array as ary
from turtle import st
str="Atharava college"
list1 = [1,'Welcome',1.4,(2+3j)]
array1 = ary.array('i',[1,2,3,4,5,6])
dic = {'Name':"XYZ",'Age':13,'Email':"telikrushna@314",'class':'12th'}
set1 ={"C++","Python","Java","Php"}
tuple1={'A','B','C','D','E',1,3,4,5.6}
print("This is %s datatype"%type(str) ,"and string is ",str )
print("This is %s datatype"%type(list1) ,"and string is ",list1 )
print("This is %s datatype"%type(array1) ,"and string is ",array1)
print("This is %s datatype"%type(dic) ,"and string is ",dic)
print("This is %s datatype"%type(set1) ,"and string is ",set1 )
print("This is %s datatype"%type(tuple1) ,"and string is ",tuple1 )
print("\n\n Print all list items using for loop")
for i in list1:
    print(i)
    print("\n\n Print all tuple items using while loop")
    i=0
    while i<len(tuple1):
        print(tuple1[i])
        i=i+1
        print("\n\n check if c++ is present in the set1 set.")
        if"C++" in set1:
            print("Yes, c++ is present in set1")
        else:
                print("No,C++ is not present in set1")

                