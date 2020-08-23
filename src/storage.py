import pymongo
from pymongo import MongoClient
from pprint import pprint

class VisitedSubmissionList:
    def __init__(self): 
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client.content_prospector
    
    def insert_submission_id(self, submission_id):
        self.db.submission_ids.insert_one({ "id" : submission_id })

    def check_submission_id(self, submission_id):
        if self.db.submission_ids.find({ "id" : submission_id }).count() > 0:
            return True
        return False

    def clear_submission_list(self):
        self.client.drop_database('content_prospector')

