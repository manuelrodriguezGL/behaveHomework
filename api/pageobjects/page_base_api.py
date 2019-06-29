import json

import urllib3
from requests.auth import HTTPBasicAuth


class ApiBase:
    def __init__(self, base_url, username, password):
        self.username = username
        self.password = password
        self.base_url = base_url
        self.auth = HTTPBasicAuth(self.username, self.password)
        urllib3.disable_warnings()

    @property
    def url(self):
        return self.base_url

    def json_loader(self, filename):
        with open(filename, 'r') as f:
            print(filename)
            data = json.load(f)
        return data
