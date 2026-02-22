import random

print("="*10 +" Number Guess   "+"="*10)
best_score= None
while True:
    secret_number=random.randint(1,100)
    attempt=7
    attempt_used=0

    print(" computer has selected a number between 1 and 100 ")
    print(" 7 attempts are provided to guess the secret number ")

    while attempt>0:
        guess=int(input("Enter your guess: "))
        attempt_used=attempt_used+1
        attempt=attempt-1

        if guess==secret_number:
            print("Successfully guessed the secret number ..! ")
            print("You have used ", attempt_used ," attempts ")

            #best score
            if best_score is None or attempt_used< best_score:
                best_score=attempt_used
                print("Youe new best score is  :",best_score)
            break
        elif guess>secret_number:
            print("Guessed number is higher than the secret number !")
        else:
            print("Guessed number is lower than the secret number !")

        # Close hint (within 5)
        if abs(guess - secret_number) <= 5:
            print(" almost near!")
        print("remaining attempts: ",attempt)

    else:
        print(" You guess is wrong ! the secret number was: ",secret_number)
        

#Play again option
    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice != "yes":
        print("Thanks for playing...")
        break