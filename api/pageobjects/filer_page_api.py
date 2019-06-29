import requests

from api.pageobjects.page_base_api import ApiBase


class FilerPage(ApiBase):
    FILES_BASE_URL = 'api/folders/'

    base_data_path = "api/data/"  # DEBUG ONLY!!!

    # base_data_path = "api/data/" # DELPOY ONLY !!!

    def all_folders(self):
        response = requests.get("{}{}".format(self.url, self.FILES_BASE_URL), auth=self.auth, verify=False)
        return response.json(), response.status_code

    def get_folder_id_by_foldername(self, foldername):
        folder_id = None
        try:
            folders, status_code = self.all_folders()
            if status_code == 200:
                for folder in folders:
                    if folder['name'] == foldername:
                        folder_id = folder['pk']
        except Exception as e:
            print(e.__cause__)
        finally:
            return folder_id

    def get_folder_id_by_foldername_contains(self, foldername):
        folder_id = None
        try:
            folders, status_code = self.all_folders()
            if status_code == 200:
                for folder in folders:
                    if foldername in folder['name']:
                        folder_id = folder['pk']
        except Exception as e:
            print(e.__cause__)
        finally:
            return folder_id

    def delete_folder(self, folder_id):
        response = requests.delete("{}{}{}".format(self.url, self.FILES_BASE_URL, "{}/".format(folder_id)),
                                   auth=self.auth)
        return response.status_code

    def create_folder(self):
        data = self.json_loader("{}folder_data.json".format(self.base_data_path))
        response = requests.post("{}{}".format(self.url, self.FILES_BASE_URL), data, auth=self.auth)
        return response.status_code
