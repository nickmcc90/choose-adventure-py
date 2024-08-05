name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

magic_potion = None
charisma = 0

answer = input("You see a cat. Do you pet it? (yes/no) ").lower()

if answer == "yes":
    print("The cat purred.")
    charisma += 1

elif answer == "no":
    print("The cat walked away.")

else:
    print("Didn't expect that, but okay. The cat walked away.")

# start of adventure
    
answer = input("You see fork in the road. Go left or right? (left/right) ").lower()

if answer == "left":
    print("You choose left.")
    answer = input("A person walks up to you and asks if you choose left. Do you tell the truth? (truth/lie) ").lower()
    if answer == "truth":
        print("Well, I'll take your word for it. Go ahead.")
        charisma += 1
        answer = input("A black cat walks up to you. It asks if you have been nice and truthful throughout the game. Have you? (yes/no) ").lower()
        if answer == "yes" and charisma == 2:
            print("Well, meow meow! You win the game for being great.")
        elif answer == "no" and charisma != 2:
            print("Well, you didn't lie to me. So I guess you win. Meow!")
        else:
            print("You didn't have to lie to me. Begone!")
    elif answer == "lie":
        print("Well, I'll take your word for it. Go ahead.")
        charisma -= 1
        answer = input("An orange cat walks up to you. It asks if you have been nice and truthful throughout the game. Have you? (yes/no) ").lower()
        if answer == "yes" and charisma == 2:
            print("Well, meow meow! You win the game for being great.")
        elif answer == "no" and charisma != 2:
            print("Well, you didn't lie to me. So I guess you win. Meow!")
        else:
            print("You didn't have to lie to me. Begone!")
    else:
        print("Choose an actual answer, and maybe you won't quit the game.")
elif answer == "right":
    print("You choose right.")
    answer = input("A creature walks up to you and asks if you choose right. Do you tell the truth? (truth/lie) ").lower()
    if answer == "truth":
        print("Well, I'll take your word for it. Go ahead.")
        charisma += 1
        answer = input("A green cat walks up to you. It asks if you have been nice and truthful throughout the game. Have you? (yes/no) ").lower()
        if answer == "yes" and charisma == 2:
            print("Well, meow meow! You win the game for being great.")
        elif answer == "no" and charisma != 2:
            print("Well, you didn't lie to me. So I guess you win. Meow!")
        else:
            print("You didn't have to lie to me. Begone!")
    elif answer == "lie":
        print("Well, I'll take your word for it. Go ahead.")
        charisma -= 1
        answer = input("An purple cat walks up to you. It asks if you have been nice and truthful throughout the game. Have you? (yes/no) ").lower()
        if answer == "yes" and charisma == 2:
            print("Well, meow meow! You win the game for being great.")
        elif answer == "no" and charisma != 2:
            print("Well, you didn't lie to me. So I guess you win. Meow!")
        else:
            print("You didn't have to lie to me. Begone!")
    else:
        print("Choose an actual answer, and maybe you won't quit the game.")
else:
    print("Sorry, you lose.")

print("Thanks for playing.")