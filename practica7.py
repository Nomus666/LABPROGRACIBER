#!/bin/bash
	
privip=$(ip route get 1.2.3.4 | awk '{print $7}')
publicip=$(curl ifconfig.me | grep ".")
IFS='.' read -ra mask <<< "$privip"

scanner(){
	echo "Scanning Mask: "$1
	out=$(nmap -Pn -p 1,100 $1)
	printf "Scanner Output \n $out"
}


echo 'Ip Privada: '$privip
echo 'Ip Publica: '$publicip

scanner ${mask[0]}"."${mask[1]}"."${mask[2]}".0/24"
