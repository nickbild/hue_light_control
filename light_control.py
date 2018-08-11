import sys
import os
import ConfigParser
import requests
import json


# Configuration
config = ConfigParser.ConfigParser()
config.read(os.path.abspath(os.path.dirname(sys.argv[0])) + '/params.cfg')
user = config.get('general', 'user')
hostname = config.get('general', 'hostname')


req = requests.get('http://' + hostname + '/api/' + user + '/lights')
json = req.json()
print json["1"]["name"]


