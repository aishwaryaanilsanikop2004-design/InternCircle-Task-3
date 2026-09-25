import random
from collections import Counter

def number_guessing_game():
    print("\n===== NUMBER GUESSING GAME =====")
    print("I have chosen a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0
    score = 100

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess == secret_number:
                score = max(10, 100 - (attempts - 1) * 10)
                print(f"Correct! You guessed it in {attempts} attempts.")
                print(f"Your score: {score}")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

def word_counter():
    print("\n===== WORD COUNTER =====")
    filename = input("Enter text file name (press Enter for words.txt): ").strip()

    if not filename:
        filename = "words.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()

        words = text.split()
        clean_words = []

        for word in words:
            cleaned = "".join(ch for ch in word if ch.isalnum())
            if cleaned:
                clean_words.append(cleaned)

        frequency = Counter(clean_words)

        print(f"\nTotal words: {len(clean_words)}")
        print(f"Unique words: {len(frequency)}")
        print("\nWord frequency:")
        for word, count in frequency.most_common():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"File '{filename}' was not found.")
        print("Make sure the text file is in the same folder as main.py.")

def main():
    while True:
        print("\n===================================")
        print(" NUMBER GUESSING GAME & WORD COUNTER")
        print("===================================")
        print("1. Play Number Guessing Game")
        print("2. Count Words from Text File")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
