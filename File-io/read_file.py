#Use open function to read the content of file
# f = open('krushna.txt','r') 
f = open('krushna.txt') #by default 'r' is there
data =f.read()
# data = f.read(5)
print(data)
f.close()