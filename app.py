import bottle

app = application = bottle.Bottle()

@app.route('/temperature_pressure', method='POST')
def index():
    for l in request.body:
        print (l)
    print (request.body.readlines())

@app.route('/')
def index():
    #return bottle.template('<html><body>Hello World!</body></html>')
    return '<html><body>Hello World2!</body></html>'

#debug stuff
if __name__ == '__main__':
    bottle.run(app=application, host='0.0.0.0', port=5000)