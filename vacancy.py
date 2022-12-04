class Vacancy:
    currency_to_rub = {"AZN": 35.68, "BYR": 23.91, "EUR": 59.90, "GEL": 21.74, "KGS": 0.76, "KZT": 0.13, "RUR": 1,
                       "UAH": 1.64, "USD": 60.66, "UZS": 0.0055}

    def __init__(self, row_dict: dict):
        self.__name = row_dict['name']
        self.__area_name = row_dict['area_name']
        self.__year = int(row_dict['published_at'][:4])
        self.__salary_from = float(row_dict['salary_from'])
        self.__salary_to = float(row_dict['salary_to'])
        self.__salary_curr = row_dict['salary_currency']
        self.__average_salary = (self.__salary_from + self.__salary_to) / 2 * self.currency_to_rub[self.__salary_curr]

    @property
    def name(self):
        return self.__name

    @property
    def area_name(self):
        return self.__area_name

    @property
    def year(self):
        return self.__year

    @property
    def average_salary(self):
        return self.__average_salary
