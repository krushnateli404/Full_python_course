mydict={
    "Intro":"I am Krushna teli",
    "Work" :"I am working in amazon",
    "Inspiration":{'Krushna':'Coder'}
}

#DICTIONARY METHOD
print(mydict.values())  #Prints the keys of dictionary
print(mydict.items())  #Prints the keys-values pairs of dictionary
print(mydict.keys())  #Prints the keys of dictionary
print(mydict)

updatedict={
    "Santosh":"Friend",
    "Pranav":"Friend",
    "Shubham":"Friend"



}
mydict.update(updatedict)  #Update the values adding  of keys-values pairs of list 
print(mydict)

print(mydict.get("Avi")) #Prints the value with key
print(mydict["Avi"]) #Prints the value with key

#Defference between .get and []syntax is
print(mydict.get("Avi"))  #written None as Avi is not present in list
print(mydict["Avi"])  #Throws an error as Avi is not present in list

