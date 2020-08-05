import picker
import praw
import yaml
import io
import logging
import prawcore.exceptions

class ContentScraper:
    def __init__(self):
        self.reddit = praw.Reddit('me')
        self.subs_and_keywords = self.parse_subs_and_keywords()
        self.content_filter = picker.ContentPicker(self.subs_and_keywords)
        
    def parse_subs_and_keywords(self):
        # load in yaml file containing desired subs and keywords
        with open("../content.yaml", 'r') as stream:
            subs_and_keywords = yaml.safe_load(stream)
        return subs_and_keywords

    def validate_sub_names(self):
        subs_are_valid = True
        sub_names = self.subs_and_keywords.keys()
        # run through each subreddit name, catching exceptions indicating invalid subreddit
        for sub_name in sub_names:
            try:
                sub_id = self.reddit.subreddit(sub_name).id
            except prawcore.exceptions.Redirect:
                subs_are_valid = False
                logging.error(sub_name + " is an invalid subreddit name.")
        return subs_are_valid

    def stream_content(self):
        # validate subreddits in content.yaml before streaming
        if not self.validate_sub_names():
            raise ValueError("There is an invalid subreddit name in content.yaml")

        # use streams for submissions, search somehow
        subs_as_string = "+".join(self.subs_and_keywords.keys())
        for submission in self.reddit.subreddit(subs_as_string).stream.submissions():
            if self.content_filter.submission_is_relevant(submission):
                print(submission.title)
    

if __name__ == "__main__":
    scraper = ContentScraper()
    scraper.stream_content()
