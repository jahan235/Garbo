x = 0
magicNumber = 5
numberGuessed = False

while not numberGuessed:
    x = int(input("ENTER YOUR GUESS: "))
    if x > magicNumber:
        print("\nLOWER\n")
    elif x < magicNumber:
        print("\nHIGHER\n")
    else:
        numberGuessed = True

print(f"YOU GUESSED CORRECTLY! THE MAGIC NUMBER WAS: {magicNumber}!")