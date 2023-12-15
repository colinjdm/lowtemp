from pyfiglet import Figlet

def neat_text(s):
    font = Figlet('slant')
    # also try 'bloody'
    print(font.renderText(s))