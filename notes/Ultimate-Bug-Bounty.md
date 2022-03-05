## Advanced Recon
---
### Tomnomnom automated recon 
----
(https://www.youtube.com/watch?v=SYExiynPEKM&t)

1. Make a target directory 

2. fetch in scope `widcards` file (no need for www.)

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