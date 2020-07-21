# https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/

from flask import Flask, jsonify
from flask_cors import CORS


# cofiguration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
"""
Why do we need Flask-CORS? In order to make 
cross-origin requests -- e.g., requests that 
originate from a different protocol, IP address, 
domain name, or port -- you need to enable 
Cross Origin Resource Sharing (CORS). 
Flask-CORS handles this for us.
"""
BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potther and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })


if __name__ == '__main__':
    app.run()