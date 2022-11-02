target = 12
userChoice = int(input("Guess the number: "))
guesses = 1
while userChoice != target:
    guesses = guesses + 1
    if userChoice < target:
        userChoice = int(input("Guess higher!"))
    elif userChoice > target:
        userChoice = int(input("Guess lower!"))
    else:
        break
print(f"It took you {guesses} guesses.")
