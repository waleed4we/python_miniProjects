import random

def level_easy(com_num):
    print("--------- Level Easy ---------")
    print("Instructions \nAs It Is Easy Level , You Will Be Given Infinite Chances Until You Guess Correct Code , It Means You Can't Lose Here")
    print("After every guess, you will be told which digits are correct and correctly placed, and which digits are correct but wrongly placed.")
    print("In The End You Will Be Told How Many Total Attempts You Made")

    count = 0

    user_guess = input("\nGuess The Code : ")
    count += 1


    while(len(user_guess) != len(com_num)):
        print(f"Your Guess Must Be {len(com_num)} Digits Long")
        user_guess = input("Guess The Code Again Please : ")
        count += 1


    while(user_guess != com_num):
        correct_count = 0
        wrong_position_count = 0

        already_exist_list = [
            user_guess[i]
            for i in range(len(com_num))
            if user_guess[i] == com_num[i]
        ]

        for i in range(len(com_num)):
            check = user_guess[i] == com_num[i]
            if(check):
                correct_count += 1
                print(f"{user_guess[i]} is true and on correct position")
            else:
                if(user_guess[i] in com_num and already_exist_list.count(user_guess[i]) < com_num.count(user_guess[i])):
                    already_exist_list.append(user_guess[i])
                    print(f"{user_guess[i]} is correct but on wrong position")
                    wrong_position_count += 1

        print(f"\nFor This {user_guess} , Your Correct Digit & Correct Position Count Is {correct_count} And Correct Digit But Wrong Position Count Is {wrong_position_count}")
        user_guess = input("\nGuess The Code Again : ")
        count += 1
        while(len(user_guess) != len(com_num)):
            print(f"Your Guess Must Be {len(com_num)} Digits Long")
            user_guess = input("Guess The Code Again Please : ")
            count += 1

    if(user_guess == com_num):
        print("---------------------------")
        print(" Congratulations , You Won")
        print(f"    You took {count} attempts")
        print("---------------------------")

def level_medium(com_num):

    print("------- Level Medium -------")
    print("Instructions \nAs It Is Medium Level , You Will Have Limited Chances To Guess The Correct Number")
    print("After every guess, you will be told how many digits are correct and correctly placed, and how many digits are correct but wrongly placed.")
    print("In The End You Will Be Told Whether You Won Or Lost And How Many Total Attempts You Made")
    print("\n Noticed Something ? You Will Be Told How Many Not Which 🔥")
    print("And If You Entered Wrong Length Code Your Live Will Be Deducted For That Too")


    count = 0
    lives = 9

    print(f"Now You Have {lives} Lives In Medium Level")
    user_guess = input("\nGuess The Code : ")
    lives -= 1
    count += 1

    while(len(user_guess) != len(com_num) and lives > 0):
        print(f"Your Guess Must Be {len(com_num)} Digits Long")
        user_guess = input("Guess The Code Again Please : ")
        count += 1
        lives -= 1

    while(user_guess != com_num and lives > 0):
        correct_count = 0
        wrong_position_count = 0

        already_exist_list = [
            user_guess[i]
            for i in range(len(com_num))
            if user_guess[i] == com_num[i]
        ]

        for i in range(len(com_num)):
            check = user_guess[i] == com_num[i]

            if(check):
                correct_count += 1
            else:
                if(user_guess[i] in com_num and already_exist_list.count(user_guess[i]) < com_num.count(user_guess[i])):
                    already_exist_list.append(user_guess[i])
                    wrong_position_count += 1
        print(f"\nFor Code {user_guess} : \n  {correct_count} Digits Are Correct And Placed Correctly \n  {wrong_position_count} Digits Are Correct But Placed Wrong")
        print(f"\nNow You Have {lives} Lives Left")
        user_guess = input("Guess The Code Again : ")
        lives -= 1
        count += 1
        while(len(user_guess) != len(com_num) and lives > 0):
            print(f"Your Guess Must Be {len(com_num)} Digits Long")
            print(f"Now You Have {lives} Lives Left")
            user_guess = input("Guess The Code Again Please : ")
            lives -= 1
            count += 1


    if (user_guess == com_num):
        print("---------------------------")
        print(" Congratulations , You Won")
        print(f" You took {count} attempts")
        print("---------------------------")
    else:
        print("--------------------------------------------")
        print(" You Lost Because You Wasted All Your Lives")
        print("--------------------------------------------")


def level_hard(com_num):

    print("------- Level Hard -------")
    print("Instructions \nAs It Is Hard Level , You Will Have Very Limited Chances We Call Them Lives To Guess The Correct Code")
    print("After every guess, you will only be told the total number of correct digits in your guess.")
    print("In The End You Will Be Told Whether You Won Or Lost And How Many Total Attempts You Made")
    print("\nLittle Favour : As It Is Hard Level , On The Guess Of Wrong Length's Code Your Live Won't Be Deducted")

    lives = 3
    count = 0


    print(f"Now You Have {lives} Lives In Hard Level")
    user_guess = input("Guess The Code : ")
    count += 1

    while(len(user_guess) != len(com_num)):
        print(f"Your Guess Must Be {len(com_num)} Digits Long")
        user_guess = input("Guess The Code Again Please : ")
        count += 1

    lives -= 1
    
    while(user_guess != com_num and lives > 0):
        correct_count = 0

        already_exist_list = [
            user_guess[i]
            for i in range(len(com_num))
            if user_guess[i] == com_num[i]
        ]

        for i in range(len(com_num)):
            check = user_guess[i] == com_num[i]

            if(check):
                correct_count += 1
            else:
                if(user_guess[i] in com_num and already_exist_list.count(user_guess[i]) < com_num.count(user_guess[i])):
                    already_exist_list.append(user_guess[i])
                    correct_count += 1
        print(f"\nFor Code {user_guess} : \n  {correct_count} Digits Are Correct \n  Now You Have {lives} Lives Left")
        user_guess = input("\nGuess The Code Again : ")
        count += 1
        while(len(user_guess) != len(com_num) and lives > 0):
            print(f"Your Guess Must Be {len(com_num)} Digits Long")
            user_guess = input("Guess The Code Again Please : ")
            count += 1
        lives -= 1


    if (user_guess == com_num):
        print("---------------------------")
        print(" Congratulations , You Won")
        print(f" You took {count} attempts")
        print("---------------------------")
    else:
        print("--------------------------------------------")
        print(" You Lost Because You Wasted All Your Lives")
        print("--------------------------------------------")



# Main Execution Code

user_num = int(input("How Many Digit's Code  You Want : "))
print(f"You Chose {user_num} Digit Code")


com_num = str(random.randint(10 ** (user_num - 1), 10**user_num - 1))

cheat_var = input("Do You Want To Reveal The Computer's Code ? (y/n): ").lower()
if(cheat_var == "y"):
    print(f"The Computer's Code Is {com_num}")
elif(cheat_var == "n"):
    print("Great! Let's Make The Game Interesting Without Revealing The Answer")
else:
    print("Oh, I See! You Didn't Enter 'y' or 'n'. Okay, We Won't Reveal The Answer")

print("Try to guess the number in as few attempts as possible!")
print("\n1 For Easy , 2 For Medium , 3 For Hard")
while True:
    try:
        user_choice = int(input("Enter Difficulty Level : "))
        if user_choice == 1:
            level_easy(com_num)
            break
        elif user_choice == 2:
            level_medium(com_num)
            break
        elif user_choice == 3:
            level_hard(com_num)
            break
        else:
            print("Invalid choice! Choose between 1, 2, or 3.")
    except ValueError:
        print("Please enter a valid number.")
