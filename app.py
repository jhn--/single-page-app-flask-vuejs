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
        # 'read': "true"
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potther and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        # 'read': "false"
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        # 'read': "true"
        'read': True
    }
]

KEYS = {'title':'', 'author':'', 'read':''}

TF = {"true": True, "false": False}

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    '''
    TODO:
        What if the title already exists? (done)
        Or what if a title has more than one author? (do i create a ... list? but how will i create my ui??)
        Check your understanding by handling these cases. 
        Also, how would you handle an invalid payload where the title, 
        author, and/or read is missing? (done)
    '''
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        response_object = check_fields(post_data) # check fields, overwrites value of original response_object
        if response_object['status'] == 'fail':
            return jsonify(response_object)
        else:
            BOOKS.append({
                'id': uuid.uuid4().hex,
                'title': post_data.get('title'),
                'author': post_data.get('author'),
                'read': post_data.get('read')
            })
            response_object['message'] = 'Book added!' # append ['message'] to response_object
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
    Take a moment to think about how you would handle the case of an id not existing. (done)
    What if the payload is not correct?  (idk what this means.)
    Refactor the for loop in the helper as well so that it's more Pythonic. (idk if this is more pythonic)
    '''
    try:
        BOOKS.remove([book for book in BOOKS if book['id'] == book_id][0])
    except Exception as e:
        return False # if the book doesn't exist, [0] will not exist and will raise a "IndexError: list index out of range" error. Simplify everything down to a False.
    else:
        return True

def check_fields(post_data):
    '''
    Check fields and submitted.
    '''
    response_object = {'status': 'fail'}

    # check if all fields exists
    if post_data.keys() != KEYS.keys(): 
        response_object['message'] = 'Missing fields.'
        return response_object
    # check if fields are empty or incorrect
    elif len(post_data.get('title')) == 0 or len(post_data.get('author')) == 0: # or post_data.get('read') not in (TF.keys() or TF.values()):
        response_object['message'] = 'Incorrect values.'
        return response_object
    # check if book title already exists in list
    elif len([book for book in BOOKS if book['title'] == post_data.get('title')]) != 0:
        response_object['message'] = 'Book already in list.'
    else:
        response_object['status'] = 'success'
    return response_object

if __name__ == '__main__':
    app.run()