import random
top_of_range=int(input("enter a top of range: "))
target_number = random.randint(0,top_of_range+1)
num_of_guesses=0
while True:
    num_of_guesses+=1
    user_guess=int(input("Guess the number: "))
    if user_guess==target_number:
        print("You Guessed it right!!")
        break
    elif user_guess<target_number:
        print("Your Guess is lessthan target value!")
    else:
        print("Your Guess is Greaterthan target value!")  

print("You got it",num_of_guesses,"guesses.")
