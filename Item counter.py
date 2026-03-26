# Author: Kael
# Date: 2026-03-26
# Program Title: Item Counter - Count Names in File

def main():
    try:
        count = 0
        with open("names.txt", "r") as file:
            for line in file:
                count += 1

        print(f"Number of names in the file: {count}")

    except IOError:
        print("An error occurred while trying to read the file.")

if __name__ == "__main__":
    main()
