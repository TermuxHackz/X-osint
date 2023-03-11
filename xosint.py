#!/usr//bin/python3

  
 #Importing modules and libraries
import os
import time
import socket
import requests
from time import sleep
import sys

banner = """\033[1;91m
                                                                 
@@@  @@@              @@@@@@    @@@@@@   @@@  @@@  @@@  @@@@@@@  
@@@  @@@             @@@@@@@@  @@@@@@@   @@@  @@@@ @@@  @@@@@@@  
@@!  !@@             @@!  @@@  !@@       @@!  @@!@!@@@    @@!    
!@!  @!!             !@!  @!@  !@!       !@!  !@!!@!@!    !@!    
 !@@!@!   @!@!@!@!@  @!@  !@!  !!@@!!    !!@  @!@ !!@!    @!!    
  @!!!    !!!@!@!!!  !@!  !!!   !!@!!!   !!!  !@!  !!!    !!!    
 !: :!!              !!:  !!!       !:!  !!:  !!:  !!!    !!:    
:!:  !:!             :!:  !:!      !:!   :!:  :!:  !:!    :!:    
 ::  :::             ::::: ::  :::: ::    ::   ::   ::     ::    
 :   ::               : :  :   :: : :    :    ::    :      :     
        Created by: AnonyminHack5
        	Version: 1.0
\033[0m"""
about = """\033[1;91m
This is an osint tool which gathers useful and yet credible valid information about a phone number, user email address and ip address and more to come in other future updates
\033[0m"""
main_menu = """
	\033[1;91m[??] Choose an option:
	\033[1;91m[1] \033[1;97m IP Address Information
	\033[1;91m[2] \033[1;97m Email Address Information
	\033[1;91m[3] \033[1;97m Phone Number Information
	\033[1;91m[0] \033[1;97m About
	\033[1;91m[q] \033[1;97m Quit
	
	"""
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
	print("\033[1;91m➤\033[1;97m Valid          : " + str(phe.json() ['valid']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m VOIP           : " + str(phe.json() ['VOIP']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Active         : " + str(phe.json() ['active']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Active Status  : " + str(phe.json() ['active_status']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Carrier        : " + str(phe.json() ['carrier']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m City           : " + str(phe.json() ['city']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Country        : " + str(phe.json() ['country']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Dialing Code   : " + str(phe.json() ['dialing_code']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Do Not Call    : " + str(phe.json() ['do_not_call']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Formatted      : " + str(phe.json() ['formatted']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Fraud Score    : " + str(phe.json() ['fraud_score']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Leaked         : " + str(phe.json() ['leaked']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Line Type      : " + str(phe.json() ['line_type']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Local Format   : " + str(phe.json() ['local_format']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m MCC            : " + str(phe.json() ['mcc']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Name           : " + str(phe.json() ['name']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Prepaid        : " + str(phe.json() ['prepaid']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Recent Abuse   : " + str(phe.json() ['recent_abuse']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Region         : " + str(phe.json() ['region']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Request ID     : " + str(phe.json() ['request_id']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Risky          : " + str(phe.json() ['risky']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m SMS Domain     : " + str(phe.json() ['sms_domain']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m SMS E-mail     : " + str(phe.json() ['sms_email']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Spammer        : " + str(phe.json() ['spammer']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Success        : " + str(phe.json() ['success']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m TimeZone       : " + str(phe.json() ['timezone']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Zip Code       : " + str(phe.json() ['zip_code']))
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
#### STart main script
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
	os.system("python3 xosint.py ||sudo xosint")