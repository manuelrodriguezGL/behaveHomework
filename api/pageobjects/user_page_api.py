import requests

from api.pageobjects.page_base_api import ApiBase


class UsersPage(ApiBase):
    USERS_BASE_URL = 'api/users/'

    def all_users(self):
        response = requests.get("{}{}".format(self.url, self.USERS_BASE_URL), auth=self.auth, verify=False)
        return response.json(), response.status_code

    def get_user_id_by_username(self, username):
        user_id = None
        try:
            users, status_code = self.all_users()
            if status_code == 200:
                for user in users:
                    if user['username'] == username:
                        user_id = user['pk']
        except Exception as e:
            print(e.__cause__)
        finally:
            return user_id

    def get_user_id_by_username_contains(self, username):
        user_id = None
        try:
            users, status_code = self.all_users()
            if status_code == 200:
                for user in users:
                    if username in user['username']:
                        user_id = user['pk']
        except Exception as e:
            print(e.__cause__)
        finally:
            return user_id

    def delete_user(self, user_id):
        response = requests.delete("{}{}{}".format(self.url, self.USERS_BASE_URL, "{}/".format(user_id)), auth=self.auth)
        return response.status_code
