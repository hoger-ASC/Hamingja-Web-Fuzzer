# Add FUZZ on the position where you wish to fuzz 
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
while True:
  line = input("\nPaste http headers with FUZZ as fuzzing position (type /w to confirm): ")
  lines.append(line)
  raw = "\n".join(lines)
  headers = parse_headers(raw)
  if line == "/w":
    break

# Processing ->
wl = input("\nEnter wordlist name with its extension: ")
with open(wl, "r") as data:
    wordlist = data.read()

def replace_n_check(headers, wordlist):
    for value in wordlist.splitlines():
        fuzzed = {k: v.replace ("FUZZ", value) for k, v in headers.items()}
        response = requests.get(url, headers=fuzzed)
        if response.status_code != 403 or 404:  # <-- Filter as needed
            print(f"\n{value} returned: {response.status_code}")

replace_n_check(headers, wordlist)

