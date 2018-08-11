# Philips Hue Light Control

Control Philips Hue lights programmatically.

## Usage:

### Status of lights

python light_control.py list

Returns:
ID:IS-ON?:BRIGHTNESS:DESCRIPTION

### Turn lights on or off

python light_control.py state [ID] [on|off]

### Adjust light brightness

python light_control.py brightness [ID] [0-254]

