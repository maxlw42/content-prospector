import praw
import Levenshtein as lev

class ContentPicker:
    def __init__(self, subs_to_keywords):
        self.subs_to_keywords = subs_to_keywords

    def text_contains_word(self, text_word_list, word):
        return word.lower() in text_word_list

    def text_contains_phrase(self, text, phrase):
        text_word_list = text.lower().split()
        phrase_word_list = phrase.lower().split()
        joined_phrase = "+".join(phrase_word_list)
        phrase_len = len(phrase_word_list)
        text_len = len(text_word_list)
        num_iterations = text_len - phrase_len + 1
        for i in range(num_iterations):
            joined_words_in_text = "+".join(text_word_list[i:i+phrase_len])
            if joined_words_in_text == joined_phrase:
                return True
        return False 
    
    def text_is_relevant(self, text, keyword):
        keyword_is_phrase = len(keyword.split()) > 1
        if keyword_is_phrase:
            return self.text_contains_phrase(text, keyword)
        else:
            return self.text_contains_word(text, keyword)

    def submission_is_relevant(self, submission):
        sub = submission.subreddit
        sub_title = sub.display_name.lower()
        keywords_and_phrases = self.subs_to_keywords[sub_title]
        for keystr in keywords_and_phrases:
            body_relevant = self.text_is_relevant(submission.selftext, keystr)
            title_relevant = self.text_is_relevant(submission.title, keystr)
            if body_relevant or title_relevant:
                return True 
        return False

if __name__ == "__main__":
    picker = ContentPicker({})