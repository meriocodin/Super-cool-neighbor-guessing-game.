print("Welcome to guess your neighbours name!")
neighbour_true = 'john'
neighbour_guess = input("Please enter your neighbours name: ").lower()
attempts = 3

while neighbour_true != neighbour_guess and attempts > 0:
    print("You guessed wrong! Please try again.")
    neighbour_guess = input("Enter a new name: ").lower()
    attempts -= 1
    print(f"Now you have {attempts} attempts. Think harder!")

if neighbour_guess == neighbour_true:
    print("Good job, you guessed your neighbours name!")
else:
    print("You run out of attempts.")