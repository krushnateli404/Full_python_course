import os
path=os.getcwd
print(os.getcwd)
dir_list=os.listdir()
print("Files available in current directory:")
for a in dir_list:
    if os.path.isfile(a):
        print(a)
print(dir_list)













#PROGRAM:2



# def Appendtext(fname):
#     with open(fname,'+a') as f:
#         f.write('Hi,Krushna')
#         f.write('Welcome in python course')
#         f.close()
#         file=open('filel.txt')
#         print("File contetn before append")
#         print(file.read())
#         Appendtext('file1.txt')
#         file1=open('file1.txt')
#         print("File content after append")
#         print(file1.read())
#         file.close()

    #PROGRAM 3
    # file1=open("file1.txt","r")
    # numbers_of_lines=0
    # numbers_of_words=0
    # numbers_of_characters=0
    # for line in file:
    #     line = line.strip("/n")