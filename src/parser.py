import yaml

class ConfigParser:
    def __init__(self):
        print(None)

    def parse_config_yaml(self, path_to_file):
        config_content = {}
        with open(path_to_file, 'r') as stream:
            config_content = yaml.safe_load(stream)
        return config_content

    def parse_subs_and_keywords(self):
        # load in yaml file containing desired subs and keywords
        yaml_content = self.parse_config_yaml("../config/content.yaml")
        subs_and_keywords = {k.lower() : v for k, v in yaml_content.items()}
        return subs_and_keywords

    def parse_reddit_credentials(self):
        # load in yaml file containing reddit credentials
        yaml_content = self.parse_config_yaml("../config/secrets/creds.yaml")
        return yaml_content
    