import csv
from information_map import USER_INFORMATION


class StorageInformationReader(object):

    def __init__(self, file_name):
        self.csv_file_name = file_name

    def check_if_enrollment_exists(self, enrollment):
        with open(self.csv_file_name, "r", encoding='utf-16-le', newline='') as user_data_storage:
            for user_data_row in user_data_storage:
                user_informations = user_data_row.split("|")
                if user_informations[USER_INFORMATION["cod_matricula"]] == enrollment:
                    return True

            return False