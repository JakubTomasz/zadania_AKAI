import json


class Importer:

    def __init__(self):
        self.tasks = []
        pass

    def read_tasks(self,tasks_file = "taski.json"):
        # TODO odczytaj plik i zdekoduj treść tutaj
        ratios = open(tasks_file, "r")
        self.tasks = json.load(ratios)
        pass

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.tasks
        pass