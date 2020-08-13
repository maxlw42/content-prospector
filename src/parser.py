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
        subs_and_keywords = {k.lower() : v for k, v in yaml_content.items()}
        return subs_and_keywords

    def parse_reddit_credentials(self):
        # load in yaml file containing reddit credentials
        yaml_content = self.parse_config_yaml("./secrets/reddit-creds.yaml")
        return yaml_content

    def parse_email_credentials(self):
        yaml_content = self.parse_config_yaml("./secrets/email-creds.yaml")
        return yaml_content
    