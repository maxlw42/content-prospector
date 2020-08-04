
class ContentClassifier:
    def __init__(self, subs_to_keywords):
        self.subs_to_keywords = subs_to_keywords

    def is_relevant_submission(self, submission):
        sub = submission.subreddit
        sub_title = sub.display_name
        keywords = self.subs_to_keywords[sub_title]
        for keyword in keywords:
            if submission.title.find(keyword) != -1:
                return True 
        return False
