# Hamingja-Web-Fuzzer
## (WIP, to add threading functionality)
Python HTTP bruteforce request fuzzer based on requests library

## Requirements & Usage

Requirements: python 3.14+, requests library

(Concept) This python web fuzzer works simmilarly to portswigger's burpsuite intruder or OWASP's zaproxy fuzzer.
The user marks a fuzzing point inside headers which is tested against a wordlist (must be in same directory as the script, prefferably .txt extension) through CLI;
The script continues to check each wordlist value and returns response based on filtered status codes.

## License, Ethics & Acknowledgements

[MIT license](https://en.wikipedia.org/wiki/MIT_License)

*Consult laws and user agreements before usage.*

Acknowledgments to w3schools.com and [the official requests documentation](https://docs.python-requests.org/en/master/index.html) for syntax along with qwen 3.5/Claude4 for testing the parsing and enumeration def functions
