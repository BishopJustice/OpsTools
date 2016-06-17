''' Copy a list of cells to your clipboard and this will add commas in between them'''

import pyperclip


def paste():
    text = pyperclip.paste()
    lines = text.splitlines()
    return lines


def commaFormat(items):
    for i in range(len(items) - 1):
        items[i] = items[i] + ","
    return items


def removeBlank(items):
    for i in items:
        if i == "\n":
            items.remove(i)
    return items


def copy(items):
    text = ''.join(items)
    pyperclip.copy(text)


copy(commaFormat(paste()))


