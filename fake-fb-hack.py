#-----------------------------------------FAKE-FB-HACKING==V0.0.0.1------------------------------------
import random
import string
import sys
print("███████ ██████        ██   ██  █████   ██████ ██   ██ ██ ███    ██  ██████  ")
print("██      ██   ██       ██   ██ ██   ██ ██      ██  ██  ██ ████   ██ ██       ")
print("█████   ██████  █████ ███████ ███████ ██      █████   ██ ██ ██  ██ ██   ███ ")
print("██      ██   ██       ██   ██ ██   ██ ██      ██  ██  ██ ██  ██ ██ ██    ██ ")
print("██      ██████        ██   ██ ██   ██  ██████ ██   ██ ██ ██   ████  ██████  ")

password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5, 15))
user_id = int(input("Enter The URL Code==> "))
full_URL = "https://www.facebook.com/profile.php?id=" + str(user_id)
print("Confirm That It Is Your Terget ID\n" + full_URL)
print("███████ ██████        ██   ██  █████   ██████ ██   ██ ██ ███    ██  ██████  ")
print("██      ██   ██       ██   ██ ██   ██ ██      ██  ██  ██ ████   ██ ██       ")
print("█████   ██████  █████ ███████ ███████ ██      █████   ██ ██ ██  ██ ██   ███ ")
print("██      ██   ██       ██   ██ ██   ██ ██      ██  ██  ██ ██  ██ ██ ██    ██ ")
print("██      ██████        ██   ██ ██   ██  ██████ ██   ██ ██ ██   ████  ██████  ")
print("Chose Your Operation \n 1. Hack This ID By Broteforsing \n 2. Hack This ID By Cracking \n 3. Hack This ID (Recomended) \n 4. ID Information \n 5. Exit")
option = input("==> ")
if option == "":
    print("OOps You Don'n Enter Any Option")
elif option == "1":
    print("Trying.....")
    print("Password Found!!!")
    print("Your Password For " + full_URL + " Is " + str(password))
elif option == "2":
    print("Your Password For " + full_URL + " Is " + str(password))
elif option == "3":
    print("This Fungtion Is Under Devlopment\nSorrry For It")
elif option == "4":
    print("This Is Not A Secured Id Because \n 𝕀𝕟 𝕋𝕙𝕚𝕤 𝕎𝕠𝕣𝕝𝕕 ℕ𝕠 𝕀𝔻 𝕀𝕤 ℕ𝕠𝕥 𝕊𝕖𝕔𝕦𝕣𝕖 𝔽𝕠𝕣 𝕄𝕪 𝕋𝕠𝕠𝕝😡")
elif option == "5":
    sys.exit()
else:
    print("Opps Chose A Number (1, 5)")