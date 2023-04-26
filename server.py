from flask import Flask, g, request, jsonify
import sqlite3
import subprocess
import datetime

# Run the script using subprocess
subprocess.call(["python3", "startdb.py"])


app = Flask(__name__)

#python3 startdb.py

DATABASE = 'location.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
@app.route('/')
def index():
    db = get_db()
    cur = db.execute('SELECT * FROM Position')
    rows = cur.fetchall()
    return str(rows)
    
@app.route('/add_data', methods=['POST'])
def add_data():
    whole = request.get_json()
    uuid = whole['UUID']
    lat = whole['Lat']
    log = whole['Lon']
    alt = whole['Alt']
    db = get_db()
    db.execute('INSERT INTO Position (UUID, Lat, Lon, Alt, Time) VALUES (?, ?, ?, ?, ?)', (uuid, lat, log, alt, datetime.datetime.now()))
    db.commit()
    return 'Data added to database'
    
@app.route('/get_data', methods=['GET'])
def get_data():
    data = []
    db = get_db()
    cur = db.execute('SELECT * FROM Position')
    rows = cur.fetchall()
    for row in rows:
        data.append(dict(row))
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)

