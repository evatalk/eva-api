from datetime import datetime, timedelta

from handlers.readers.information_map import USER_INFORMATION_MAP


class FinishedCoursesInformationAnalyzer(object):

    def __init__(self, informations):
        self.information_data = informations
        self.history_analysis = {
            "after_2015": [],
            "between_2013_to_2014": [],
            "before_2013": [],
        }

    @property
    def data_analyzed(self):
        return self.history_analysis

    def analyze(self):
        for user_data in self.information_data:
            extract_data = self._extract_data(user_data)

            # Analyze the data by end date
            self._analysis_end_date(extract_data)

    def _analysis_end_date(self, extracted_information_data):
        datetime_analyzer = DateTimeAnalyzer(
            extracted_information_data["course_end_date_value"])

        end_date = datetime_analyzer.get_date()

        date_equals_2015 = datetime(2015, 1, 1)
        date_equals_2013 = datetime(2013, 1, 1)

        if end_date is not None:
            check_if_user_finishes_after_2015 = datetime_analyzer.compare_dates(
                end_date, date_equals_2015)

            check_if_user_finishes_before_2013 = datetime_analyzer.compare_dates(
                date_equals_2013, end_date)

            if check_if_user_finishes_after_2015:
                self.history_analysis["after_2015"].append(
                    extracted_information_data)

            elif check_if_user_finishes_before_2013:
                self.history_analysis["before_2013"].append(
                    extracted_information_data)

            else:
                self.history_analysis["between_2013_to_2014"].append(
                    extracted_information_data)

    def _extract_data(self, user_information_list):
        course_name_value = user_information_list[USER_INFORMATION_MAP["nome_curso"]]
        workload_value = user_information_list[USER_INFORMATION_MAP["carga_horaria"]]
        teaching_format_value = user_information_list[USER_INFORMATION_MAP["formato"]]
        enrollment_status_value = user_information_list[USER_INFORMATION_MAP["sit_matricula"]]
        class_status_value = user_information_list[USER_INFORMATION_MAP["sit_turma"]]
        course_end_date_value = user_information_list[USER_INFORMATION_MAP["dt_fim"]]

        return {
            "course_name": course_name_value,
            "workload": workload_value,
            "teaching": teaching_format_value,
            "enrollment": enrollment_status_value,
            "class_status": class_status_value,
            "course_end_date": course_end_date_value,
        }


class DateTimeAnalyzer(object):

    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def compare_dates(cls, date, date_to_compare):
        return date >= date_to_compare

    def get_date(self):
        splited_date = self._split_datetime(self.date_string)

        if splited_date is None:
            return None

        date_informations = self._get_year_month_day(splited_date)

        if date_informations is None:
            return None

        datetime_instance = self._create_a_datetime_instance(date_informations)

        if datetime_instance is None:
            return None

    def _split_datetime(self, date_string):
        try:
            date = date_string[:10].split("-")
        except IndexError:
            return None

        return date

    def _get_year_month_day(self, date):
        YEAR = 0
        MONTH = 1
        DAY = 2

        try:
            year = date[YEAR]
            month = date[MONTH]
            day = date[DAY]
        except IndexError:
            return None

        return (year, month, day)

    def _create_a_datetime_instance(self, date):
        YEAR = 0
        MONTH = 1
        DAY = 2

        try:
            date = datetime(date[YEAR], date[MONTH], date[DAY])
        except (TypeError, ValueError):
            return None

        return date
