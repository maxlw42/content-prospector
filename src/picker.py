
class ContentPicker:
    def __init__(self, subs_to_keywords):
        self.subs_to_keywords = subs_to_keywords

    def title_is_relevant(self, submission, keyword):
        title = submission.title
        return title.find(keyword) != -1
    
    def body_is_relevant(self, submission, keyword):
        body = submission.selftext
        return body.find(keyword) != -1

    def submission_is_relevant(self, submission):
        sub = submission.subreddit
        sub_title = sub.display_name
        keywords = self.subs_to_keywords[sub_title]
        for keyword in keywords:
            body_relevant = self.body_is_relevant(submission, keyword)
            title_relevant = self.title_is_relevant(submission, keyword)
            if body_relevant or title_relevant:
                return True 
        return False
