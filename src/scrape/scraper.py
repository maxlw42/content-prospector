import praw
import yaml
import io

class ContentScraper:
    def __init__(self):
        self.reddit = praw.Reddit('me')
        self.subs_and_keywords = self.parse_subs_and_keywords()

    def parse_subs_and_keywords(self):
        # load in yaml file containing desired subs and keywords
        with open("../../content.yaml", 'r') as stream:
            subs_and_keywords = yaml.safe_load(stream)
        return subs_and_keywords

    def stream_content(self):
        # use streams for submissions, search somehow
        subs_as_string = "+".join(self.subs_and_keywords.keys())
        for submission in self.reddit.subreddit(subs_as_string).stream.submissions():
            print(submission.subreddit.display_name + " : " + submission.title)
    

if __name__ == "__main__":
    scraper = ContentScraper()
    scraper.stream_content();
    
