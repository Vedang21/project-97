print("Number Guessing Game between 1-10")

guessingNumber= int(input("enter your guessingNumber: "))

if (guessingNumber<9):
    print("Your Guess was too low: Guess a higher number")
elif(guessingNumber>1):
    print("Congratulation you Won")
else:
    print("Your Guess was too high: Guess a lower number")