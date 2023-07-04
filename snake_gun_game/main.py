import random
def gameWin(comp,win):
  if comp == you:
    return None
  elif comp == 'w':
      if you =='s':
        return True
      elif you=='g':
        return False
      
  elif comp == 's':
       if you =='g':
        return True
       elif you =='w':
         return False
  elif comp == 'g':
       if you =='s':
        return False
       elif you =='w':
         return True
       


print("Comp turn:Snake(s) Water(w) or Gun(g)")
randNo = random.randint(1,3)
if randNo == 1:
     comp = 's'
elif randNo ==2:
    comp = 'w'
elif randNo ==3:
    comp = 'g'

you = input("Your turn:Snake(s) Water(w) or Gun(g): ")
print(f"Comp is choose: {comp}")
print(f"you are choose: {you}")

a = gameWin(comp,you)
if a==None:
    print("Match is tied....")
elif a:
    print("You win!")
else:
    print("You lose!")


