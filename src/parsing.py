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

    def parse_query(self, query):
        query_len = len(query)
        if query_len >= 5 and query[0:4] == "~OR(" and query[query_len - 1:] == ")":
            keyword_list = query[4:query_len - 1].split(",")
            return MultiQuery(keyword_list, "OR")
        elif query_len >= 6 and query[0:5] == "~AND(" and query[query_len - 1:] == ")":
            keyword_list = query[4:query_len - 1].split(",")
            return MultiQuery(keyword_list, "AND")
        elif len(query.split()) > 1:
            return SingleQuery(query, "PHRASE")
        else:
            return SingleQuery(query, "WORD")

    def parse_reddit_credentials(self):
        # load in yaml file containing reddit credentials
        yaml_content = self.parse_config_yaml("./secrets/reddit-creds.yaml")
        return yaml_content

    def parse_email_credentials(self):
        yaml_content = self.parse_config_yaml("./secrets/email-creds.yaml")
        return yaml_content

class Query:
    def __init__(self, query_type):
        self.query_type = query_type

    def is_word_query(self):
        return self.query_type is "WORD"

    def is_phrase_query(self):
        return self.query_type is "PHRASE"

    def is_and_query(self):
        return self.query_type is "AND"

    def is_or_query(self):
        return self.query_type is "OR"

class SingleQuery(Query):
    def __init__(self, query_text, query_type):
        super().__init__(query_type)
        self.query_text = query_text

class MultiQuery(Query):
    def __init__(self, query_text_list, query_type):
        super().__init__(query_type)
        self.query_text_list = query_text_list

if __name__ == "__main__":
    parser = ConfigParser()
    query_one = parser.parse_query("~AND(h, x)")
    query_two = parser.parse_query("~OR(h t,x,j)")
    query_three = parser.parse_query("bubble blower")
    query_four = parser.parse_query("bubble")
    print(query_one.is_and_query())
    print(query_two.is_or_query())
    print(query_three.is_phrase_query())
    print(query_four.is_word_query())