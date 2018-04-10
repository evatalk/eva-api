from handlers.readers.information_analyzer import \
    FinishedCoursesInformationAnalyzer


class EvaResponseWriter(object):

    def __init__(self, user_informations):
        self.user_informations = user_informations

    def finished_courses_response(self):
        """
        Returns a dictionary containing the courses finalized
        by the user divided into the appropriate predefined
        time intervals.
        """
        finished_courses_data = self._analyze_data_finished_courses(
            self.user_informations)

        return finished_courses_data

    def _analyze_data_finished_courses(self, user_informations):
        """
        It analyzes all the information obtained from
        a user and divides them according to the date
        of completion of the course.
        """
        information_analyzer = FinishedCoursesInformationAnalyzer(
            user_informations)

        information_analyzer.analyze()

        analyzed_data = information_analyzer.data_analyzed

        return analyzed_data
