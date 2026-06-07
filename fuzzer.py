# Add ¬ on the position where you wish to fuzz 
# (script treats it by replacing it with each word in wordlist)

import requests
import os

url = input("Paste URL: ").strip()

# Parsing ->
def parse_headers(raw_headers: str) -> dict: #parser
    headers = {}
    for line in raw_headers.strip().splitlines():
        if line.startswith(("GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS")): #skip HTTP request section
            continue
        if not line.strip():
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            headers[key.strip()] = value.strip()
    return headers

lines = []
if True:
  line = input("Paste http headers with ¬ as fuzzing position: "\n)
  lines.append(line)
  raw = "\n".join(lines)
  headers = parse_headers(raw)

# Processing ->
wl = input("Enter wordlist name with its extension: ")
with open(wl, "r") as data:
    wordlist = data.read()

def replace_n_check(headers, wordlist):
    for value in wordlist:
        headers["¬"] = value
        response = requests.get(url, headers=headers)
        if respone.status_code != 403 or 404:  # <-- Filter as needed
            print(f"\n{value} returned: {response}")

