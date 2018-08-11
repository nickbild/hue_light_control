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


def RepresentsInt(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False


if len(sys.argv) < 2:
	print "Usage:\npython " + sys.argv[0] + " list"
	print "Returns:\nID:IS-ON?:BRIGHTNESS:DESCRIPTION"
	print "\npython " + sys.argv[0] + " state [ID] [on|off]"
	print "\npython " + sys.argv[0] + " brightness [ID] [0-254]\n"
	sys.exit(0)

if sys.argv[1] == "list":
	req = requests.get('http://' + hostname + '/api/' + user + '/lights')
	json = req.json()
	for id in json:
		print str(id) + ":" + str(json[id]["state"]["on"]) + ":" + str(json[id]["state"]["bri"]) + ":" + json[id]["name"]

elif sys.argv[1] == "state":
	light_id = sys.argv[2]
	state = sys.argv[3]

	if not RepresentsInt(light_id):
		print "Invalid light ID!"
		sys.exit(0)

	if state == "on":
		json = json.dumps({'on': True})
	elif state == "off":
		json = json.dumps({'on': False})
	else:
		print "Invalid state!"
		sys.exit(0)

	req = requests.put('http://' + hostname + '/api/' + user + '/lights/' + light_id + '/state', data=json)
	print req.text

elif sys.argv[1] == "brightness":
	light_id = sys.argv[2]
	brightness = sys.argv[3]

	if not RepresentsInt(light_id):
		print "Invalid light ID!"
		sys.exit(0)

	if not RepresentsInt(brightness):
		print "Invalid brightness level!"
		sys.exit(0)

	brightness = int(brightness)
	if brightness < 0 or brightness > 254:
		print "Brightness must be between 0 and 254!"
		sys.exit(0)

	json = json.dumps({'bri': brightness})

	req = requests.put('http://' + hostname + '/api/' + user + '/lights/' + light_id + '/state', data=json)
	print req.text

