import csv
from statistic import Statistic


class DataSet:
    def __init__(self, file_name: str, selected_vacancy: str):
        file = open(file_name, 'r', encoding='utf-8-sig')
        self.data = csv.reader(file, delimiter=',')
        self.titles = next(self.data)
        self.glue_row_dictionaries()
        self.statistic = Statistic(selected_vacancy)
        self.statistic.enter_static_data(self.data)

    def glue_row_dictionaries(self):
        self.data = filter(lambda row: len(row) == len(self.titles) and "" not in row, self.data)
        self.data = (dict(zip(self.titles, row)) for row in self.data)
