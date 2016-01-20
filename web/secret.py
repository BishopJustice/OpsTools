import webbrowser
sites = ('https://www.lucidchart.com/documents/edit/9e2be758-c1ba-42c9-87ae-8064068721c2#','https://docs.google.com/document/d/148sIJilp9LA4NUDc59Y2vnFK_h8iVAy5Kgx-8TuM5gU/edit?ts=564e533a','https://docs.google.com/spreadsheets/d/1VEvEG-ZqmC-ceFmBIilI-wXo7EzMTGgu7PKk-b6L0_Y/edit#gid=0', 'https://docs.google.com/spreadsheets/d/1gyVEzNe6UmKEHTW4oyeRnwI_OFtKdM_YFaeNIbbmGVo/edit?ts=566773bf#gid=0', 'https://modeanalytics.com/editor/lyft/reports/05c752bedb03')
webbrowser.open_new(sites[0])
for each in sites[1:]:
	webbrowser.open(each)
