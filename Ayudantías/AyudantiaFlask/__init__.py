from flask import Flask, jsonify, abort, request
from pymongo import MongoClient


app = Flask(__name__)

# MONGODATABASE = "AyudantiaDB"
# MONGOSERVER = "localhost"
# MONGOPORT = 27017
# client = MongoClient(MONGOSERVER, MONGOPORT)

@app.route('/')
def hello_world():
    return jsonify({"Status": "ok"}), 200


@app.route('/sender/<int:user>', methods=['GET'])
def sender(user):
    pass


@app.route('/add_message/', methods=['POST'])
def add_message():
    pass


@app.route('/remove_message/<string:date>', methods=['DELETE'])
def remove_message(date):
    pass


if __name__ == '__main__':
    app.run(port=5000)
