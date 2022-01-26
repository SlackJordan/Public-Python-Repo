from datetime import datetime
import requests
import json
import smtplib
from pprint import pprint


def send_email(message, to_email):
    auth = ('sendinyasomeupdatescuh@gmail.com', 'trying this again')

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # Send email
    server.sendmail(auth[0], to_email, message)


now = datetime.now()
nn = now.strftime("%m/%d/%Y %H:%M:%S")

apiKey = "867830822e581bed5c067307554204bf"
userAgent = 'VulDB API Advanced Python Demo Agent'
headers = {'User-Agent': userAgent, 'X-VulDB-ApiKey': apiKey}
url = 'https://vuldb.com/?api'
postData = {'recent': 25}
response = requests.post(url, headers=headers, data=postData)
if response.status_code == 200:

    # Parse HTTP body as JSON
    responseJson = json.loads(response.content)
    print(pprint(responseJson['result']))
    # Output

    top_twenty_five = ""

    for i in responseJson['result']:
        #print(
        #    f"Entry Data: {i['entry']['title']}\nRisk Level: {i['vulnerability']['risk']['name']}\nCVE ID: {i['source']['cve']['id']}\n-------------------------------------------\n")
       try:
            top_twenty_five += f"Title: {i['entry']['title']}\nRisk Level: {i['vulnerability']['risk']['name']}\nCVE ID: {i['source']['cve']['id']}\n\n----------------------------------------------------------------------------------------------------------\n\n"
       except KeyError:
           top_twenty_five += f"Title: {i['entry']['title']}\nRisk Level: {i['vulnerability']['risk']['name']}\nCVE ID: N/A\n\n----------------------------------------------------------------------------------------------------------\n\n"

    # print(i["entry"]["id"])
    # print(i["entry"]["title"])

message = f"Date and time is: {nn}\n\n\n Here is the 25 most recent exploits:\n\n\n" + top_twenty_five
emails = ["slack.jordan@outlook.com", "jordan-cve@23p.com"]

for email in emails:
    send_email(message, email)
