## Domain Recon
---
1. crt.sh
    
    - retrieve organization website SSL certificate from browser `https://www.ssl2buy.com/wiki/how-to-view-ssl-certificate-details-on-chrome-56`   

        - in alternative, SSL certificates can be checked in `https://www.sslshopper.com/`

    - paste organization `Trade Name` in `crt.sh` (ex: Under Armour, Inc.)

2. Shodan recon

    - create an account or, multiple accounts in order to retrieve more access (free account has access to only 2 pages)
    - retrieve `Trade Name`
    - dork `ssl.'Trade-Name-with-no-punctuation' 200` in order to retrieve live websites with that specific SSL
    - filter results with `http.title`
    - open 10-15 (or all) pages and analyze - the main targets are `Login` pages
    - retrieve webpages's IP addresses

        - other dorks to use: (*apply same filters*)
        ```
        - net:<CIDR,CIDR,CIDR>
        - ssl:"Program Name"
        - ssl.cert.subject.CN:"domain.com" 200
        - http.title:"Grafana" 200 (for Grafana 0day vulnerability)
            - filter for '.org' and search for the particular domain
        - http.title:"Citrix Gateway" 200 (same procedure as for Grafana)
        ```
    *other recon platforms:*
    ```
    - whoxy.com
    - securitytrails.com
    ```
    - once we have all the `Login` pages, we can start scanning with BurpSuite and try testing for weak passwords    

3. Gihub recon

    - retrieve `Trade Name` and query Github (`password, pwd, pw, admin, api, token, secret, private`)
    - retrieve the `domain` and query Github
    - check for code pushes
    - static code review
    - check for Users that pushed the code, and query (even in Google)
    - filter queryes by adding `NOT this.com`, `language:python`
    - apply same tactic on `gist.github.com`
 



## Static Code Analysis
---
1. Browser dev tools
    
    - F12 on webpage, and look for `.js` files - open and search for sensitive data (api, password, domain, access tokens, etc.)


