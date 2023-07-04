def remove_split(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()
this = " Krushna is good boy  "
n = remove_split(this,"Krushna")
print(n)