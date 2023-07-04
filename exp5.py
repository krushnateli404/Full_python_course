f= open("test.txt", "r")

number_of_lines=0
number_of_words=0
number_of_charcter=0
for lines in f:
    lines=lines.strip("\n")
    words=lines.split()
    number_of_lines+=1
    number_of_words+=len(words)
    number_of_charcter+=len(lines)


f.close()
print("number of lines ", number_of_lines,"\n number of words " ,number_of_words,"\nnumber of charcters ",number_of_charcter)