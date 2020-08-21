from pymongo import MongoClient
from pprint import pprint

class VisitedSubmissionList:
    def __init__(self): 
        client = MongoClient("mongodb://localhost:27017")
        self.db = client.content_prospector
    
    def insert_submission_id(self, submission_id):
        self.db.submission_ids.insert_one({submission_id : submission_id})

    def check_submission_id(self, submission_id):
        return None

    def clear_submission_list(self):
        return None


if __name__ == "__main__":
    list = VisitedSubmissionList()
    list.insert_submission_id("345272")
