# Splits dates from times on your clipboard and returns month and year
import pyperclip


times = pyperclip.paste().split('\n')

clean_times = []
for each in times:
	splat = each.split(' ')
	clean_times.append(splat[0])

clean = []
for each in clean_times:
    splat = each.split('/')
    del splat[1]
    new_date = "/".join(splat)
    clean.append(new_date)

final = ('\n').join(clean)
pyperclip.copy(final)
print 'The date is on your clipboard'



