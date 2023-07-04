a={1,3,5,7,8,9}
print(type(a))
print(a)

#IMPORTANT:this syntax will create an empty directory and not an empty set
a={}
print(type(a))

#An empty set will create this syntax
a=set()
print(type(a))

#Adding value in an empty set
a.add(4)
a.add(5) 
a.add(6)
a.add(6)
#a.add([1,2,3]) #In an set we can't add list 
a.add((12,21,32)) #but we can add tupples
print(a)
print(len(a))
a.remove(5)
print(a)


