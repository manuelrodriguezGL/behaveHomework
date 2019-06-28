import urllib3
# from requests.auth import HTTPBasicAuth

from api.utils.auth_util import AuthUtil


class ApiBase:
    def __init__(self, base_url, username, password):
        self.username = username
        self.password = password
        self.base_url = base_url
        self.auth = AuthUtil(username, password)
        # self.auth = HTTPBasicAuth(self.username, self.password)
        urllib3.disable_warnings()

    @property
    def url(self):
        return self.base_url
