# Author: Kael
# Date: 2026-03-26
# Program Title: Average Numbers - Read and Sum Integers from File

def main():
    total = 0
    count = 0

    try:
        with open("numbers.txt", "r") as file:
            for line in file:
                try:
                    number = int(line.strip())
                    total += number
                    count += 1
                except ValueError:
                    print(f"ValueError: Could not convert '{line.strip()}' to an integer.")

        if count > 0:
            print(f"Total of numbers: {total}")
            print(f"Average of numbers: {total / count}")
        else:
            print("No valid numbers found in the file.")

    except IOError:
        print("An error occurred while trying to read the file.")

if __name__ == "__main__":
    main()
