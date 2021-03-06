import picker
import notifier
import parsing
import storage
import praw
import yaml
import io
import logging
import prawcore.exceptions

class ContentScraper:
    def __init__(self):
        self.config_parser = parsing.ConfigParser()
        self.subs_and_keywords = self.config_parser.parse_subs_and_keywords()
        reddit_credentials = self.config_parser.parse_reddit_credentials()
        self.reddit = praw.Reddit(client_id=reddit_credentials['client_id'],
                                  client_secret=reddit_credentials['client_secret'],
                                  user_agent=reddit_credentials['user_agent'],
                                  username=reddit_credentials['username'],
                                  password=reddit_credentials['password'])

        self.content_picker = picker.ContentPicker(self.subs_and_keywords)
        self.content_notifier = notifier.ContentNotifier()
        self.visited_submission_storage = storage.VisitedSubmissionStorage()
    
    def validate_sub_names(self):
        subs_are_valid = True
        sub_names = self.subs_and_keywords.keys()
        for sub_name in sub_names:
            try:
                sub_id = self.reddit.subreddit(sub_name).id
            except prawcore.exceptions.Redirect:
                subs_are_valid = False
                logging.error(sub_name + " is an invalid subreddit name in content.yaml.")
        return subs_are_valid

    def stream_content(self):
        if not self.validate_sub_names():
            raise ValueError("There is an invalid subreddit name in content.yaml")

        subs_as_string = "+".join(self.subs_and_keywords.keys())
        for submission in self.reddit.subreddit(subs_as_string).stream.submissions():
            submission_is_relevant = self.content_picker.submission_is_relevant(submission)
            submission_is_visited = self.visited_submission_storage.check_submission_id(submission.id)
            if submission_is_relevant and not submission_is_visited:
                self.content_notifier.send_email_notification(submission)
                self.visited_submission_storage.mark_submission_id(submission.id)
    

if __name__ == "__main__":
    scraper = ContentScraper()
    scraper.stream_content()
