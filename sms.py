import requests
import subprocess
subprocess.call(["figlet","fake","number"])
while True:
	destination_number = input("enter destination number : ")
	message = input("enter your message : ")
	if "" in destination_number and message == "":
		break
	response = requests.post("https://textbelt.com/text",{
	
		'phone':'{}'.format(destination_number),
		'message':'{}'.format(message),
		'key':'textbelt',
	})
	print(response.json())							
	exit = input("enter q or Q to exit : ")
	if exit == 'q' or 'Q':
		break
	
