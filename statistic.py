import math
from vacancy import Vacancy
from year import Year
from city import City


def check_statistics_preparedness(method):
    def wrapper(self):
        if not self.fulfillment:
            self.calculate_statistics()
        return method(self)
    return wrapper


class Statistic:
    def __init__(self, selected_vacancy: str):
        self.__selected_vacancy = selected_vacancy
        self.__vacancies_count = 0
        self.__cities = {}
        self.__years = {}

        self.__salary_dynamics = {}
        self.__num_vacancies_dynamics = {}
        self.__selected_salary_dynamics = {}
        self.__selected_num_vacancies_dynamics = {}
        self.__city_salary_dynamics = {}
        self.__city_num_vacancies_dynamics = {}

        self.fulfillment = False

    @property
    @check_statistics_preparedness
    def salary_dynamics(self):
        return self.__salary_dynamics

    @property
    @check_statistics_preparedness
    def num_vacancies_dynamics(self):
        return self.__num_vacancies_dynamics

    @property
    @check_statistics_preparedness
    def selected_salary_dynamics(self):
        return self.__selected_salary_dynamics

    @property
    @check_statistics_preparedness
    def selected_num_vacancies_dynamics(self):
        return self.__selected_num_vacancies_dynamics

    @property
    @check_statistics_preparedness
    def city_salary_dynamics(self):
        return self.__city_salary_dynamics

    @property
    @check_statistics_preparedness
    def city_num_vacancies_dynamics(self):
        return self.__city_num_vacancies_dynamics

    @property
    def years(self):
        return self.__years

    @property
    def cities(self):
        return self.__cities

    @property
    def selected_vacancy(self):
        return self.__selected_vacancy

    def enter_static_data(self, data):
        for row_dict in data:
            self.update(row_dict)

    def update(self, row_dict: dict):
        vacancy = Vacancy(row_dict)
        if vacancy.area_name not in self.__cities.keys():
            self.__cities[vacancy.area_name] = City(vacancy)
        else:
            self.__cities[vacancy.area_name].update(vacancy)
        if vacancy.year not in self.__years.keys():
            self.__years[vacancy.year] = Year(vacancy, self.__selected_vacancy)
        else:
            self.__years[vacancy.year].update(vacancy)
        self.__vacancies_count += 1

    def calculate_statistics(self):
        for year in self.__years.values():
            self.__salary_dynamics[year.name] = math.floor(year.average_salary)
            self.__num_vacancies_dynamics[year.name] = year.vacancy_count
            self.__selected_salary_dynamics[year.name] = math.floor(year.selected_vacancy_average_salary)
            self.__selected_num_vacancies_dynamics[year.name] = year.selected_vacancy_count
        self.__cities = dict(filter(lambda x: x[1].vacancy_count >= (self.__vacancies_count / 100),
                                    self.__cities.items()))
        self.__city_salary_dynamics = dict(sorted(self.__cities.items(),
                                                  key=lambda x: x[1].average_salary, reverse=True)[:10])
        self.__city_salary_dynamics = {key: math.floor(val.average_salary)
                                       for key, val in self.__city_salary_dynamics.items()}
        self.__city_num_vacancies_dynamics = dict(sorted(self.__cities.items(),
                                                         key=lambda x: x[1].vacancy_count, reverse=True)[:10])
        self.__city_num_vacancies_dynamics = {key: round(val.vacancy_count / self.__vacancies_count, 4)
                                              for key, val in self.__city_num_vacancies_dynamics.items()}
        self.fulfillment = True

    def print_statistics(self):
        self.calculate_statistics()
        print("Динамика уровня зарплат по годам:", self.__salary_dynamics)
        print("Динамика количества вакансий по годам:", self.__num_vacancies_dynamics)
        print("Динамика уровня зарплат по годам для выбранной профессии:", self.__selected_salary_dynamics)
        print("Динамика количества вакансий по годам для выбранной профессии:", self.__selected_num_vacancies_dynamics)
        print("Уровень зарплат по городам (в порядке убывания):", self.__city_salary_dynamics)
        print("Доля вакансий по городам (в порядке убывания):", self.__city_num_vacancies_dynamics)
