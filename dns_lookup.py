#!/usr/local/bin/python3
import requests 
import json

# request what domain to check save in variable
print("What domain are we looking up? ")
domain = input()

# look up the DNS records for the domain
look_up = requests.get(f"https://networkcalc.com/api/dns/lookup/{domain}").json()
human_readable = json.dumps(look_up, indent = 4)

# failout statement
status = look_up.get("status")
if status == "OK":
    print("Looking up ... ... ...")
elif status == "NO_RECORDS":
    print("There are no A records for that domain")
    exit()
else:
    print("There was a problem with your input, try again")
    exit()

parsed_address = json.loads(human_readable)
ip = [record["address"] for record in parsed_address["records"].get("A", [])]
print(f"The IP for {domain} is {ip}")

# check when it was registered and return date 
whois_look_up = requests.get(f"https://networkcalc.com/api/dns/whois/{domain}").json()
full_created_date = whois_look_up["whois"]["registry_created_date"]
created_date = full_created_date.split('T')[0]
print(f"This record was created on {created_date}")