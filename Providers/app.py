#!flask/bin/python
import os
from flask import Flask, jsonify
from flask import render_template
from flask import request
from flask_mysqldb import MySQL
# from config import Config
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# connections
project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './templates')
app = Flask(__name__, template_folder=template_path)

app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'provider'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'billdb'

mysql = MySQL(app)

#db = MySQL.connect("localhost", "root", "qwerty", "information_schema")


# =================================================================


# Routing:

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/provider/reg', methods=['POST'])
def get_tasks():
    providerName = request.form.get("p_name")
    query = "INSERT INTO Provider (name) VALUES ('{}')".format(providerName)
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    res = cur.fetchall()
    cur.close()
    return jsonify(res)
    # INSERT INTO table_name
    #VALUES (value1, value2, value3, ...);


@app.route('/provider/add', methods=['GET'])
def load_form():
    return render_template('index.html')


# @app.route('/api/healthy', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})


@app.route('/provider/{id}', methods=['PUT'])
def update_provider():
    return "return render_template('index.html')"


@app.route('/rates', methods=['POST'])
def upload_rates():
    return "return render_template('index.html')"


@app.route('/rates', methods=['GET'])
def get_rates():
    return "return render_template('index.html')"


@app.route('/truck', methods=['POST'])
def add_truck():
    return "return render_template('index.html')"


@app.route('/truck/{id}', methods=['PUT'])
def update_truck():
    return "return render_template('index.html')"


@app.route('/truck/<id>?from=t1&to=t2', methods=['GET'])
def get_truck():
    return "return render_template('index.html')"


@app.route('/bill/<id>?from=t1&to=t2', methods=['GET'])
def get_bill():
    return "return render_template('index.html')"


@app.route('/health', methods=['GET'])
def get_health():
    query = "SELECT * FROM billdb;"
    try:
        cur = mysql.connection.cursor()
    except:
        return "MYSQL_IS_DOWN"
    else:
        # test that the DB is alive by selecting data:
        query = "SELECT * from Provider;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        mysql.connection.commit()
        res = cur.fetchall()
        cur.close()
    return jsonify(res)


# @app.route('/api/healthy', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})


app.run(host='0.0.0.0', port=5000)
if __name__ == '__main__':
    app.run(debug=True)
