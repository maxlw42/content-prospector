import yaml

class ConfigParser:
    def parse_config_yaml(self, path_to_file):
        config_content = {}
        with open(path_to_file, 'r') as stream:
            config_content = yaml.safe_load(stream)
        return config_content

    def parse_subs_and_keywords(self):
        # load in yaml file containing desired subs and keywords
        yaml_content = self.parse_config_yaml("./content.yaml")
        # begin parsing subreddits an keywords here
        subs_and_keywords = {}
        for sub, keyword_query_list in yaml_content.items():
            parsed_query_list = []
            for keyword_query in keyword_query_list:
                parsed_query_list.append(self.parse_query(keyword_query))
            subs_and_keywords[sub.lower()] = parsed_query_list
        return subs_and_keywords

    def parse_query(self):
        return None

    def parse_reddit_credentials(self):
        # load in yaml file containing reddit credentials
        yaml_content = self.parse_config_yaml("./secrets/reddit-creds.yaml")
        return yaml_content

    def parse_email_credentials(self):
        yaml_content = self.parse_config_yaml("./secrets/email-creds.yaml")
        return yaml_content

class SingleQuery:
    def __init__(self, query_text, query_type):
        self.query_text = query_text
        self.type = query_type

    def is_word_query(self):
        return query_type is "WORD"
    
    def is_phrase_query(self):
        return query_type is "PHRASE"

class MultiQuery():
    def __init(self, single_query_list, query_type):
        self.query_text_list = query_text_list
        self.query_type = query_type

    def is_and_query(self):
        return query_type is "AND"
    
    def is_or_query(self):
        return query_type is "OR"