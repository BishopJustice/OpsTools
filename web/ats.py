import webbrowser, sys, pyperclip

if len (sys.argv) > 1:
	applicant = ' '.join(sys.argv[1:])
else:
	applicant = pyperclip.paste()

app_list = applicant.splitlines()

choice = input('Please choose ATS (A), TOM (T), or VEHICLE (T). Note that ATS uses applicant_id while TOM uses obscurred_id\n')

if choice.lower() in ['ats', 'a']:
	for each in app_list:
		webbrowser.open('https://ats.lyft.com/#/applicants/' + each)

elif choice.lower() in ['tom', 't']:
	for each in app_list:
		webbrowser.open('https://tom.lyft.net/users/' + each)

elif choice.lower() in ['vehicle', 'v']:
	for each in app_list:
		webbrowser.open('https://tom.lyft.net/users/' + each + '/vehicles')
