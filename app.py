import bottle
import json

app = application = bottle.Bottle()

_temp = 0
@app.route('/temperature_pressure', method='POST')
def temperature_data():
    data = json.loads(bottle.request.body)
    _temp = data["temperature"]
    for l in bottle.request.body:
        print (l)
    print (bottle.request.body.readlines())

@app.route('/temperature_pressure', method='POST')
def temperature_data():
    #return bottle.template('<html><body>Hello World!</body></html>')
    return template('<html><body> Latest temperature is: {{temp}} </body></html>', temp=_temp)

#debug stuff
if __name__ == '__main__':
    bottle.run(app=application, host='0.0.0.0', port=5000)
