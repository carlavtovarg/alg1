import random
random_value = random.randint(1, 100)
for x in range (1, 8):
    if(x==7):
        print("Sorry, you didn'/t guess the correct number. The correct number is {0}".format(random_value))
        quit()
    num_try= input("Please guess a number between 1 and 100 (attemp {0}): ".format(x))
    #validation
    try:
        num_try = int(num_try)
    except ValueError:
        print("Please enter just enter integer number")
    except Exception:
        print("An unknown error has ocurred")
    else:
        if num_try==random_value:
            print("Correct! You win.")
            quit()
        elif num_try > random_value:
            print("Wrong guess, you guessed too high.")
        elif num_try < random_value:
            print("Wrong guess, you guessed too low.")
