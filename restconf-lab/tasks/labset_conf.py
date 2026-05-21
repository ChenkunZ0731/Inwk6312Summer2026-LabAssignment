import logging
import requests
import yaml
from requests.auth import HTTPBasicAuth
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
)

USER = 'student'
PASS = 'Meilab123'

routers = yaml.load(
    open('lab5yml.yml'),
    Loader=yaml.SafeLoader
)

def set_interfaces(append_url):

    for hostname, value in routers.items():

        mgmt_ip = value[0]["mgmt_ip"][0]["ip"]

        for interface in value[1]["interfaces"]:

            BASE_URL = 'http://{0}/restconf/api/running/'.format(mgmt_ip)

            url = BASE_URL + append_url + interface["name"]

            auth = HTTPBasicAuth(USER, PASS)

            headers = {
                'Accept': 'application/vnd.yang.data+json',
                'Content-Type': 'application/vnd.yang.data+json'
            }

            data = {
                "ietf-interfaces:interface": {
                    "name": interface["name"],
                    "description": "Changed through Restconf",
                    "type": "iana-if-type:ethernetCsmacd",
                    "enabled": True,
                    "ietf-ip:ipv4": {
                        "address": [
                            {
                                "ip": interface["ip"],
                                "netmask": interface["mask"]
                            }
                        ]
                    },
                    "ietf-ip:ipv6": {}
                }
            }

            logging.info(f"Sending PUT to {url}")

            response = requests.put(
                url,
                auth=auth,
                headers=headers,
                data=json.dumps(data)
            )

            print(response.status_code)
            print(response.text)

            if response.status_code in [200, 201, 204]:

                logging.info(
                    f"Request successful on {hostname}, Code: {response.status_code}"
                )

            else:

                logging.error(
                    f"Error on {hostname}, Code: {response.status_code}"
                )

                print(response.text)

    return "All interfaces processed"

print(set_interfaces("interfaces/interface/"))