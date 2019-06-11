import json
import unittest


class TestCaseBase(unittest.TestCase):
    json_path = ""

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def json_loader(self, filename):
        with open(filename, 'r') as f:
            print(filename)
            data = json.load(f)
        return data
