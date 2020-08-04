import praw
import yaml

class ContentStream:
    def __init__(self):
        self.reddit = praw.Reddit('me')

    def streamIt(self):
        # login to Reddit with creds from .ini file
    
        # use streams for submissions, search somehow
        for submission in self.reddit.subreddit("pics").stream.submissions():
            print(submission.subreddit.display_name + " : " + submission.title)
    

if __name__ == "__main__":
    stream = ContentStream()
    stream.streamIt();
    
