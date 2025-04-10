#!/usr/local/bin/python3
import requests 
import json

# disable warnings on requests while networkcalc ssl is out and forcing use with verify=False. REMOVE WHEN DOABLE
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# global styling
border = "=================================================="
border2 = "--------------------------------------------------"

# request what domain to check save in variable
print(f"\nWhat domain are we looking up?\n{border2}\n")
domain = input()

# look up the DNS records for the domain
look_up = requests.get(f"http://networkcalc.com/api/dns/lookup/{domain}", verify=False).json()

# failout statement
status = look_up.get("status")
if status == "OK":
    print(f"\n{border}\nLooking up {domain}\n{border}\n")
elif status == "NO_RECORDS":
    print(f"\n{border}\n There are no A records for that domain{border}\n")
    exit()
else:
    print("There was a problem with your input, try again")
    exit()

ip = [record["address"] for record in look_up["records"].get("A")]
ip_print = " ".join(ip) # stripping the arraty from the output 
print(f"\n{border2}\nThe IP for {domain} is {ip_print}\n{border2}\n")

# function to look up IP organisation 
to_check = ip[0]
org_look_up = requests.get(f"https://ipinfo.io/{to_check}/json").json()
org = org_look_up.get("org")

print(f"\n{border2}\nThis IP is registered to {org}\n{border2}\n")

# check when it was registered and return date 
whois_look_up = requests.get(f"http://networkcalc.com/api/dns/whois/{domain}", verify=False).json()

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

