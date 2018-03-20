import csv
from datetime import datetime

from eva.settings import INFORMATIONS_STORAGE_PATH
from handlers.readers.information_analyzer import DateTimeAnalyzer
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

    def user_courses_history_to_analyze(self, user_enrollement, user_cpf):
        """
        Returns a list of all courses that the user has already
        completed or is still attending based on cpf or enrollment,
        which will be analyzed later.
        """
        courses = []

        with open(self.csv_file_name, "r", encoding='utf-16-le', newline='') as user_data_storage:

            for user_data_row in user_data_storage:
                user_informations = user_data_row.split("|")

                # Check informed enrollement
                if (user_informations[USER_INFORMATION_MAP["cod_matricula"]] == user_enrollement
                        or user_informations[USER_INFORMATION_MAP["cpf"]] == user_cpf):
                    if user_informations[USER_INFORMATION_MAP["sit_matricula"]].strip(" ") == "Concluído":
                        courses.append(user_informations)

            return courses

    def courses_open_for_subscriptions(self, user_cpf):
        datetime_today = datetime.now()
        open_for_subscriptions = []

        with open(self.csv_file_name, "r", encoding='utf-16-le', newline='') as user_data_storage:

            for user_data_row in user_data_storage:
                user_informations = user_data_row.split("|")

                # Check if informed CPF exists
                if user_informations[USER_INFORMATION_MAP["cpf"]] == user_cpf:
                    date_end_subscription_text = user_informations[USER_INFORMATION_MAP["dt_fim_insc"]]
                    datetime_analyzer = DateTimeAnalyzer(
                        date_end_subscription_text)
                    date_end_subscription = datetime_analyzer.get_date()

                    if datetime_analyzer.compare_dates(date_end_subscription, datetime_today):
                        json_response = Jsonify.open_for_subscrition(
                            user_informations)
                        open_for_subscriptions.append(json_response)

            return open_for_subscriptions
