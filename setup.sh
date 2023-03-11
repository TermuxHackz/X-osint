# /bin/bash 
  
  cls || clear
 # banner
echo -e "\033[1;91m
                                                                 
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
 Version: 0.1
   \033[0m"
   echo
	printf "\e[1;34m\tInstall the packages for your Terminal \e[0m\n\n"
	printf "\e[1;34m\t\t[\e[0m\e[1;77m01\e[0m\e[1;34m]\e[0m\e[1;93mTermux\e[0m\n"
printf "\e[1;34m\t\t[\e[0m\e[1;77m02\e[0m\e[1;34m]\e[0m\e[1;93mLinux\e[0m\n"
read -p $'\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Choose your terminal: \e[0m\en' terminal

if [[ $terminal == "1" || $terminal == "01" ]]; then
printf "\e[1;94mYou have choosen Termux as your current terminal packages for Termux will Start to install... \e[0m\n"
sleep 3
clear || cls
echo -e "\033[1;91m[*] \033[1;97m Allow file permission\033[0m"
echo 
echo -e "\033[1;91m[*]\033[1;97m Installing Required Packages\033[0m"
echo 
echo -e "\033[1;91m[*]\033[1;97m Updating Termux\033[0m"
echo
pkg update -y
echo
echo -e "\033[1;91m[*]\033[1;97m Upgrading Termux\033[0m"
pkg upgrade -y
echo
echo -e "\033[1;91m[*]\033[1;97m Installing All Packages one-time\033[0m"
pkg install git -y
pkg install python -y
pkg install wget -y
pkg install curl -y 
pkg install python3
python3 -m pip install --upgrade pip
pip install lolcat 
pip install requests
pip install ip2geotools
echo
echo -e "\033[1;91m[*]\033[1;97m Setting up environment \033[0m"
echo
rm -rf /data/data/com.termux/X-osint/ 
 mkdir /data/data/com.termux/X-osint/ 
 touch xosint
 echo 'python /data/data/com.termux/X-osint/xosint.py' >> xosint
 chmod +x xosint
 mv xosint /data/data/com.termux/files/usr/bin 
 cp xosint.py /data/data/com.termux/X-osint
 cp README.md /data/data/com.termux/X-osint
 cd .. 
 rm -rf X-osint
 echo 
 echo -e "\033[1;91m[*]\033[1;97m X-osint Installed Successfully, Now its ready for use. So re-open your Termux To use X-osint" 
 echo -e "\033[1;91m[*]\033[1;97m After reopen your termux just type '\033[1;91mxosint\033[1;97m' to launch X-osint" 
 echo 
 exit
 
 elif [[ $terminal == "02" || $terminal == "2" ]]; then
printf "\e[1;94mYou have choosen Linux as your current terminal packages for Linux will Start to install... \e[0m\n"
sleep 3
clear || cls 
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get -y install ssh
sudo apt-get -y install curl
sudo apt-get -y install php
sudo pip install lolcat
sudo pip install ip2geotools
sleep 2
printf "\e[1;94mSetting up environment for Linux .. \e[0m\n"				
sleep 2
rm -rf /$HOME/X-osint/ 
 mkdir /$HOME/X-osint/ 
 touch xosint
 echo 'python /$HOME/X-osint/xosint.py' >> xosint
 chmod +x xosint
 mv xosint /$HOME/usr/bin 
 cp xosint.py /$HOME/X-osint
 cp README.md /$HOME/X-osint
 cd .. 
 rm -rf X-osint
 echo 
 echo -e "\033[1;91m[*]\033[1;97m X-osint Installed Successfully, Now its ready for use. So re-open your Linux Terminal To use X-osint" 
 echo -e "\033[1;91m[*]\033[1;97m After reopen your terminal just type '\033[1;91mxosint\033[1;97m' to launch X-osint" 
 echo 
 exit
else 
printf "\e[0m\e[1;91m [\e[1;97m~\e[1;91m]\e[1;93m Sorry, lol thats not in the option 😂....open up your eyes..!!. \e[0m\e[1;91m[\e[0m\e[1;97m~\e[0m\e[1;91m]\e[0m\n"
sleep 2
clear || cls
bash setup.sh
fi