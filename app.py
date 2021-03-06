import bottle
import bottle.ext.sqlite
import json
import time

app = application = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='sensor_data.db')
app.install(plugin)

@app.route('/temperature_pressure', method='POST')
def temperature_data(db):
    data = bottle.request.json
    epoch_time = time.time()
    
    c = db.cursor()
    
    temp = data["temperature"]
    c.execute("INSERT INTO temperature VALUES (?,?)", (epoch_time, temp,))

    pressure = data["pressure"]
    c.execute("INSERT INTO pressure VALUES (?,?)", (epoch_time, pressure,))

    db.commit()

@app.route('/temperature.json', method='GET')
def temperature_data(db):
    try:
        limit = int(bottle.request.query.get('limit', 96))
    except ValueError:
        limit = 96

    data = []
    for row in db.execute('SELECT * from temperature ORDER BY date DESC LIMIT ?', (limit,)): #at 15 minutes between sample, the past 24 hours is 24*4 = 96 points
        item = {"timestamp":row[0], "temperature":row[1]}
        data.append(item)
    return json.dumps(data)

@app.route('/temperature', method='GET')
def temperature_data(db):
    #return bottle.template('<html><body>Hello World!</body></html>')
    row = db.execute('SELECT * from temperature ORDER BY date DESC LIMIT 96').fetchone()
    if row:
        temp = row[1]
        return bottle.template('<html><body> Latest temperature is: {{temp}} </body></html>', temp=temp)
    return bottle.HTTPError(404, "Page not found")

@app.route('/pressure', method='GET')
def temperature_data(db):
    #return bottle.template('<html><body>Hello World!</body></html>')
    row = db.execute('SELECT * from pressure ORDER BY date DESC LIMIT 1').fetchone()
    if row:
        pressure = row[1]
        return bottle.template('<html><body> Latest pressure is: {{pressure}} </body></html>', pressure=pressure)
    return bottle.HTTPError(404, "Page not found")

#debug stuff
if __name__ == '__main__':
    bottle.run(app=application, host='0.0.0.0', port=5000)
