#play guessing number
guess_number = 0
number = 37
while number != guess_number:
    guess_number = int(input("Please guess a number\n"))
    if guess_number > number:
        print("lower")
    else:
        print("higher")
print("you are win. The number is {}. you are mindreader".format(guess_number))
