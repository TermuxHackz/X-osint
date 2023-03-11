#! /bin/bash 
  
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
	printf "\e[1;34m\tSelect your terminal to install X-osint \e[0m\n"
	printf "\e[1;91m\t[!] PLEASE MAKE SURE YOU CHOOSE CORRECTLY [!] \e[0m\n\n"
	printf "\e[1;34m\t\t[\e[0m\e[1;77m01\e[0m\e[1;34m]\e[0m\e[1;93mTermux\e[0m\e[1;91m [UNSTABLE]\e[0m\n"
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
pip install requests
echo
echo -e "\033[1;91m[*]\033[1;97m Setting up environment \033[0m"
echo
cp -r xosint.py $PREFIX/bin
cd $PREFIX/bin && mv xosint.py xosint
cd $PREFIX/bin && chmod u+x xosint
 printf "\e[1;91m[*]\e[1;97m X-osint Installed Successfully, Now its ready for use. So re-open your Termux To use X-osint\e[0m\n" 
 printf "\e[1;91m[*]\e[1;97m After reopen your termux just type '\e[1;91mxosint\e[1;97m' to launch X-osint \e[0m\n" 
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
echo -e "\033[1;91m[*]\033[1;97m Installing Lolcat\033[0m"
echo
sudo pip install lolcat

sleep 1
printf "\e[1;94mSetting up environment for Linux .. \e[0m\n"				
sleep 1
sudo cp -r xosint.py /usr/local/bin
cd /usr/local/bin && sudo mv xosint.py xosint
cd /usr/local/bin && sudo chmod u+x xosint
cd $HOME && sudo rm -rf X-osint
 printf "\e[1;91m[*]\e[1;97m X-osint Installed Successfully, Now its ready for use. So re-open your Linux Terminal To use X-osint\e[0m\n" 
 printf "\e[1;91m[*]\e[1;97m After reopen your terminal just type '\e[1;91msudo xosint\e[1;97m' to launch X-osint \e[0m" 
 echo ""
 exit
else 
printf "\e[0m\e[1;91m [\e[1;97m~\e[1;91m]\e[1;93m Sorry, lol thats not in the option 😂....open up your eyes..!!. \e[0m\e[1;91m[\e[0m\e[1;97m~\e[0m\e[1;91m]\e[0m\n"
sleep 1
clear || cls
bash setup.sh
fi
