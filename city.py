from vacancy import Vacancy


class City:
    def __init__(self, vacancy: Vacancy):
        self.__name = vacancy.area_name
        self.__vacancy_count = 1
        self.__all_salary = vacancy.average_salary
        self.__average_salary = vacancy.average_salary

    @property
    def average_salary(self):
        return self.__average_salary

    @property
    def vacancy_count(self):
        return self.__vacancy_count

    def update(self, vacancy: Vacancy):
        self.__vacancy_count += 1
        self.__all_salary += vacancy.average_salary
        self.__average_salary = self.__all_salary / self.__vacancy_count
