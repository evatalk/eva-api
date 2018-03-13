import csv

from eva.settings import INFORMATIONS_STORAGE_PATH
from handlers.readers.information_map import USER_INFORMATION_MAP
from handlers.writers.jsonifiers import Jsonify


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

    def user_courses_history(self, cpf_user_intendifier):
        """
        Identifies the student's entire history, showing the courses
        in progress and those already completed, the class situation
        and the enrollment situation
        """
        history_data = []

        with open(self.csv_file_name, "r", encoding='utf-16-le', newline='') as user_data_storage:

            for user_data_row in user_data_storage:
                user_informations = user_data_row.split("|")

                # Check if informed CPF exists
                if user_informations[USER_INFORMATION_MAP["cpf"]] == cpf_user_intendifier:

                    json_user_history_data = Jsonify.user_history_data(
                        user_informations)

                    history_data.append(json_user_history_data)

            return history_data
    
    def list_user_courses_by_enrollement(self, user_enrollement):
        
        courses = []

        with open(self.csv_file_name, "r", encoding='utf-16-le', newline='') as user_data_storage:

            for user_data_row in user_data_storage:
                user_informations = user_data_row.split("|")

                # Check informed enrollement 
                if user_informations[USER_INFORMATION_MAP["cod_matricula"]] == user_enrollement:

                    courses.append(user_informations)

            return courses