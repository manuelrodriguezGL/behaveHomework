import random

import pytest

from acceptance.utils.read_env_config import ReadEnvConfig
from api.configurations.test_case_base import TestCaseBase
from api.pageobjects.user_api import Users


class TestUsers(TestCaseBase):
    random_number_delete = 0

    def setUp(self) -> None:
        super().setUp()
        # self.json = self.json_loader("../data/json1.json")
        self.json = self.json_loader("api/data/json1.json")

    @pytest.mark.full_regression
    def test_create_user_no_stuff(self):
        random_number = random.randint(1, 1000)

        print(self.json)
        user_instance = Users(ReadEnvConfig.get_app_api_url(), self.json["username"], self.json["password"])
        resp, status_code = user_instance.create_user(
            username="UserTest1_{}".format(random_number),
            email="UserTest_{}@test.com".format(random_number),
            is_staff=False
        )

        # check the status code is 201 = created
        assert status_code == 201, "Wrong status code"
        assert resp['username'] == "UserTest1_{}".format(random_number), "Wrong username"
        assert resp['email'] == "UserTest_{}@test.com".format(random_number), "Wrong username"

    @pytest.mark.full_regression
    def test_create_user_stuff(self):
        random_number = random.randint(1, 1000)
        user_instance = Users(ReadEnvConfig.get_app_api_url(), self.json["username"], self.json["password"])
        resp, status_code = user_instance.create_user(
            username="UserTest1_{}".format(random_number),
            email="UserTest_{}@test.com".format(random_number),
            is_staff=True
        )

        # check the status code is 201 = created
        assert status_code == 201, "Wrong status code"
        assert resp['username'] == "UserTest1_{}".format(random_number), "Wrong username"
        assert resp['email'] == "UserTest_{}@test.com".format(random_number), "Wrong username"

    @pytest.mark.full_regression
    def test_delete_user(self):
        # pre-step
        random_number = random.randint(1, 1000)
        user_instance = Users(ReadEnvConfig.get_app_api_url(), self.json["username"], self.json["password"])
        resp, status_code = user_instance.create_user(
            username="UserTest1_{}".format(random_number),
            email="UserTest_{}@test.com".format(random_number),
            is_staff=True
        )
        assert status_code == 201, "Not able to create the user."

        # test case
        status_code = user_instance.delete_user(resp['pk'])
        assert status_code == 204, "The user was not removed. Wrong status code."
        assert len([user for user in user_instance.all_users[0] if user['username'] == "UserTest1_{}".format(random_number)]) == 0, \
            "The user was found but it was supposed to be deleted, and it is not."
