"""GRAHAM RUTTIMAN"""
name = input("What is your name?")
if name=="":
    name = input("Please tell me your name?")
else:
    for i in range (1,len(name),2):
        print(name[i])



