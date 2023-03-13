import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks,tasks_file = "taski.json"):
        # TODO zapisz taski do pliku tutaj
        file = open(tasks_file, "w")
        json.dump(tasks, file, indent=1)
        file.close()
        pass
