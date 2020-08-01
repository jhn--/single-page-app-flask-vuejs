#!/bin/bash

# write test case ffs

# test add book
curl -X POST http://localhost:5000/books -d \
  '{"title": "1Q84", "author": "Haruki Murakami", "read": "true"}' \
  -H 'Content-Type: application/json'

# get first book's id
b=`curl http://127.0.0.1:5000/books | awk -F '"id":"' '{print $2}' | awk -F '","' '{print $1}'`
# test delete book
curl -X DELETE http://localhost:5000/books/$b
