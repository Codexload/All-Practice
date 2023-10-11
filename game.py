import random
sec_number = random.randint(1, 10)
name = input("Enter Your Name--> ")
print("Well Hello There MR.", name,"Welcome To the game \n Now Guess A Number(1, 10)")
#-----------------------------------------Coding-----------------------------------------
for i in range(1, 100):
    innum = int(input("Enter Your Gussed Number--> "))
    if innum < sec_number:
        print("Well", name, "You Entered a Low Number(INCORRECT)")
    elif innum > sec_number:
        print("Well", name, "You Entered a High Number(INCORRECT)")
    else:
        break
if innum == sec_number:
    print("Well", name, "You Entered The Correct Number(CORRECT)🎉🎉🎉")
else:
    print("Ooh No You Guess The Wrong Number")