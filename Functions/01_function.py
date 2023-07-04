#NORMAL METHOD
# marks1 = [20,30,40,59]
# percent1 = (marks1[0]+marks1[1]+marks1[2]+marks1[3])/400 *100
# marks2 = [80,70,90,59]
# percent2 = (marks2[0]+marks2[1]+marks2[2]+marks2[3])/400 *100
# print(percent1,percent2)

#using function
def percent(marks):
    p = (marks[0]+marks[1]+marks[2]+marks[3])/400 *100
    return p

marks1 = [20,30,40,59]
print(percent(marks1))
marks2 = [80,70,90,59]
print(percent(marks2))
