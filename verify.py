import sys

def main():
    print(verify(input("Text: ")))


def verify(text):
    if text == 'true':
        return 'Verified'


if __name__ == "__main__":
    main()