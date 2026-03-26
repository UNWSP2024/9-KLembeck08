# Author: Kael
# Date: 2026-03-26
# Program Title: Random Number File Writer

import random

def main():
    try:
        amount = int(input("How many random numbers should be written (1–1000)? "))

        if amount < 1 or amount > 1000:
            print("Please enter a number between 1 and 1000.")
            return

        with open("random_numbers.txt", "w") as file:
            for _ in range(amount):
                number = random.randint(1, 500)
                file.write(str(number) + "\n")

        print("Random numbers successfully written to random_numbers.txt")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
