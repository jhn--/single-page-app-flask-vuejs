# https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/

from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid


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
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potther and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    '''
    TODO:
        What if the title already exists? (done)
        Or what if a title has more than one author? 
        Check your understanding by handling these cases. 
        Also, how would you handle an invalid payload where the title, 
        author, and/or read is missing?
    '''
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        if len([book for book in BOOKS if book['title'] == post_data.get('title')]) == 0:
            # if there's no such book title in the list
            BOOKS.append({
                'id': uuid.uuid4().hex,
                'title': post_data.get('title'),
                'author': post_data.get('author'),
                'read': post_data.get('read')
            })
            response_object['message'] = 'Book added!' # append ['message'] to response_object
        else:
            response_object['status'] = 'fail'
            response_object['message'] = 'Book already in list.'
    else:
        response_object['books'] = BOOKS # append ['books'] to response_object
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated.'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed.'
    return jsonify(response_object)

def remove_book(book_id):
    '''
    Take a moment to think about how you would handle the case of an id not existing. 
    What if the payload is not correct? 
    Refactor the for loop in the helper as well so that it's more Pythonic.
    '''
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

if __name__ == '__main__':
    app.run()