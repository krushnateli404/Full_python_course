letter = '''Dear <|NAME|>
Greeting from CodeWithHarry. I am happy to tell you your selection
You are selected!
Thanks and regards,
DuaK
<|DATE|>'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)