## Advanced Recon
---
### Tomnomnom automated recon 
----
(https://www.youtube.com/watch?v=SYExiynPEKM&t)

1. Make a target directory 

2. Fetch in scope `widcards` file (no need for www.)

3. `cat wildcards | assetfinder --subs-only | anew domains`
    - add to path: https://www.digitalocean.com/community/tutorials/how-to-install-go-on-ubuntu-20-04
    - download go applications: https://medium.com/@sherlock297/go-get-installing-executables-with-go-get-in-module-mode-is-deprecated-de3a30439596
4. in alternative we can use `findomain -f wildcards | tee -a from-findomain`, where `tee -a` is an alternative to anew
    - once we have `from-findomain` we can run `cat from-findomain | anew domains` so we can add other domains to scope and eliminate duplicates

5. remove special characters from `domain` file, like "_", "*"

6. `cat domains | httprobe -c 80 --prefer-https | anew hosts`

7.  `cat hosts | fff -d 1 -S -o roots`, this will output a new file will all the root file containing all the headers of the pages

8. `cd roots` and `gf <command>` for information (https://github.com/tomnomnom/gf)

9. `waybackurls '<domain>'` | tee -a waybackurls-domain
    
    - or `waybackurls --get-versions '<web-page>'`
    - search for `.js` files

- Bruteforce 404 and 403 pages

10. `ffuf -w /Seclists/Web-Content/raft-large-files.txt -u <domain>/FUZZ`

    - in alternative we can use `raft-large-directories.txt`

    - advanced ffuf fuzzing: `ffuf -u https://DOM/FUZZ -w domains.txt: DOM, wordlist.txt: FUZZ -recursion -recursion-depth 3 -s -e .asa,.inc,.config,.bak,.old,.sql,.tar.gz -o results.txt -of csv -se -ac`


### Jhaddix methodology
-----
(https://www.youtube.com/watch?v=p4JgIu1mceI&)

1. Scope domains

2. Acquisition

    - `crunchbase.com`, get target information details (founders, acquisitons, Linkedin, etc.) and possibily dill down on old domains related to the target

3. ASN enumeration

    - `bgp.he.net`, helps to acquire both IPv4 and IPv6 addresses
    
    - `echo 'target' | metabigor net --org -v`, using metabigor

    - `pyhton asnlookup.py -a <target>`


### LeetDoor methodology
----
(https://www.youtube.com/watch?v=U2VUycNCBcE&, https://github.com/blackhatethicalhacking)

1. create scope directory

2. gather subdomains passively via `recon-ng`, can use `amass`

3. `cat <subdomains> | httpx -verbose > <urls>`, checking for live subdomains

4. gather IP addresses from `amass`

5. `./isup.sh <ips>`, will probe for valid IP addresses and will dump them to a file `valid-ips.txt`

6. `nmap -iL valid-ips.txt -sSV -A -T4 -O -Pn -v -F -oX <nmap-results.xml>`

    - examen output via Hive preferrably: https://hexway.io/downloads/
    
    - examen for expired certificates

    - printers

    - other service vulnerabilities (metasploit, log4j, etc.)

7. `sniper -f <valid-ips.txt> -m massweb -w <workspace-name>`, it's an advanced `nmap` type of tool

8. `osmedeus scan -f vuln-and-dirb -t <list-of-domains.txt>`

    - or, `osmedeus scan -T <list_of_targets.txt>`

    - apply concurrency of 2, `cat <list_of_targets.txt> | osmedeus scan -c 2`

9. `cat <subdomains.txt> | while read line ; do echo "QUIT" | openssl s_client -connect $line:443 2>&1 | grep 'server extension "heartbeat" (id=15)' || echo $line: safe; done`, in order to check for `Heartbleed`

10. `getJS --url <domain.com> --output <results.txt>`, grabbing .js files from domain

    - or, `getJS --input <urls.txt> --output <results.txt>`

11. `takeover -l <sub_domains.txt> -v -t 10` to check for domain takeover

12. `nuclei -l <urls.txt> -t /root/nuclei-templates/technologies/s3-detect.yaml` to check for S3 buckets via `Nuclei`

13. `python3 paramspider.py --domain <doamin.com> --exclude woff,png,svg,php,jpg --output <params.txt>`

14. `eyewitness -f <urls.txt>` for taking screenshots of targets in order to prioritize

15. `cat <params.txt> | gf xss | sed 's/FUZZ/ /g' >> <xss_params_forMeg.txt>`, preparing for fuzzing

16. `amass enum -passive -d <domain.com> -v | httpx -verbose | nuclei -t /root/nuclei-templates/cves/ -o <output.txt>` searching for vulnerabilites via `Nuclei`

17. `amass enum -passive -d <domain.com> -v | httpx -verbose | jaeles scan -s 'cves' -s 'sensitive' -s 'fuzz' -s ‘common' -s 'routines' report -o <output.txt>` using `Jaeles` for CVE scanning


### Amass
----
(https://www.youtube.com/watch?v=ES6OKjgW36w)

- Wordlists/API keys/DNS resolvers can be added/modified from the .config file

1. `amass enum -d <domain.com> -src -ip | anew subdomains`, will find subdomains using a basic built-in wordlist, and will output to file

2. `amass intel -asn <AS number> -active`, in order to dig deeper for domains based on the ASN

3. `amass intel -whois -d <domain.com>`, even deeper recon via a reverse whois, for free (only top 50 results)

4. `amass enum -df <subdomains-file> -src -ip -brute -wm ?a?a,?d?d?d -awm ?a?a?a` for using `hashcat`  wildcards


## Active Scanning
----
### Nuclei
----
(https://www.youtube.com/watch?v=jbmFYydIWXE&)

1. Grab the file of found domains for Recon

2. Run: `nuclei -l ~/Path/to/hosts -rate-limit 4 -header 'User-Agent: BugBountyHuter' -H 'X-Bug-Bounty: YesWeHack'`


## Attack Techniques
----
### CSRF
---
- Cross Site Request Forgery - type of attack that uses input fields to forge/repeat/remove/replace a specific type of request to the web server. Normally this is accomplished via a `token` generated from the server. High value targets are `money transfers`, `login pages`, or anything that renders an input unique.
