import pytest

from acceptance.utils.read_env_config import ReadEnvConfig
from api.configurations.test_case_base import TestCaseBase
from api.pageobjects.user_page_api import UsersPage


"""Delete one user:
    1. Get all users
    2. Search for the user name, and get the id
    3. delete it"""


class TestUserSuite(TestCaseBase):
    base_data_path = "../data/" # DEBUG ONLY!!!
    # base_data_path = "api/data/" # DELPOY ONLY !!!

    def setUp(self) -> None:
        super().setUp()
        self.json = self.json_loader("{}test_data.json".format(self.base_data_path))

    def searchByUsername(self, username):
        return UsersPage.get_user_id_by_username(username)

    @pytest.mark.api_remove_user
    def test_delete_user(self):
        user_instance = UsersPage(ReadEnvConfig.get_app_api_url(), self.json["usermame"], self.json["password"])
        username = self.json_loader("{}test_users.json".format(self.base_data_path))['username']
        user_id = self.searchByUsername(username)
        status_code = user_instance.delete_user(user_id)
        assert status_code == 204, "The user was not removed. Status code is not 204."
