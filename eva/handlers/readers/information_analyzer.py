from datetime import datetime
from datetime import timedelta


class UserInformationAnalyzer(object):
    # format example 2015-05-08 16:38:45.000
    pass


class DateTimeAnalyzer(object):
    
    @classmethod
    def compare_dates(cls, date, date_to_compare):
        return date > date_to_compare

    def get_date(self, date_string):
        splited_date = self._split_datetime(date_string)

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
