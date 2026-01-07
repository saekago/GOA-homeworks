seats = 500
while seats > 0:
    print("sell ticket")
    seats = seats - 1

# ----------------------

number = 67
attempt = 3
user_input = ""

while user_input != number and attempt > 0:
    user_input = int(input("guess the number between 1 - 100: "))
    attempt -= 1

    if user_input == number:
        print("you win!")
    elif attempt == 0:
        print("you lose!")
    else:
        print("wrong number, try again!")
        print("you still have " + str(attempt) + " attempts!")