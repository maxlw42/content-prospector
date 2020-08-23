import praw
import Levenshtein as lev

class ContentPicker:
    def __init__(self, subs_to_keywords):
        self.subs_to_keywords = subs_to_keywords

    def title_is_relevant(self, submission, keyword):
        title = submission.title
        return keyword.lower() in title.lower()
    
    def body_is_relevant(self, submission, keyword):
        body = submission.selftext
        return keyword.lower() in body.lower()

    def submission_is_relevant(self, submission):
        sub = submission.subreddit
        sub_title = sub.display_name.lower()
        keywords_and_phrases = self.subs_to_keywords[sub_title]
        for keystr in keywords_and_phrases:
            body_relevant = self.body_is_relevant(submission, keystr)
            title_relevant = self.title_is_relevant(submission, keystr)
            if body_relevant or title_relevant:
                return True 
        return False
