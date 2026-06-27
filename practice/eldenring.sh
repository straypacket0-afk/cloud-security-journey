#!/usr/bin/zsh

echo "do you like coffee?,(y/n)"

read coffee 

if [[ $coffee == "y" ]]; then
	echo "great"
else
	echo "leave"
fi
