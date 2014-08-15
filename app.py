import bottle
import bottle.ext.sqlite
import json

app = application = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='sensor_data.db')
app.install(plugin)

@app.route('/temperature_pressure', method='POST')
def temperature_data(db):
    for l in bottle.request.body:
        print (l)
    print (bottle.request.json)
    data = bottle.request.json


    temp = data["temperature"]

    c = db.cursor()
    
    c.execute("INSERT INTO temperature VALUES ('2006-01-05',?)", (temp,))

    pressure = data["pressure"]
    c.execute("INSERT INTO pressure VALUES ('2006-01-05',?)", (pressure,))

    db.commit()

@app.route('/temperature', method='GET')
def temperature_data(db):
    #return bottle.template('<html><body>Hello World!</body></html>')
    row = db.execute('SELECT * from temperature').fetchone()
    if row:
        temp = row[1]
        return bottle.template('<html><body> Latest temperature is: {{temp}} </body></html>', temp=temp)
    return bottle.HTTPError(404, "Page not found")

#debug stuff
if __name__ == '__main__':
    bottle.run(app=application, host='0.0.0.0', port=5000)
