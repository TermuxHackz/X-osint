# /bin/bash

  cls || clear
echo -e "\033[38;5;208m
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
 Version: \033[1;92m2.3
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
echo -e "\033[1;91m[*]\033[1;97m Installing Python, Tor and Tkinter\033[0m"
pkg install -y python tor python-tkinter libxslt python-numpy
echo
echo -e "\033[1;91m[*]\033[1;97m Installing pip dependencies from requirements.txt\033[0m"
echo
pip install --upgrade pip
pip install -r requirements.txt
echo
echo -e "\033[1;91m[*]\033[1;97m Downloading spaCy language model\033[0m"
python -m spacy download en_core_web_sm --break-system-packages
echo
echo -e "\033[1;91m[*]\033[1;97m Installing Cinemagoer\033[0m"
pip install cinemagoer
echo
echo -e "\033[1;91m[*]\033[1;97m Installing vininfo\033[0m"
pip install vininfo
echo
echo -e "\033[1;91m[*]\033[1;97m Installing find-github-email\033[0m"
pip install find-github-email
echo
echo -e "\033[1;91m[*]\033[1;97m Setting up environment \033[0m"
echo
if [ -f xosint ] && [ -f setup.sh ]; then
cp -r xosint $PREFIX/bin && \
cp -r subdomains.txt $PREFIX/bin && \
cp -r templates $PREFIX/bin && \
cp -r static $PREFIX/bin && \
chmod u+x $PREFIX/bin/xosint && \
chmod u+x $PREFIX/bin/subdomains.txt && \
chmod u+x $PREFIX/bin/templates && \
chmod u+x $PREFIX/bin/static
if [ $? -eq 0 ]; then
REPO_DIR=$(pwd)
cd ..
rm -rf "$REPO_DIR"
fi
fi
printf "\e[1;91m[*]\e[1;97m X-osint Installed Successfully, Now its ready for use. So re-open your Termux To use X-osint\e[0m\n"
printf "\e[1;91m[*]\e[1;97m After reopen your termux just type '\e[1;91mxosint\e[1;97m' to launch X-osint \e[0m"
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
echo -e "\033[1;91m[*]\033[1;97m Installing Tor and Tkinter\033[0m"
sudo apt-get install -y tor python3-tk python3-numpy libxslt1-dev
echo
echo -e "\033[1;91m[*]\033[1;97m Installing Lolcat\033[0m"
echo
pip install lolcat --break-system-packages
echo
echo -e "\033[1;91m[*]\033[1;97m Installing pip dependencies from requirements.txt\033[0m"
echo
pip install --upgrade pip --break-system-packages
pip install -r requirements.txt --break-system-packages
echo
echo -e "\033[1;91m[*]\033[1;97m Downloading spaCy language model\033[0m"
python3 -m spacy download en_core_web_sm --break-system-packages
echo
echo -e "\033[1;91m[*]\033[1;97m Installing Cinemagoer\033[0m"
pip install cinemagoer --break-system-packages
echo
echo -e "\033[1;91m[*]\033[1;97m Installing vininfo\033[0m"
pip install vininfo --break-system-packages
echo
echo -e "\033[1;91m[*]\033[1;97m Installing find-github-email\033[0m"
pip install find-github-email --break-system-packages
echo
printf "\e[1;94mSetting up environment for Linux .. \e[0m\n"
sleep 1
echo
if [ -f xosint ] && [ -f setup.sh ]; then
sudo cp -r xosint /usr/local/bin && \
sudo cp -r subdomains.txt /usr/local/bin && \
sudo cp -r templates /usr/local/bin && \
sudo cp -r static /usr/local/bin && \
sudo chmod +x /usr/local/bin/xosint && \
sudo chmod +x /usr/local/bin/subdomains.txt && \
sudo chmod +x /usr/local/bin/templates && \
sudo chmod +x /usr/local/bin/static
if [ $? -eq 0 ]; then
REPO_DIR=$(pwd)
cd ..
sudo rm -rf "$REPO_DIR"
fi
fi
printf "\e[1;91m[*]\e[1;97m X-osint Installed Successfully, Now its ready for use. So re-open your Linux Terminal To use X-osint\e[0m\n"
echo
echo
printf "\e[1;91m[*]\e[1;97m After reopen your terminal just type '\e[1;91mxosint\e[1;97m' to launch X-osint \e[0m"
echo ""
exit
else
printf "\e[0m\e[1;91m [\e[1;97m~\e[1;91m]\e[1;93m Sorry, lol thats not in the option 😂....open up your eyes..!!. \e[0m\e[1;91m[\e[0m\e[1;97m~\e[0m\e[1;91m]\e[0m\n"
sleep 1
clear || cls
bash setup.sh
fi
