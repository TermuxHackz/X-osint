#!/usr/bin/python3

  
 #Importing modules and libraries
import os
import time
import socket
import requests
from time import sleep
import sys
import json
from PIL import Image
from PIL.ExifTags import TAGS
import piexif

banner = """\033[1;91m
▒██   ██▒ ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▒▒ █ █ ▒░▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
░░  █   ░▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
 ░ █ █ ▒ ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
▒██▒ ▒██▒░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
▒▒ ░ ░▓ ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
░░   ░▒ ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
 ░    ░  ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
 ░    ░      ░ ░        ░   ░           ░          
                            
        Created by: AnonyminHack5
        Team: TermuxHackz Society
        	Version: 2.0
\033[0m"""

main_menu = """
	\033[1;91m[??] Choose an option:
	\033[1;91m[1] \033[1;97m IP Address Information
	\033[1;91m[2] \033[1;97m Email Address Information
	\033[1;91m[3] \033[1;97m Phone Number Information
	\033[1;91m[4] \033[1;97m Host Search
	\033[1;91m[5] \033[1;97m Ports
	\033[1;91m[6] \033[1;97m Exploit CVE
	\033[1;91m[7] \033[1;97m Exploit Open Source Vulnerability Database 
	\033[1;91m[8] \033[1;97m DNS Lookup
	\033[1;91m[9] \033[1;97m DNS Reverse
        \033[1;91m[10] \033[1;97mEmail Finder
        \033[1;91m[11] \033[1;97mExtract Metadata from image
        \033[1;91m[12]\033[1;97m Check Twitter Status
        \033[1;91m[13]\033[1;97m Subdomain Enumeration
	\033[1;91m[u] \033[1;97m Update X-osint
	\033[1;91m[0] \033[1;97m About
	\033[1;91m[q] \033[1;97m Quit
	
	"""
about = """\033[1;91m
This is an osint tool which gathers useful and yet credible valid information about a phone number, user email address and ip address and more to come in other future updates
\033[0m"""
def traceip():
	targetip = input("\033[1;91mEnter IP Address: \033[0m")
	r = requests.get("http://ip-api.com/json/" + targetip)
	print("\n\033[1;91m[*]\033[1;97m IP detail is given down below\n")
	#print()
	sleep(0.1)
	print("\033[1;92m \033[1;91m➤\033[1;97m Status Code    : " + str(r.status_code))
	sleep(0.1)
	if str(r.json() ['status']) == 'success':
		print(" \033[1;91m➤\033[1;97m Status         :\033[1;92m " + str(r.json() ['status']))
		sleep(0.1)
	elif str(r.json() ['status']) == 'fail':
		print(" \033[1;91m➤\033[1;97m Status         :\033[1;97m " + str(r.json() ['status']) + '\033[1;92m')
		sleep(0.1)
		print(" \033[1;91m➤\033[1;97m Message        : " + str(r.json() ['message']))
		sleep(0.1)
		if str(r.json() ['message']) == 'invalid query':
			print('\n\033[1;91m[!] \033[1;97m' + targetip + ' is an invalid IP Address, So you can try another IP Address.\n')
			exit()
		elif str(r.json() ['message']) == 'private range':
			print('\n\033[1;91m[!] \033[1;97m' + targetip + ' is a private IP Address, So This IP can not be traced.\n')
			exit()
		elif str(r.json() ['message']) == 'reserved range':
			print('\n\033[1;91m[!] \033[1;97m' + targetip + ' is a reserved IP Address, So This IP can not be traced.\n')
			exit()
		else:
			print('\nCheck your internet connection.\n')
			exit()
	print("\033[1;92m \033[1;91m➤\033[1;97m Target IP      : " + str(r.json() ['query'] ))
	sleep(0.1)
	print("\033[1;92m \033[1;91m➤\033[1;97m Country:	: " + str(r.json() ['country'] ))
	sleep(0.1)
	print(" \033[1;92m\033[1;97m➤\033[1;97m Country Code    : " + str(r.json() ['countryCode']))
	sleep(0.1)
	print(" \033[1;92m\033[1;97m➤\033[1;97m City   	: " + str(r.json() ['city']))
	sleep(0.1)
	print(" \033[1;92m\033[1;97m➤\033[1;97m Timezone    	: " + str(r.json() ['timezone']))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Region Name    : " + str(r.json() ['regionName'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Region         : " + str(r.json() ['region'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m ZIP Code       : " + str(r.json() ['zip'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Latitude       : " + str(r.json() ['lat'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Longitude      : " + str(r.json() ['lon'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m ISP            : " + str(r.json() ['isp'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Organization   : " + str(r.json() ['org'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m AS             : " + str(r.json() ['as'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Location       : " + str(r.json() ['lat']) + ',' + str(r.json() ['lon']))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Google Map     : \033[1;94mhttps://maps.google.com/?q=" + str(r.json() ['lat']) + ',' + str(r.json() ['lon']))
	sleep(0.1)
	print()
	mapaddress = input("\033[1;91m[*]\033[1;97m Press ENTER To Open Location on Google maps or press any other key to quit: ")
	if mapaddress == "":
		print()
		print("[*] Opening Location on google map")
		print()
		os.system("xdg-open https://maps.google.com/?q=" + str(r.json() ['lat']) + ',' + str(r.json() ['lon']) + " > /dev/null 2>&1")
		print()
	else:
		print()
		print("[*] Aborting.....")
		print()

###email address information gathering
def email_info():
	mailid = input("\033[1;91m Enter email address: \033[1;94m")
	eml = requests.get("https://ipqualityscore.com/api/json/email/pPiATkSdtLn3xgKW7a7HikZeZ4HMNa2R/" + mailid )
	print()
	sleep(1)
	print()
	print("\033[1;91m[~]\033[1;97m E-mail Details are given down below")
	print()
	print("\033[1;91m➤\033[1;97m Target E-mail       : " + str(mailid) )
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Status Code         : " + str(eml.status_code) )
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Valid               : " + str(eml.json() ['valid']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Catch All           : " + str(eml.json() ['catch_all']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Common              : " + str(eml.json() ['common']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Deliverability      : " + str(eml.json() ['deliverability']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Disposable          : " + str(eml.json() ['disposable']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m DNS Valid           : " + str(eml.json() ['dns_valid']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Fraud Score         : " + str(eml.json() ['fraud_score']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Frequent Complainer : " + str(eml.json() ['frequent_complainer']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Generic             : " + str(eml.json() ['generic']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Honeypot            : " + str(eml.json() ['honeypot']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Leaked              : " + str(eml.json() ['leaked']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Message             : " + str(eml.json() ['message']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Over All Score      : " + str(eml.json() ['overall_score']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Recent Abuse        : " + str(eml.json() ['recent_abuse']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Request ID          : " + str(eml.json() ['request_id']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Sanitized E-mail    : " + str(eml.json() ['sanitized_email']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m SMTP Score          : " + str(eml.json() ['smtp_score']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Spam Trap Score     : " + str(eml.json() ['spam_trap_score']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Success             : " + str(eml.json() ['success']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Suggested Domain    : " + str(eml.json() ['suggested_domain']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Suspect             : " + str(eml.json() ['suspect']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Timed Out           : " + str(eml.json() ['timed_out']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m First Name          : " + str(eml.json() ['first_name']))
	sleep(0.1)
	print()
	print("\033[1;91m[~]\033[1;94m Domain Age")
	print()
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Human      : " + str(eml.json() ['domain_age'] ['human']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m ISO        : " + str(eml.json() ['domain_age'] ['iso']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Time Stamp : " + str(eml.json() ['domain_age'] ['timestamp']))
	sleep(0.1)
	print()
	print("\033[1;91m[~]\033[1;94m First Seen")
	print()
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Human      : " + str(eml.json() ['first_seen'] ['human']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m ISO        : " + str(eml.json() ['first_seen'] ['iso']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Time Stamp : " + str(eml.json() ['first_seen'] ['timestamp']))
	sleep(0.1)
	print()
def phone_info():
	mobileno = input("\033[1;91m Enter phone number with country code: \033[1;94m")
	phe = requests.get("https://ipqualityscore.com/api/json/phone/pPiATkSdtLn3xgKW7a7HikZeZ4HMNa2R/" + mobileno )
	sleep(1)
	print()
	print("\033[1;91m[~]\033[1;97m Phone Number Details are given down below")
	print()
	print("\033[1;91m➤\033[1;97m Target Number  : " + mobileno)
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Status Code    : " + str(phe.status_code) )
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Success        : " + str(phe.json() ['success']))
	sleep(0.1)
	print()
	print("\033[1;91m➤\033[1;97m VIP INFO \033[0m")
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Location: ****, ****\033[0m")
	sleep(0.1)
	activation_code = input("\033[1;97mEnter activation code to get Location details (12 characters): \033[0m")
	if activation_code != "b12ch12345BN":
		print("\033[1;97m Invalid Activation Code, Contact me to get it\033[0m")
		sleep(1)
		exit
	else:
		print("\033[1;97m HAHAHAHA!!! Gotacha!!!!Location info feature not available yet...Stay tuned\033[0m")
		exit
#### Update script
def update():
	os.system("clear")
	print(banner)
	print()
	print("\033[1;91m➤\033[1;97m Searching for updates...-> \033[0m\033[1;94mFound")
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Updating.. \033[0m")
	sleep(0.1)
	print()
	print()
	print("\033[1;91m\tSelect your terminal for update \033[0m\n")
	print("\033[1;91m\t[!] PLEASE MAKE SURE YOU CHOOSE CORRECTLY [!] \033[0m\n\n")
	print("\033[1;34m\t\t[\033[0m\033[1;77m1\033[0m\033[1;34m]\033[0m\033[1;93mTermux\033[0m")
	print("\033[1;34m\t\t[\033[0m\033[1;77m2\033[0m\033[1;34m]\033[0m\033[1;93mLinux\033[0m\n")
	update_terminal = input("\033[1;94mChoose: \033[0m")
	
	if update_terminal == "1":
		print("\033[1;97m[+] Updating for termux......\033[0m")
		print()
		sleep(0.1)
		os.system("cd $HOME")
		os.system("cd $PREFIX/bin")
		os.system("rm xosint")
		print("\033[1;97m[+] Validating installation....\033[0m\n")
		sleep(0.1)
		os.system("cd $HOME")
		os.system("git clone https://github.com/TermuxHackz/X-osint")
		print("\033[1;97m[+] Granting permissions.....\033[0m\n")
		os.system("cd X-osint")
		os.system("chmod +x *")
		sleep(0.5)
		print("\033[1;97m[+] Preparing Setup file.....\033[0m\n")
		sleep(0.5)
		print("\033[1;97m[+] Setup file ready!!.....Starting in 2s...\033[0m\n")
		print("\033[1;97m[+] Update completed.....\033[0m\n")
		sleep(2)
		os.system("cd $HOME && cd X-osint")
		os.system("bash setup.sh")
	elif update_terminal == "2":
		print("\033[1;97m[+] Updating for linux......\033[0m")
		print()
		sleep(0.1)
		os.system("cd $HOME")
		os.system("cd /usr/local/bin")
		os.system("sudo rm xosint")
		print("\033[1;97m[+] Validating installation....\033[0m\n")
		sleep(0.5)
		os.system("cd $HOME")
		os.system("git clone https://github.com/TermuxHackz/X-osint")
		print("")
		print("\033[1;97m[+] Granting permissions.....\033[0m\n")
		os.system("cd X-osint")
		os.system("chmod +x *")
		sleep(0.5)
		print("\033[1;97m[+] Preparing Setup file.....\033[0m\n")
		sleep(0.5)
		print("\033[1;97m[+] Setup file ready!!.....Starting in 2s...\033[0m\n")
		print("\033[1;97m[+] Update completed.....\033[0m\n")
		sleep(2)
		os.system("cd $HOME && cd X-osint")
		os.system("bash setup.sh")
	else:
		print("Invalid input....KINDLY UPDATE...quiting..")
		sleep(0.5)
		exit
		
#### STart main script
### 4, 5, 6, 7
os.system("clear")
print(banner)
print(main_menu)
option = input("\033[1;91mxosint>> \033[1;97m") 
if option == "1":
	traceip()
elif option == "2":
	email_info()
elif option == "3":
	phone_info()
elif option == "4":
	def shodan_host():
		if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
			with open('api.txt', 'r') as file:
				shodan_api=file.readline().rstrip('\n')
		else:
			file = open('api.txt', 'w')
			shodan_api = input("[+] Please enter a valid Shodan API key (Shodan.io): ")
			file.write(shodan_api)
			print("[+] File written: ./api.txt")
			file.close()
		host_ip = input("\033[1;91m[+]\033[0m\033[1;97mShodan Host Search (IP): \033[0m")
		url = "https://api.shodan.io/shodan/host/"+ host_ip +"?key=" + shodan_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
	shodan_host()
elif option == "5":
	def shodan_ports():
		if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
			with open('api.txt', 'r') as file:
				shodan_api=file.readline().rstrip('\n')
		else:
			file = open('api.txt', 'w')
			shodan_api = input("[+] Please enter a valid Shodan API key (Shodan.io): ")
			file.write(shodan_api)
			print("[+] File written: ./api.txt")
			file.close()
		url = "https://api.shodan.io/shodan/ports?key=" + shodan_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
	shodan_ports()
elif option == "6":
	def shodan_exploit_cve():
		if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
			with open('api.txt', 'r') as file:
				shodan_api=file.readline().rstrip('\n')
		else:
			file = open('api.txt', 'w')
			shodan_api = input("[+] Please enter a valid Shodan API key (Shodan.io): ")
			file.write(shodan_api)
			print("[+] File written: ./api.txt")
			file.close()
		exploit_cve = input("\033[1;91m[+]\033[0m\033[1;97mExploit CVE: \033[0m")
		url = "https://exploits.shodan.io/api/search?query="+ "cve:" + exploit_cve +"&key=" + shodan_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
	shodan_exploit_cve()
elif option == "7":
	def shodan_exploit_osvdb():
		if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
			with open('api.txt', 'r') as file:
				shodan_api=file.readline().rstrip('\n')
		else:
			file = open('api.txt', 'w')
			shodan_api = input("[+] Please enter a valid Shodan API key (Shodan.io): ")
			file.write(shodan_api)
			print("[+] File written: ./api.txt")
			file.close()
		exploit_osvdb = input("\033[1;91m[+]\033[0m\033[1;97mExploit Open Source Vulnerability Database: \033[0m")
		url = "https://exploits.shodan.io/api/search?query="+ "osvdb:" + exploit_osvdb +"&key=" + shodan_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
	shodan_exploit_osvdb()
	
elif option == "8":
	def shodan_dns_lookup():
		if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
			with open('api.txt', 'r') as file:
				shodan_api=file.readline().rstrip('\n')
		else:
			file = open('api.txt', 'w')
			shodan_api = input("[+] Please enter a valid Shodan API key (Shodan.io): ")
			file.write(shodan_api)
			print("[+] File written: ./api.txt")
			file.close()
		hostnames = input("\033[1;91m[+]\033[0m\033[1;97mDNS Lookup: \033[0m")
		url = "https://api.shodan.io/dns/resolve?hostnames="+ hostnames +"&key=" + shodan_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
	shodan_dns_lookup()
	
elif option == "9":
	def shodan_dns_reverse():
		if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
			with open('api.txt', 'r') as file:
				shodan_api=file.readline().rstrip('\n')
		else:
			file = open('api.txt', 'w')
			shodan_api = input("[+] Please enter a valid Shodan API key (Shodan.io): ")
			file.write(shodan_api)
			print("[+] File written: ./api.txt")
			file.close()
		ips = input("\033[1;91m[+]\033[0m\033[1;97mDNS Reverse: \033[0m")
		url = "https://api.shodan.io/dns/reverse?ips="+ ips +"&key=" + shodan_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
	shodan_dns_reverse()

elif option == "10":
	if os.path.exists("./api2.txt") and os.path.getsize("./api2.txt") > 0:
		with open('api2.txt', 'r') as file:
			hunter_api=file.readline().rstrip('\n')
	else:
		file = open('api2.txt', 'w')
		hunter_api = input("[+] Please enter a valid Hunter API key to continue (Get from Hunter.io): ")
		file.write(hunter_api)
		print("[+] File written: ./api2.txt")
		file.close()

	def hunter_email_finder():
		email_domain = input("\033[1;91m[+]\033[0m\033[1;97mDomain: \033[0m")
		first_name = input("\033[1;91m[+]\033[0m\033[1;97mFirst Name: \033[0m")
		last_name = input("\033[1;91m[+]\033[0m\033[1;97mLast Name: \033[0m")
		url = "https://api.hunter.io/v2/email-finder?domain="+ email_domain + "&first_name=" + first_name +"&last_name=" + last_name +"&api_key=" + hunter_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
		hunter_email_finder()
elif option == "11":
	print("\033[1;91m[!]NOTICE:\033[0m\033[1;93m To get a better metadata of the image please do not use images from whatsapp or social media platforms as they strip away metadata from images, also do not use screenshot images, USE IMAGES TAKEN FROM A DEVICE CAMERA THANK YOU [!]\033[0m")
	print()
	imagename = input("\033[1;91m[+]\033[0m\033[1;97m Enter Correct path of the image (JPEG ONLY): \033[0m")
	print("")
	print()
	# open the image
	exif_dict = piexif.load(imagename)
	print(f'Metadata for {imagename}:')
	for ifd in exif_dict:
		print(f'{ifd}:')
		for tag in exif_dict[ifd]:
			tag_name = piexif.TAGS[ifd][tag]["name"]
			tag_value = exif_dict[ifd][tag]
			
			if isinstance(tag_value, bytes):
				tag_value = tag_value[:10]
			print(f'\t{tag_name:25}: {tag_value}')
	print()

		
elif option == "12":
	email_add = input("\033[1;91m[+]\033[0m\033[1;97mEnter email: \033[0m")
	url = "https://api.twitter.com/i/users/email_available.json?email=" + email_add 
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))
			
elif option == "13":
	import resolver
	import threading

	domain = input("\033[1;91m[+]\033[0m\033[1;97mEnter domain name (without www): \033[0m")
	file_path = input("\033[1;91m[+]\033[0m\033[1;97mPath of subdomains lists (Get from my github): \033[0m")
	
	def check_host(self, host):
		is_valid = False
		Resolver = dns.resolver.Resolver()
		Resolver.nameservers = ['1.1.1.1', '1.0.0.1']
		self.lock.acquire()
		try:
			ip = Resolver.query(host, 'A')[0].to_text()
			if ip:
				if self.verbose:
					self_print_("%s%: %s%" % (R, self.engine_name, W, host))
					is_valid = True
					self.live_subdomains.append(host)
		except:
			pass
			self.lock.release()
			return is_valid
	sub_list = open(file_path).read()
	subs = sub_list.splitlines()
	
	for sub in subs:
		domain = f"http://{sub}.{domain}"
		
		try:
			requests.get(domain)
		except requests.ConnectionError:
			pass
		else:
			print("\033[1;94m[+]\033[0m Valid Subdomain: ",domain)
	def domain(self):
		sleep(0.2)
	def __domain__(self):
		t.threading.Thread(target=self.domain)
		t.start()

elif option == "u":
	update()
elif option == "q":
	print()
	exit
elif option == "0":
	print(about)
	exit
else:
	print()
	print("[*] Invalid Input..try again....")
	sleep(0.9)
	os.system("xosint ||sudo xosint")
