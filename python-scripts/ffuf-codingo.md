# FFUF

## Resources

- Insider PhD - https://www.youtube.com/watch?v=aN3Nayvd7FU&t=0s

- Codingo - https://www.youtube.com/watch?v=iLFkxAmwXF0


## Installation

$ sudo apt install ffuf

	or

$ sudo apt install golang

$ go get github.com/ffuf/ffuf

$ go get -u github.com/ffuf/ffuf


## Scanning

- build a wordlist for directory transversal

$ ffuf -u <target URL/FUZZ/> -w ./wordlist --> it will replace the words from the wordlist with the 'FUZZ' keyword

$ curl <target URL/admin> --> to see the asset


## Basic wordlist

- Tomnonom - https://www.youtube.com/watch?v=W4_QCSIujQ4&t=0s

- Seclist - https://github.com/danielmiessler/SecLists


## Recursion

$ ffuf -u <target URL/FUZZ> -w ./wordlist -recursion --> will perform recursion on found parent directories

$ ffuf -u <target URL/FUZZ> -w ./wordlist -recursion-depth [n] --> default is 30, but we can use lower or higher numbers


## Extention checks

$ ffuf -u <target URL/FUZZ> -w ./wordlist -recursion -e .bak --> queueing the wordlist to find .bak files


## Custom fuzzing words

$ ffuf -u <target URL/W1> -w ./wordlist:W1 -e .bak --> recursion is not possible at this stage, but it might be useful for busting a specific directory


## Silent mode and Tee for output

$ ffuf -u <target URL/FUZZ> -w ./wordlist -s --> it will print out only the results and not the whole buffer

$ ffuf -u <target URL/FUZZ> -w ./wordlist -s | tee ./output.txt --> will stream the results to an output file


## Working with HTML output

$ ffuf -u <target URL/FUZZ> -w ./wordlist -of html -o ./output --> formats include json, ejson, html, md, csv, ecsv; it will output into an html file with the results


## Filters and matches