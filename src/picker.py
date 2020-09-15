import praw
import parsing
import Levenshtein as lev

class ContentPicker:
    def __init__(self, subs_to_keywords):
        self.subs_to_keywords = subs_to_keywords
        self.parser = ConfigParser()

    def is_close_match(self, text_a, text_b):
        return lev.distance(text_a, text_b) <= 2

    def text_contains_word(self, text, word):
        text_word_list = text.lower().split()
        for i in range(len(text_word_list)):
            if self.is_close_match(text_word_list[i], word):
                return True
        return False

    def text_contains_phrase(self, text, phrase):
        text_word_list = text.lower().split()
        phrase_word_list = phrase.lower().split()
        joined_phrase = "+".join(phrase_word_list)
        phrase_len = len(phrase_word_list)
        text_len = len(text_word_list)
        num_iterations = text_len - phrase_len + 1
        for i in range(num_iterations):
            joined_words_in_text = "+".join(text_word_list[i:i+phrase_len])
            if self.is_close_match(joined_words_in_text, joined_phrase):
                return True
        return False 


    def text_contains_one_of(self, text, keyword_list):
        text_contains_one = False
        for keyword in keyword_list:
            if len(keyword.split(" ")) > 1 and self.text_contains_phrase(keyword):
                text_contains_one = True
            elif self.text_contains_word(keyword):
                text_contains_one = True
        return text_contains_one
    
    def text_contains_all_of(self, text, keyword_list):
        text_contains_all = True
        for keyword in keyword_list:
            if len(keyword.split(" ")) > 1 and not self.text_contains_phrase(keyword):
                text_contains_all = False
            elif not self.text_contains_word(keyword):
                text_contains_all = False
        return text_contains_all

    
    def text_is_relevant(self, text, query):
        if query.is_phrase_query():
            return self.text_contains_phrase(text, query.query_text)
        elif query.is_word_query():
            return self.text_contains_word(text, query.query_text)
        elif query.is_and_query():
            return self.text_contains_all_of(text, query.keyword_list)
        elif query.is_or_query():
            return self.text_contains_one_of(text, query.keyword_list)
        else:
            raise ValueError("There is an invalid keyword in content.yaml")

    def submission_is_relevant(self, submission):
        sub = submission.subreddit
        sub_title = sub.display_name.lower()
        keywords_and_phrases = self.subs_to_keywords[sub_title]
        for keyword_query in keywords_and_phrases:
            body_relevant = self.text_is_relevant(submission.selftext, keyword_query)
            title_relevant = self.text_is_relevant(submission.title, keyword_query)
            if body_relevant or title_relevant:
                return True 
        return False

if __name__ == "__main__":
    picker = ContentPicker({})