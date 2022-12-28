import requests
import json
from argparse import ArgumentParser
from prettytable import PrettyTable

# asks for user api key
parser = ArgumentParser()
parser.add_argument('-k', '--apikey', required=True, help='Meraki API Key')
api_key = parser.parse_args().apikey

# set headers
headers = {'X-Cisco-Meraki-API-Key': api_key, 
            'Accept': 'application/json', 
            'Content-Type': 'application/json'}

# base url
base_url = "https://api.meraki.com/api/v1"

# get organizations
url = base_url + "/organizations"
response = requests.get(url=url, headers=headers)

# organizations table
org_table = PrettyTable(['OrganizationId', 'OrganizationName'])
for org in response.json():
    org_table.add_row([org['id'], org['name']])
print(org_table)

# asks for organizationId
organizationid = input('\n--> Informe a OrganizationId desejada: ')

# get organization networks
url = base_url + f"/organizations/{organizationid}/networks"
response = requests.get(url=url, headers=headers)

# networks table
networks_table = PrettyTable(['NetworkId', 'NetworkName'])
for net in response.json():
    networks_table.add_row([net['id'], net['name']])
print(networks_table)

# asks for NetworkId
networkid = input('\n--> Informe a NetworkId desejada: ')
for net in response.json():
    if networkid in net['id']:
        networkname = net['name']

# get network devices
url = base_url + f"/networks/{networkid}/devices"
response = requests.get(url=url, headers=headers)

# devices table
devices_table = PrettyTable(['NetworkId', 'NetworkName', 'Modelo', 'SerialNumber', 'Firmware'])
for device in response.json():
    devices_table.add_row([networkid, networkname, device['model'], device['serial'], device['firmware']])
print(devices_table)
