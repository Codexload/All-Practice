#This Code Was Practice By Tanjimul Hisham (Fardin)
##############Tanjimul Hisham (Fardin################)
print(" ______            _ _        ")
print("|  ____|          | (_)       ")
print("| |__ __ _ _ __ __| |_ _ __ ")
print("|  __/ _` | '__/ _` | | '_ \  ")
print("| | | (_| | | | (_| | | | | |")
print("|_|  \__,_|_|  \__,_|_|_| |_| ")

print("----------Upper Case-----------")
name = "Tanjimul Hisham"
name_update_1 = str(name.upper())
print(name_update_1)

print("----------Lower Case-----------")
name = "Tanjimul Hisham"
name_update_2 = name.lower()
print(name_update_2)

print("----------Finding-----------")
value = "Tanjimul Hisham"
value_count_singal_letter = value.find("T")
print(value_count_singal_letter)
value_count_maltipal_letter = value.find("jim")
print(value_count_maltipal_letter)
value_count_in_word = value.find("Hisham")
print(value_count_in_word)

print("----------Replace-----------")
word = "Tanjimul Hisham"
word_replace = word.replace("Hisham", "Fardin")
print(word_replace)

print("----------Type Casting-----------")
current_age = input("Enter Your Current Age = ")
future_age = int(current_age) + 20
print(future_age)

print("----------Calculate-----------")
first_number = input("Enter Any Number= ")
second_number = input("Enter Any Number= ")
print(int(first_number) + int(second_number))

print("----------Fungtion1-----------")
def hello(name):
    print("Hello " + name)
hello("Tanjimul")
hello("Hisham")

print("----------Fungtion2-----------")
def mechine(number_one, number_two):
    if number_one > number_two:
        print("Number One Is Greater Than Number Two", number_one, ">", number_two)
    elif number_one == number_two:
        print("Number One Is Equal To Number Two", number_one, "=", number_two)
    else:
        print("Number One Is Less Than Number Two", number_one, "<", number_two)
number_one = int(input("Enter 1st Number--> "))
number_two = int(input("Enter 2nd Number--> "))
mechine(number_one, number_two)
a = 100
b = 100
mechine(a, b)