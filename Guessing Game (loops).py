#Guessing Game

# guess = int(input("Enter your number: "))
# c = 10
for i in range(10):
    guess = int(input("Enter your number: "))
    print(guess)
    if (guess== 21):
        print("You have Won!")
        break
    elif (guess < 21):
        print ("Enter a greater number!")
    elif (guess > 21):
        print("Enter a smaller number!")
else:
    print("Game OVer! You have used up all your turns")