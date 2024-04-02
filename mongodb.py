# pip install pymongo
import pymongo
from pymongo import MongoClient
from datetime import datetime

# make a connection
client = MongoClient('mongodb://localhost:27017/dockerdemo')

# get database
db = client.pluto

# get collection
posts = db.posts

# write to posts collection
def write(stamps):
    for stamp in stamps:
        item = {
            'stamp': stamp
        }
        db.posts.update_one(item, {'$set':item}, upsert=True)

# read posts collection
def read():
    stamps = []

    # get last 5 entries    
    for post in posts.find().sort('stamp',pymongo.DESCENDING).limit(5):
        stamps.append(post['stamp'])
    return stamps

# delete posts collection data
def delete():
    posts.remove({}) 