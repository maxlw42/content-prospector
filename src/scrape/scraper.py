import praw

def redditAuth():
    # login to Reddit with creds from .ini file
    reddit = praw.Reddit('me')
    

if __name__ == "__main__":
    redditAuth();
