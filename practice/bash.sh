#! /usr/bin/zsh


echo "================================"
echo "   PETER'S STUDY DASHBOARD"
echo "================================"
echo "Date: $(date '+%A, %d %B %Y')"
echo "Time: $(date '+%H:%M')"
echo "--------------------------------"
echo "RAM Free: $(free -h | awk '/^Mem:/ {print $4}')"
echo "Battery: $(cat /sys/class/power_supply/BAT0/capacity)%"
echo "--------------------------------"
echo "Let's get it. 🔥"
echo "================================"
sleep 2
timer=$((300/60))
echo "Which session of the day?.(1/2)"
read session
if [[ "$session" == "1" ]]; then
	echo "First sssion documents - Lab/Practice"
	echo "session time is: $timer mins"
	for (( i=timer; i>0; i-- )); do
        	echo "$i mins remaining"
        	sleep 60
	done
elif [[ "$session" == "2" ]]; then
	echo "Second session  documents - Input"
fi
 
