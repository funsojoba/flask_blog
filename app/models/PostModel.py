from ..app import mongo
from flask import request, json
from flask_pymongo import ObjectId

from app.helpers.Utility import toDictionaryArray

from datetime import datetime


class PostModel:
    def __init__(self):
        pass
    
    
    def getPost(self, _id):
        posts = mongo.db.posts.find({'_id': ObjectId(_id)})
        post = toDictionaryArray(posts)[0]
        return post
    
    def addPost(self, title, content, image=None):
        date = datetime.now()
        insert_data = {
            "title":title,
            "content":content,
            "image":image,
            "status":1,
            "created_at": date,
            "updated_at": date
            }
        response = mongo.db.posts.insert(insert_data)
        return str(ObjectId(response))
    
    def updatePost(self, _id, title, content, image=None):
        date = datetime.now()
        update_data = {
            "title":title,
            "content":content,
            "image":image,
            "status":1,
            "updated_at": date
            }
        
        mongo.db.posts.update({'_id': ObjectId(_id)}, {"$set": update_data}, False, True)
        return _id
    
    def delete_post(self, _id):
        mongo.db.posts.delete({"_id":ObjectId(_id)})
    
post_model = PostModel()