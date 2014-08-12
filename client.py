import requests
from Adafruit_BMP085 import BMP085
import json

#initialise sensor
bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode

temp = bmp.readTemperature()
pressure = bmp.readPressure()

payload = {'temperature': temp, 'pressure': pressure}

server_url = 'http://zephos.duckdns.org:5000/temperature_pressure'
r = requests.post(server_url, data=json.dumps(payload))
print(r.status_code)