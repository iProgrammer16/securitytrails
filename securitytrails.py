import requests
import json


# Twitter: @iProgrammer16
print("\n\n\tTwitter: @iProgrammer16\n\n \t iProgrammer16 v1.0\n\n")



domain = input("Please enter your domain name: ")
apiKey = input("Please enter your api key: ")
print("\n")

while True:
    if not domain:
        domain = input("Please enter your domain name: ")
    elif not apiKey:
        apiKey = input("Please enter your api key: ")
    else:
        break


url = "https://api.securitytrails.com/v1/domain/" + domain + "/subdomains?children_only=false&include_inactive=true"
headers = {
    "accept": "application/json",
    "APIKEY": apiKey
}

response = requests.get(url, headers=headers)

data = response.json()

count = 0
for subdomains in data['subdomains']:
    print(subdomains + "." + domain)
    with open('_' + domain, 'a') as f:
        f.writelines(subdomains + "." + domain + "\n")
        f.close()
    count +=1

print("\nsubdomains count: " + str(count))