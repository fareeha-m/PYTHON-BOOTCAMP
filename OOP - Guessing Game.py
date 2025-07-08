class GuessingGame:
    def __init__(self):
        self.secretnumber = 15
        self.attempts = 3

    def play(self):
        for i in range (self.attempts):
            guess = int(input("Enter your number: "))
            print(guess)
            if guess == self.secretnumber:
                print("You Won!")
                break
            elif guess < self.secretnumber:
                print ("Enter a Larger Number")
            elif guess > self.secretnumber:
                print("Enter a smaller number")
        else:
            print ("Game Over! You have used all your attempts")

game = GuessingGame()
game.play()