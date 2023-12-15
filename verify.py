import figlet


def main():
    figlet.slant('Verify')
    verify(input("Are you telling the truth? "))


def verify(text):
    if text == 'yes':
        print(figlet.small('Congrats, youre verified'))
    else:
        print(figlet.bloody('GET OUT'))


if __name__ == "__main__":
    main()

    ####