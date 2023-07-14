#!/bin/bash

read -r -p "Run Project [R] or Certbot operations [C]" choice

if [[ ${choice} == [rR] ]]; then
	echo "building with compose"
	sudo docker compose up -d --build
elif [[ ${choice} == [cC] ]]; then
	read -r -p "New Cert [N] or Renew [R]" operation

	if [[ ${operation} == [nN] ]]; then
		echo "adding new cert"
		read -r -p "enter domain name: " domain
		sudo docker compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d "${domain}"
	elif [[ ${operation} == [rR] ]]; then
		echo 'Renewing certs'
		sudo docker compose run --rm certbot renew

	fi
fi
