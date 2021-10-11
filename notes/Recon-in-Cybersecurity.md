# Recon in Cybersecurity
(https://www.udemy.com/course/reconcybersec)

## Platforms

+ Platform based

	+ https://hackerone.com
	+ https://bugcrowd.com
	+ https://intigrity.com
	+ https://www.openbugbounty.org/
	+ https://www.synack.com
	+ https://cobalt.io/
	+ https://www.zerocopter.com

+ Non-platform based

	1. go to https://google.com
	2. search for:

		- inurl:"security.txt"
		- intitle:"responsible disclosure policy"


## Automated tools

+ subdomains

	- findomain
	- subbrute
	- crt.sh
	- amass
	- assetfinder

+ alive subdomains

	- httprobe
	- https://github.com/CristiVlad25/py-scripts-other

+ bruteforcing

	- 

+ file parsing

	-  


## Subdomain discovery

+ Amass (https://github.com/OWASP/Amass )

	# amass enum -d <domain> >> results.txt

	# amass --help

+ Findomain (https://github.com/Edu4rdSHL/findomain)

	# findomain -t <domain>

	# findomain --help

+ crt.sh (https://github.com/appsecco/the-art-of-subdomain-
enumeration/blob/master/crtsh_enum_web.py)

	# python3 crt_enum_web.py <domain>

	# %.docs.google.com

+ Assetfinder (https://github.com/tomnomnom/assetfinder)

	# assetfinder --subs-only <domain> >> results.txt

	# cat results.txt | wc -l

+ SUbbrute (https://github.com/TheRook/subbrute )

	# ./subbrute.py <domain>

- Appsecc: https://github.com/appsecco/the-art-of-subdomain-enumeration

- Free book: https://appsecco.com/books/subdomain-enumeration/


## Eliminating the noise

+ removing the duplicate subdomains

	# cat results.txt | sort -u > results-unique.txt

	# cat results-unique.txt | wc -l

+ probing the unique results (both http and https)

	- httprobe

	# cat results-unique.txt | httprobe -c 100 > results-alive.txt

	# cat results-alive.txt

	- upcheck.py

	# upcheck.py results-alive.txt

	- create a random subset

	# tail -n 50 results-alive.txt | sort -R > results-subset.txt

	- grep and clean only alive from upcheck

	# cat results-alive.txt | grep "'200'" | cut -d "'" -f2 > clean-results.txt


## Attacking (Directory brute forcing)

+ Dirb

	# locate common.txt 

		> find word list - better to create a custom one (build from SecList)

	# dirb <domain> common.txt

	# dirb 

		> manual

+ Dirbuster

+ Gobuster

	# gobuster -u <domain> -w common.txt -x js, txt, log, bak, php --wildcard

		> will append the indicated file extensions

	# gobuster 

		> for manual

	# gobuster --help

		> more information and try some combinations of flags

+ Dirsearch (best)

	# dirsearch.py -u <domain> -w common.txt -e js, php, txt, log, bak -b -t 200

		> -b for hostname and not IP

		> -t for threads, use less for noise

	# CTRL+C

		> pause the search, better when using a VM

+ Fuff

	# fuff -w common.txt -u <domain> /FUZZ mc 200 -c -v

		> mc 200 - matchcode 200


## Finding other bugs

+ Slurp (bucket hunting)

	# slurp domain -t <domain>

	# slurp keyword -t <word (google docs)>

		> will search for google docs

	# slurp --help

	# slurp certstream

		> check it out

+ Bucket Flaws

		> search the repo on Github

+ S3scanner

		> search the repo on Github

+ AWS Bucket dump

		> search the repo on Github

+ shodan.io

		> check out 'Complete Guide to Shodan'

		> check out Shodan-Dorks

	1. go to company website
	2. look into the source-code and copy the link of the favicon file
	3. use python script to get favicon hash (https://gist.github.com/yehgdotnet/b9dfc618108d2f05845c4d8e28c5fc6a)
	4. copy the hash
	5. go to shodan and query "http.favicon.hash: <hash>"

+ Github

- manual reconnaisance

	1. input into search bar "google "api_key"" - can use 'secret', 'csrf', 'token', 'password' (https://github.com/techgaun/github-dorks)
	2. filter with "Code"
	3. search

- automated reconnaisance

	- truffleHog https://github.com/trufflesecurity/truffleHog

	- gitrob https://github.com/michenriksen/gitrob

	- gittyleaks https://github.com/kootenpv/gittyleaks

+ ReconT https://github.com/dock3rX/ReconT

+ Webint.io 

+ Cyberscan.io

+ Pastebin.com

+ WolframAlpha.com

+ Google dorks (google hacking)
https://www.exploit-db.com/google-hacking-database


## Increasing the attack surface

+ nmap

	# nmap -sS -sU -sV -p- <domain>

+ nikto 
	
	# nikto -h <domain>

	# nikto -h <domain>:1932

		> if the website is running on a different port than 80 or 443

+ Burp (or ZAP)


## Searching for JS files

- automated

	- Linkfinder 

	# python3 linkfinder.py -i <domain.com/file.js> -o cli

		> find js files from F12

- manual (best)

	1. install 'JS beautifier'
	2. analyze and search for sensitive files via search funtion (http, https, .js, .xml, .log, api, api_key, token, apikey, secret, config, conf, cfg, env)


## Waybackmachine

+ waybackurls

	# echo <string> | waybackurls

		> will search on archive.org the specific string

	# cat domains.txt | waybackurls > results.txt

		> can do this search even by domains

	# cat results.txt | grep "\.js"

		> add more filters to the grep query





