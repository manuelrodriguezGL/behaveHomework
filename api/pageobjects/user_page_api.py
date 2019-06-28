import requests

from api.pageobjects.page_base_api import ApiBase


class Users(ApiBase):
    USERS_BASE_URL = 'api/users/'

    @property
    def all_users(self):
        response = requests.get("{}{}".format(self.url, self.USERS_BASE_URL), auth=self.auth, verify=False)
        return response.json(), response.status_code

    def delete_user(self, user_id):
        response = requests.delete("{}{}{}".format(self.url, self.USERS_BASE_URL, "{}/".format(user_id)), auth=self.auth)
        return response.status_code
