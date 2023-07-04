a= [1,2,3,4,5]
for item in a:
    print(item)
    if(item==3):
        # break
        continue
    print("break the loop")
else:
    print("We are in else statements")