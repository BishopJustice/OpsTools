"""Takes a selection of phone numbers and formats them the same. Offers optional SQL readying."""

import pyperclip
import re


def phone_format(phone_number):
    clean_phone_number = str(1) + re.sub('[^0-9]+', '', phone_number)
    formatted_phone_number = re.sub(
        "(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(clean_phone_number[:-1])) + clean_phone_number[-1]
    return clean_phone_number


def sqler(lines):
    lines = lines.splitlines()

    for i in range(len(lines) - 1):
        lines[i] = "\'+" + lines[i] + "',"
    lines[-1] = "\'" + lines[-1] + "'"

    for i in lines:
        if i == "'',":
            lines.remove(i)

    new = '\n'.join(lines)
    pyperclip.copy(new)


data = pyperclip.paste()
numbers = data.splitlines()

clean_numbers = []

for i in numbers:
    if i == '':
        numbers.remove(i)

for each in numbers:
    clean_numbers.append(phone_format(each))

end = '\n'.join(clean_numbers)
pyperclip.copy(end)


sql = raw_input(
    'Numbers copied to clipboard. Would you like to ready it for SQL? (Y/N)')

if sql == 'y':
    sqler(end)
    print ("Your list is ready on your clipboard and ready for a SQL report")
else:
    print ('Your list is ready, if you want to add sql brackets, use SQLer.py')
