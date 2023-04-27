from flask import Flask, g, request, jsonify
import sqlite3
import datetime

from auth import require_bearer_token

from startdb import create_db

create_db()

app = Flask(__name__)

# python3 startdb.py

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
@require_bearer_token
def index():
    db = get_db()
    cur = db.execute('SELECT * FROM Position')
    rows = cur.fetchall()
    return str(rows)


@app.route('/add_data', methods=['POST'])
@require_bearer_token
def add_data():
    field = ['UUD','FullName','LastName','CompanyName','PhoneNumber','Lat','Lon','Alt']
    data = request.get_json()
    value = [data[i] for i in fields]
    db = get_db()
    db.execute('INSERT INTO Position (UUID, FullName, LastName, CompanyName, PhoneNumber, Lat, Lon, Alt, Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, {datetime.datetime.now()})', (value))
    db.commit()
    return 'Data added to database'


@app.route('/get_data', methods=['GET'])
@require_bearer_token
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
