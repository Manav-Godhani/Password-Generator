# password generator - mnv_godhani 😉

import random
alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = ["1","2","3","4","5","6","7","8","9","0"]

def pass_generator(x):
    print("=================================")
    print(" 1️⃣  Mix of Alphabets and Numbers")
    print(" 2️⃣  Only Alphabets")
    print(" 3️⃣  Only Numbers")
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

    
      
    

length = int(input("Enter the length of password ! :- "))
pass_generator(length)
    