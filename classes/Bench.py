class Bench():
    def __init__(self, list=[]):
        self.list = list

    def add_to_bench(self, benched_pokemon):
        self.list.append(benched_pokemon)

    def get_list(self):
        return self.list