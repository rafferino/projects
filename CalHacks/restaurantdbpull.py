import os

def terminalcommand():
	for i in range(0, 39848, 100):
		os.system("curl -i -X GET \
		-H 'Content-Type:application/json' \
		-H 'Authorization:bearer 93f3db26-0929-4a96-9d27-3661cbbfb370' \
		'https://platform.otqa.com/sync/directory?limit=100&offset={}' >>restaurant1.json".format(i))

terminalcommand()