from vacancy import Vacancy


class Year:
    def __init__(self, vacancy: Vacancy, selected_vacancy: str):
        self.__name = vacancy.year
        self.__vacancy_count = 1
        self.__all_salary = vacancy.average_salary
        self.__average_salary = vacancy.average_salary
        self.__selected_vacancy = selected_vacancy

        self.__selected_vacancy_count = 1 if selected_vacancy in vacancy.name else 0
        self.__selected_vacancy_all_salary = \
            vacancy.average_salary if selected_vacancy in vacancy.name else 0
        self.__selected_vacancy_average_salary = \
            vacancy.average_salary if selected_vacancy in vacancy.name else 0

    @property
    def name(self):
        return self.__name

    @property
    def average_salary(self):
        return self.__average_salary

    @property
    def vacancy_count(self):
        return self.__vacancy_count

    @property
    def selected_vacancy_count(self):
        return self.__selected_vacancy_count

    @property
    def selected_vacancy_average_salary(self):
        return self.__selected_vacancy_average_salary

    def update(self, vacancy: Vacancy):
        self.__vacancy_count += 1
        self.__all_salary += vacancy.average_salary
        self.__average_salary = self.__all_salary / self.__vacancy_count

        if self.__selected_vacancy in vacancy.name:
            self.__selected_vacancy_count += 1
            self.__selected_vacancy_all_salary += vacancy.average_salary
            self.__selected_vacancy_average_salary = self.__selected_vacancy_all_salary / self.__selected_vacancy_count
