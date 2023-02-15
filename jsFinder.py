import argparse
import json
import requests
import re
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='the URL of the website to crawl')
parser.add_argument('--verbose', help='display URLs as they are found', action='store_true')
parser.add_argument('--json', help='output results in JSON format', action='store_true')
parser.add_argument('-o', '--output', help='save output to a file')
parser.add_argument('--status-code', help='display status codes of the JavaScript files', action='store_true')
args = parser.parse_args()

if not args.url:
    parser.print_help()
else:
    response = requests.get(args.url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    script_tags = soup.find_all('script')

    javascript_urls = {}

    for script_tag in script_tags:
        src = script_tag.get('src')
        if src:
            if re.match(r'^https?:', src) and re.search(r'\.js(?:\?[^\/]*)?$', src):
                response = requests.get(src)
                status_code = response.status_code
                javascript_urls[src] = status_code
                if args.verbose:
                    print(src)

    if args.json:
        json_str = json.dumps(javascript_urls, indent=4)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(json_str)
        else:
            print(json_str)
    else:
        if args.status_code:
            for url, status_code in javascript_urls.items():
                print(url, status_code)
        else:
            for url in javascript_urls.keys():
                print(url)
