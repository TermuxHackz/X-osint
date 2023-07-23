# /bin/bash 
  
  cls || clear
 # banner
echo -e "\033[1;91m
▒██   ██▒ ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▒▒ █ █ ▒░▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
░░  █   ░▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
 ░ █ █ ▒ ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
▒██▒ ▒██▒░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
▒▒ ░ ░▓ ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
░░   ░▒ ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
 ░    ░  ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
 ░    ░      ░ ░        ░   ░           ░     
   An Open Source Intelligence Framework  
     Created by: AnonyminHack5
     Team: TermuxHackz Society
 Version: \033[1;92m2.1
   \033[0m"
   echo
	printf "\e[1;34m\tSelect your terminal to install X-osint \e[0m\n"
	printf "\e[1;91m\t[!] PLEASE MAKE SURE YOU CHOOSE CORRECTLY [!] \e[0m\n\n"
	printf "\e[1;34m\t\t[\e[0m\e[1;77m01\e[0m\e[1;34m]\e[0m\e[1;93mTermux\e[0m\e[1;91m [STABLE]\e[0m\n"
printf "\e[1;34m\t\t[\e[0m\e[1;77m02\e[0m\e[1;34m]\e[0m\e[1;93mLinux\e[0m\n"
read -p $'\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Choose your terminal: \e[0m\en' terminal

if [[ $terminal == "1" || $terminal == "01" ]]; then
printf "\e[1;94mYou have choosen Termux as your current terminal packages for Termux will Start to install... \e[0m\n"
sleep 3
clear || cls
echo -e "\033[1;91m[*] \033[1;97m Allow file/move permission\033[0m"
echo
termux-setup-storage
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
pkg install python3
echo
echo -e "\033[1;91m[*]\033[1;97m Installing tor \033[0m"
pkg install tor
echo
echo -e "\033[1;91m[*]\033[1;97m Installing Requests\033[0m"
echo
pip install requests
echo
echo -e "\033[1;91m[*]\033[1;97m Installing Pillow\033[0m"
echo
pip install pillow==2.2.1
echo
echo -e "\033[1;91m[*]\033[1;97m Installing resolver\033[0m"
pip install resolver
echo
echo -e "\033[1;91m[*]\033[1;97m Installing piexif\033[0m"
pip install piexif
echo
echo -e "\033[1;91m[*]\033[1;97m Removing old packages\033[0m" 
python3 -m pip uninstall googlesearch-python -y
python3 -m pip uninstall google-search -y
python3 -m pip uninstall google -y
echo
echo -e "\033[1;91m[*]\033[1;97m Installing google\033[0m" 
pip install google
echo
echo -e "\033[1;91m[*]\033[1;97m Installing libxslt\033[0m"
pkg install libxslt
echo
echo -e "\033[1;91m[*]\033[1;97m Installing IMDb [Might take a while, please be patient]\033[0m"
pip install IMDbPY
pip install imdbpy
echo 
echo -e "\033[1;91m[*]\033[1;97m Installing Cinemagoer \033[0m"
pip install cinemagoer
echo
echo -e "\033[1;91m[*]\033[1;97m Installing prompt-toolkit\033[0m"
pip install prompt-toolkit
echo
echo -e "\033[1;91m[*]\033[1;97m Installing vininfo\033[0m"
pip install vininfo
echo
echo -e "\033[1;91m[*]\033[1;97m Installing tkinter\033[0m"
pip install tk-tools
echo
echo -e "\033[1;91m[*]\033[1;97m Installing phonenumbers\033[0m"
pip install phonenumbers
echo

echo -e "\033[1;91m[*]\033[1;97m Installing colorama\033[0m"
pip install colorama
echo
echo -e "\033[1;91m[*]\033[1;97m Installing folium\033[0m"
pip install folium
echo
echo -e "\033[1;91m[*]\033[1;97m Installing opencage\033[0m"
pip install opencage
echo
echo -e "\033[1;91m[*]\033[1;97m Installing Find github\033[0m"
pip install find-github-email
echo
echo -e "\033[1;91m[*]\033[1;97m Installing BeautifulSoup4\033[0m"
pip install bs4
echo
echo -e "\033[1;91m[*]\033[1;97m Setting up environment \033[0m"
echo
cp -r xosint $PREFIX/bin
cp -r subdomains.txt $PREFIX/bin
cd $PREFIX/bin && chmod u+x xosint
cd $PREFIX/bin && chmod u+x subdomains.txt
cd $HOME
rm -rf X-osint
printf "\e[1;91m[*]\e[1;97m X-osint Installed Successfully, Now its ready for use. So re-open your Termux To use X-osint\e[0m\n" 
printf "\e[1;91m[*]\e[1;97m After reopen your termux just type '\e[1;91mxosint\e[1;97m' to launch X-osint \e[0m" 
exit
 
 elif [[ $terminal == "02" || $terminal == "2" ]]; then
printf "\e[1;94mYou have choosen Linux as your current terminal packages for Linux will Start to install... \e[0m\n"
sleep 2
clear || cls 
echo -e "\033[1;91m[*]\033[1;97m Updating Linux\033[0m"
sudo apt-get update
echo
echo -e "\033[1;91m[*]\033[1;97m Upgrading Linux\033[0m"
sudo apt-get upgrade -y
echo
echo -e "\033[1;91m[*]\033[1;97m Installing tor \033[0m"
sudo apt install tor -y
echo 
echo -e "\033[1;91m[*]\033[1;97m Installing Lolcat\033[0m"
echo
pip install lolcat
echo
echo -e "\033[1;91m[*]\033[1;97m Installing Pillow\033[0m"
echo
pip install pillow==2.2.1
echo
echo -e "\033[1;91m[*]\033[1;97m Installing resolver\033[0m"
echo
pip install resolver
echo
echo -e "\033[1;91m[*]\033[1;97m Installing piexif\033[0m"
pip install piexif
sleep 1
echo
echo -e "\033[1;91m[*]\033[1;97m Removing old packages\033[0m" 
sudo python3 -m pip uninstall googlesearch-python -y
sudo python3 -m pip uninstall google-search -y
sudo python3 -m pip uninstall google -y
echo
echo -e "\033[1;91m[*]\033[1;97m Installing google\033[0m" 
sudo pip install google
echo
echo -e "\033[1;91m[*]\033[1;97m Installing IMDb\033[0m" 
pip install IMDbPY
pip install imdbpy
echo
echo -e "\033[1;91m[*]\033[1;97m Installing Cinemagoer \033[0m"
pip install cinemagoer
echo
echo -e "\033[1;91m[*]\033[1;97m Installing prompt-toolkit\033[0m"
pip install prompt-toolkit
echo
echo -e "\033[1;91m[*]\033[1;97m Installing phonenumbers\033[0m"
pip install phonenumbers
echo
echo -e "\033[1;91m[*]\033[1;97m Installing colorama\033[0m"
pip install colorama
echo
echo -e "\033[1;91m[*]\033[1;97m Installing BeautifulSoup4\033[0m"
pip install bs4
echo

echo -e "\033[1;91m[*]\033[1;97m Installing Find github\033[0m"
pip install find-github-email
echo
echo -e "\033[1;91m[*]\033[1;97m Installing folium\033[0m"
pkg install python-numpy
pip install folium
echo
echo -e "\033[1;91m[*]\033[1;97m Installing opencage\033[0m"
pip install opencage
echo
echo -e "\033[1;91m[*]\033[1;97m Installing vininfo\033[0m"
pip install vininfo
echo
echo -e "\033[1;91m[*]\033[1;97m Installing tkinter\033[0m"
pip install tk-tools
echo
printf "\e[1;94mSetting up environment for Linux .. \e[0m\n"				
sleep 1
echo
sudo cp -r xosint /usr/local/bin
cd /usr/local/bin && sudo chmod u+x xosint
cd $HOME && sudo rm -rf X-osint
 printf "\e[1;91m[*]\e[1;97m X-osint Installed Successfully, Now its ready for use. So re-open your Linux Terminal To use X-osint\e[0m\n"
 echo
 echo
 printf "\e[1;91m[*]\e[1;97m After reopen your terminal just type '\e[1;91msudo xosint\e[1;97m' to launch X-osint \e[0m" 
 echo ""
 exit
else 
printf "\e[0m\e[1;91m [\e[1;97m~\e[1;91m]\e[1;93m Sorry, lol thats not in the option 😂....open up your eyes..!!. \e[0m\e[1;91m[\e[0m\e[1;97m~\e[0m\e[1;91m]\e[0m\n"
sleep 1
clear || cls
bash setup.sh
fi
