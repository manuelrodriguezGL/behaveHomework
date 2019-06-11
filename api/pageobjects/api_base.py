import urllib3
from requests.auth import HTTPBasicAuth


class ApiBase:

    def __init__(self, app_base_url, username, password):
        self.username = username
        self.password = password
        self.app_base_url = app_base_url
        self.auth = HTTPBasicAuth(self.username, self.password)
        urllib3.disable_warnings()

    @property
    def url(self):
        return self.app_base_url
