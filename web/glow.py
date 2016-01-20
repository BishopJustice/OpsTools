import webbrowser
items = ('https://docs.google.com/document/d/1QyVYSFacdhgA3zW3xzTcViom8fms64nh7GJjRjFICMs/edit',
'https://modeanalytics.com/lyft/reports/72cbe597dcda?trk_srch_pos=0',
'https://modeanalytics.com/lyft/reports/b10ca756dca0',
'https://docs.google.com/spreadsheets/d/1iz8-mDNDkTEYySeHiwl1PoWu-EROCVZ5ir5U6L1v8b8/edit#gid=1140078119',
'https://docs.google.com/spreadsheets/d/1RNCtzbaBKtvkEl1NGAduik65VF5ImXZW7DXV_kNPoio/edit#gid=1881908563')
for item in items:
	webbrowser.open_new(item)
