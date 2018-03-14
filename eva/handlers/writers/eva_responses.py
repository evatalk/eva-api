from handlers.conversations.responses import RESPONSE_MAP
from handlers.readers.information_analyzer import FinishedCoursesInformationAnalyzer
from handlers.writers.text_helpers import TextHandler


class EvaResponseWriter(object):

    def __init__(self, user_informations):
        self.user_informations = user_informations

    def finished_courses_response(self):
        finished_courses_data = self._analyze_data_finished_courses(
            self.user_informations)

        if finished_courses_data["after_2015"] is not None:
            list_of_course_names = self._get_list_of_finished_courses(
                finished_courses_data["after_2015"])

            # TextHandler.concatenate_information_to_text(,)

        if finished_courses_data["between_2013_to_2014"] is not None:
            list_of_course_names = self._get_list_of_finished_courses(
                finished_courses_data["between_2013_to_2014"])

            # TextHandler.concatenate_information_to_text(,)

        if finished_courses_data["before_2013"] is not None:
            list_of_course_names = self._get_list_of_finished_courses(
                finished_courses_data["before_2013"])

            # TextHandler.concatenate_information_to_text(,)

    def _analyze_data_finished_courses(self, user_informations):
        information_analyzer = FinishedCoursesInformationAnalyzer(
            user_informations)
        information_analyzer.analyze()

        analyzed_data = information_analyzer.data_analyzed

        return analyzed_data

    def _get_list_of_finished_courses(self, dict_data):
        course_names = []

        for data in dict_data:
            course_names.append(data["course_name"])

        return course_names
