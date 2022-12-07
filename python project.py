import random
print("Welcome to Dice roll")
print("Start Game")
i=""
scr=0
while i!="n":
    x = int(input("Enter number from 1-6: "))
    y = random.randint(1,6)
    if x not in range(1,6+1):
        print("Number must be between 1 to 6!")
    else:
        print(y)
        if x==y:
            scr+=5
            print("Congrats You win!")
    p = print("Do you want to play again ?")
    i = input("Press 'y' for 'yes' and press any other key for exit : ")
    if i.upper() == "Y":
        continue
    else:
        print("Game over!")
        break
print("Your score:",scr)