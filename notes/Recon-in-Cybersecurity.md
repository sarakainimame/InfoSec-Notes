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


## Attacking

+ Directory brute forcing

