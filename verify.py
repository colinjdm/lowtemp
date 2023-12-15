from figlet import neat_text

def main():
    neat_text('Verify')
    print(verify(input("Are you telling the truth? ")))


def verify(text):
    if text == 'yes':
        return 'Verified'
    else:
        return 'NOPE'


if __name__ == "__main__":
    main()