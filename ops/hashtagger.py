'''Copy a list of cells and this will take away all spaces and punctuation and add a # to the beginning'''
import pyperclip
import re


def paste():
    # Pastes your clipboard into a variable and splits it into lines
    text = pyperclip.paste()
    lines = text.splitlines()
    return lines


def clean(item):
    # Gets rid of spaces and all punctuation
    item = '#' + re.sub(r'[^\w\s]', '', item.replace(' ', ''))
    return item


def copy(List):
    # Copies the variable you give it
    text = ', '.join(List)
    pyperclip.copy(text)

tagged = []

for item in paste():
    tagged.append(clean(item))

copy(tagged)
