import random

def play_guessing_game():
    target = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if guess < target:
                print("Too low")
            elif guess > target:
                print("Too high")
            else:
                print(f"Correct! You guessed it in {attempts} attempts")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    play_guessing_game()
