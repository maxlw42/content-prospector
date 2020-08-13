import picker
import notifier
import parser
import praw
import yaml
import io
import logging
import prawcore.exceptions

class ContentScraper:
    def __init__(self):
        # use a config parser to extract relevant parameters and credentials to login
        self.config_parser = parser.ConfigParser()
        self.subs_and_keywords = self.config_parser.parse_subs_and_keywords()
        reddit_credentials = self.config_parser.parse_reddit_credentials()
        self.reddit = praw.Reddit(client_id=reddit_credentials['client_id'],
                                  client_secret=reddit_credentials['client_secret'],
                                  user_agent=reddit_credentials['user_agent'],
                                  username=reddit_credentials['username'],
                                  password=reddit_credentials['password'])

        # modules for selecting relevant submissions and notifying user of submission
        self.content_picker = picker.ContentPicker(self.subs_and_keywords)
        self.content_notifier = notifier.ContentNotifier()
    

    def validate_sub_names(self):
        subs_are_valid = True
        sub_names = self.subs_and_keywords.keys()
        # run through each subreddit name, catching exceptions indicating invalid subreddit
        for sub_name in sub_names:
            try:
                sub_id = self.reddit.subreddit(sub_name).id
            except prawcore.exceptions.Redirect:
                subs_are_valid = False
                logging.error(sub_name + " is an invalid subreddit name in content.yaml.")
        return subs_are_valid

    def stream_content(self):
        # validate subreddits in content.yaml before streaming
        if not self.validate_sub_names():
            raise ValueError("There is an invalid subreddit name in content.yaml")

        # use streams for submissions, search somehow
        subs_as_string = "+".join(self.subs_and_keywords.keys())
        for submission in self.reddit.subreddit(subs_as_string).stream.submissions():
            if self.content_picker.submission_is_relevant(submission):
                print(submission.title)
                self.content_notifier.send_email_notification(submission)
    

if __name__ == "__main__":
    scraper = ContentScraper()
    scraper.stream_content()
