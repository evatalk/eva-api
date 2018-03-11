import csv

from eva.settings import INFORMATIONS_STORAGE_PATH

from .information_map import USER_INFORMATION_MAP


class StorageInformationReader(object):

    def __init__(self, file_name):
        self.csv_file_name = file_name

    def check_the_information_veracity(self, informed_cpf, informed_email):
        """
        If the data entered is valid, it returns the complete information of the user.
        Otherwise, returns None.
        """
        with open(self.csv_file_name, "r", encoding='utf-16-le', newline='') as user_data_storage:
            for user_data_row in user_data_storage:
                user_informations = user_data_row.split("|")
                # Check if informed CPF exists
                if user_informations[USER_INFORMATION_MAP["cpf"]] == informed_cpf:
                    # The e-mail exists, now we gonna check the e-mail
                    if user_informations[USER_INFORMATION_MAP["login_liferay"]] == informed_email:
                        # Returns the user informations
                        return True, user_informations

                    # The CPF exists, but the e-mail don't
                    return False, None

            # Informed data is invalid
            return False, None
