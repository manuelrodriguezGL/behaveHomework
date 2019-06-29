import pytest

from acceptance.utils.read_env_config import ReadEnvConfig
from api.configurations.test_case_base import TestCaseBase
from api.pageobjects.user_page_api import UsersPage


class TestUserSuite(TestCaseBase):
    base_data_path = "../data/" # DEBUG ONLY!!!
    # base_data_path = "api/data/" # DELPOY ONLY !!!

    def setUp(self) -> None:
        super().setUp()
        self.json = self.json_loader("{}test_data.json".format(self.base_data_path))

    @pytest.mark.api_remove_user
    def test_delete_user(self):
        user_instance = UsersPage(ReadEnvConfig.get_app_api_url(), self.json['username'], self.json['password'])
        username = self.json_loader("{}test_users.json".format(self.base_data_path))['username']
        user_id = user_instance.get_user_id_by_username(username)
        status_code = user_instance.delete_user(user_id)
        assert status_code == 204, "The user was not removed. Status code is not 204."
