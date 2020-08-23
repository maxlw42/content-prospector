import pymongo
from pymongo import MongoClient
from pprint import pprint

class VisitedSubmissionStorage:
    def __init__(self): 
        self.client = MongoClient("mongodb://mongo:27017")
        self.db = self.client.content_prospector
    
    # mark a submission id as visited
    def mark_submission_id(self, submission_id):
        self.db.submission_ids.insert_one({ "id" : submission_id })

    # return true if submission has already been sent through notification, false otherwise
    def check_submission_id(self, submission_id):
        if self.db.submission_ids.find({ "id" : submission_id }).count() > 0:
            return True
        return False

    # clear the current store of visited submissions
    def clear_submission_list(self):
        self.client.drop_database('content_prospector')

