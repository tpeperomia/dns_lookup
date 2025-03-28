#!/usr/local/bin/python3
import requests 
import json

# request what domain to check save in variable
print("What domain are we looking up? ")
domain = input()

# look up the DNS records for the domain
look_up = requests.get(f"https://networkcalc.com/api/dns/lookup/{domain}").json()

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

ip = [record["address"] for record in look_up["records"].get("A")]
print(f"The IP for {domain} is {ip}")

# function to look up IP organisation 
to_check = ip[0]
org_look_up = requests.get(f"https://ipinfo.io/{to_check}/json").json()
org = org_look_up.get("org")

print(f"This IP is registered to {org}")

# check when it was registered and return date 
whois_look_up = requests.get(f"https://networkcalc.com/api/dns/whois/{domain}").json()

# to make sure the whois contains usable data
status2 = whois_look_up.get("status")
if status2 == "OK":
    full_created_date = whois_look_up.get("whois", {}).get("registry_created_date", None)
    if full_created_date:
        created_date = full_created_date.split('T')[0]
        print(f"This record was created on {created_date}")
    else:
        print(f"There are no date created records for {domain}")
else: 
    print(f"There are no date created records for {domain}")