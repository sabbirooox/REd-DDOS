#!/bin/bash
clear
echo -e "\e[1;32m[+] Installing Requirements...\e[0m"
pkg update -y && pkg upgrade -y
pkg install python -y
pip install colorama

echo -e "\e[1;32m[+] Downloading RED DDOS Tool...\e[0m"
curl -sL https://raw.githubusercontent.com/sabbiroox/Red-DDOS/main/tool.py -o tool.py

chmod +x tool.py

echo -e "\e[1;34m[✓] Installation Complete!\e[0m"
echo -e "\e[1;33mType 'python tool.py' to run the tool.\e[0m"
