import configparser
import json
import requests

class Common:
    def url(self):
        config = configparser.ConfigParser()
        config.read('./utilities/properties.cfg')
        url = (config['api']['endpoint'])
        return url

    def open_jsonData(path):
        with open(path) as f:
            json_request = json.loads(f.read())
        return json_request