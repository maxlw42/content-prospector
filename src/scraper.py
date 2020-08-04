import classifier
import praw
import yaml
import io

class ContentScraper:
    def __init__(self):
        self.reddit = praw.Reddit('me')
        self.subs_and_keywords = self.parse_subs_and_keywords()
        self.content_filter = classifier.ContentClassifier(self.subs_and_keywords)

    def parse_subs_and_keywords(self):
        # load in yaml file containing desired subs and keywords
        with open("../content.yaml", 'r') as stream:
            subs_and_keywords = yaml.safe_load(stream)
        return subs_and_keywords

    def stream_content(self):
        # use streams for submissions, search somehow
        subs_as_string = "+".join(self.subs_and_keywords.keys())
        for submission in self.reddit.subreddit(subs_as_string).stream.submissions():
            if self.content_filter.is_relevant_submission(submission):
                print(submission.title)
    

if __name__ == "__main__":
    scraper = ContentScraper()
    scraper.stream_content();
