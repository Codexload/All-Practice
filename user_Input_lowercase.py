i = 1
while i <= 10:
    print("1. Yes\n2. No")
    user_input = input("==> ").lower()
    if user_input == "yes":
        print("Thanks For Chosing Yes")
    elif user_input == "no":
        print("You Chose No")
    i += 1