# Domain Lookup Script &#128213;

## Description
This Python script retrieves DNS records and WHOIS registration details for a given domain. It fetches the domain's IP address (A records) and registration creation date using the `networkcalc.com` API. 

I created this script as an exercise to become more familiar with API interactions and DNS record uses. 

## Prerequisites
- Python 3.x
- `requests` library (install using `pip install requests`)

## Example output 
What domain are we looking up? 
example.com
Looking up ... ... ...
The IP for example.com is ['93.184.216.34']
This record was created on 1995-08-14

## Error Handling
If no A records exist, the script notifies the user and exits.
If an invalid domain is entered, an error message is displayed.
