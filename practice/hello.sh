#!/usr/bin/zsh


date=$(date)
location=$(pwd)
name=$(whoami)
docu=$(cat prompt.txt)
courses="Linux, Networking, Python, Cloud"

echo "Welcome, $name "
sleep 1
echo "You're currently in $location" 
echo "Time & Date : $date"
sleep 1

echo "\nSession 01, Input Session."
sleep 2
echo "On schedule: $courses"
echo "Where would you want to start?"
read choice
if [[ $choice == "python" ]]; then
	echo "$choice is a good choice!"
elif [[ $choice == "networking" ]]; then
	echo "$choice is a good choice!"
elif [[ $choice == "linux" ]]; then
        echo "$choice is a good choice!"
	echo "$linux"
elif [[ $choice == "cloud" ]]; then
        echo "$choice is a good choice!"
else
	echo "$choice Not in schedule"
fi
