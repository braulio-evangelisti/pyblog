import pymongo
from pymongo import MongoClient


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard  # DB
        self.Users = self.db.users

    def insert_user(self, data):
        id = self.Users.insert({"username": data.username, "display_name": data.display_name, "password": data.password, "email": data.email})
        print("uid is", id)

