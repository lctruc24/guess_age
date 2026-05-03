maxAge = 100
minAge = 0

print("""Instruction:
'yes' if your age > guessed age
'no' if your age < guessed age
'perfect' if your age = guessed age""")
print()

guessAge = int((maxAge + minAge)/2)
print(f"Your age: {guessAge}")

while True:
    guessAge = int((maxAge + minAge)/2)
    print("Your age is greater than the guessed age")
    answer = input("> ")

    if answer.lower() == 'yes':
        minAge = guessAge
        guessedAge = int((maxAge + minAge)/2)
        print(f'Your age: {guessedAge}')

    elif answer.lower() == "no":
        maxAge = guessAge
        guessedAge = int((maxAge + minAge)/2)
        print(f'Your age: {guessedAge}')

    elif answer.lower() == "perfect":
        print("---Congratuation!!!---")
        print(f'---Your age is {guessAge}---')
        break
    
    else:
        print("I don't understand your mean")
