import requests
from Adafruit_BMP085 import BMP085
import json

#initialise sensor
print ('Initialising sensor...')
bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode

print ('Reading sensor...')
temp = bmp.readTemperature()
pressure = bmp.readPressure()

payload = {'temperature': temp, 'pressure': pressure}

print ('POSTing data...')
server_url = 'http://zephos.duckdns.org:5000/temperature_pressure'
headers = {'content-type': 'application/json'}
r = requests.post(server_url, data=json.dumps(payload), headers=headers)
print(r.status_code)
