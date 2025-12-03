# password generator - mnv_godhani 😉

import random
alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","@","#","$","%","^","&","*","(",")"]
specical_char = [" ","~","`","-","_","=","+","{","}","[","]","|",":",";","'","<",">",",",".","?","/"]

def pass_generator(x):
    print("=================================")
    print(" 1️⃣  Mix of Alphabets and Numbers")
    print(" 2️⃣  Only Alphabets")
    print(" 3️⃣  Only Numbers")
    print(" 4️⃣  Mix of Alphabets, Numbers and Symbols")
    print(" 5️⃣  Mix of Alphabets, Numbers, Symbols and Special Characters")
    print("=================================")
    choice = int(input("Enter Your requirements :-  :- "))

    if choice == 1:
        allchar = alp + num
        print("Generating Password...")
        for i in range(1,x+1):
            a = random.choice(allchar)
            print(a, end="")
    elif choice == 2:
        for i in range(1,x+1):
            a = random.choice(alp)
            print(a, end="")
    elif choice == 3:
        for i in range(1,x+1):
            a = random.choice(num)
            print(a, end="")
    elif choice == 4:
        allchar = alp + num + symbols
        print("Generating Password...")
        for i in range(1,x+1):
            a = random.choice(allchar)
            print(a, end="")
    elif choice == 5:
        allchar = alp + num + symbols + specical_char
        print("Generating Password...")
        for i in range(1,x+1):
            a = random.choice(allchar)
            print(a, end="")
    else:
        print("Please Enter Valid Choice 👎")

    
length = int(input("Enter the length of password ! :- "))
pass_generator(length)

# password generator - mnv_godhani 😉
# This is a simple password generator script that allows users to create passwords based on their preferences.
# It offers options to include alphabets, numbers, symbols, and special characters in the generated password.
# The user can specify the desired length of the password, and the script will generate a random password accordingly.
# Enjoy using it and stay secure!

    