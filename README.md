# jsFinder
``` 
 git clone https://github.com/pwnesec/jsFinder.git
 cd jsFinder
```
# Usage
```
usage: jsFinder.py [-h] [--url URL] [--verbose] [--json] [-o OUTPUT] [--status-code]

options:
  -h, --help            show this help message and exit
  --url URL             the URL of the website to crawl
  --verbose             display URLs as they are found
  --json                output results in JSON format
  -o OUTPUT, --output OUTPUT
                        save output to a file
  --status-code         display status codes of the JavaScript files
```
# Example
```
json format  : python3 jsFinder.py --url https://facebook.com --json
status code  : python3 jsFinder.py --url https://facebook.com --status-code
verbose mode : python3 jsFinder.py --url https://facebook.com --verbos
```
