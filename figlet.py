import random

from pyfiglet import Figlet

figlet = Figlet()


def main():
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(input("Text for random font: ")))
    print(f)


def slant(s):
    font = Figlet('slant')
    print(font.renderText(s))


def bloody(s):
    font = Figlet('bloody')
    print(font.renderText(s))


def small(s):
    font = Figlet('small')
    print(font.renderText(s))


if __name__ == "__main__":
    main()