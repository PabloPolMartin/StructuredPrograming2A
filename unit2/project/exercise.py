import sys

if __name__ == "__main__":
    str = input("Enter phrase:\n")

    reverse = ''.join(reversed(str.split()))

    print(reverse)