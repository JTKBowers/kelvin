import bottle
import json

app = application = bottle.Bottle()

@app.route('/temperature_pressure', method='POST')
def index():
    data = json.loads(request.body)
    temp = data["temperature"]
    for l in bottle.request.body:
        print (l)
    print (bottle.request.body.readlines())

@app.route('/lol')
def index():
    #return bottle.template('<html><body>Hello World!</body></html>')
    return '<html><body>Hello World2!</body></html>'

#debug stuff
if __name__ == '__main__':
    bottle.run(app=application, host='0.0.0.0', port=5000)
