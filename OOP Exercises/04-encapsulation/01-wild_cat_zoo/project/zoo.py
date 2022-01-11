from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet

class Zoo:
    def __init__(self, name: str, budget: float, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity= workers_capacity
        self.animals = []
        self.workers = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, budget):
        self.__budget = budget

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, animal_capacity):
        self.__animal_capacity = animal_capacity

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, workers_capacity):
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price: float):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget < price:
                return "Not enough budget"
            self.animals.append(animal)
            self.__budget -= price
            animal_type = ""
            if type(animal) is Lion:
                animal_type = "Lion"
            elif type(animal) is Cheetah:
                animal_type = "Cheetah"
            elif type(animal) is Tiger:
                animal_type = "Tiger"
            return f"{animal.name} the {animal_type} added to the zoo"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            worker_type = ""
            if type(worker) is Caretaker:
                worker_type = "Caretaker"
            elif type(worker) is Vet:
                worker_type = "Vet"
            elif type(worker) is Keeper:
                worker_type = "Keeper"
            return f"{worker.name} the {worker_type} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            current_worker = [worker for worker in self.workers if worker.name == worker_name][0]
            self.workers.remove(current_worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_costs = sum([animal.get_needs() for animal in self.animals])
        if self.__budget < total_costs:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_costs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: float):
        self.__budget += amount

    def animals_status(self):
        lion_string = ""
        tiger_string = ""
        cheetah_string = ""
        lion_count = 0
        tiger_count = 0
        cheetah_count = 0
        for animal in self.animals:
            if type(animal) is Lion:
                lion_string += f"\n{animal.__repr__()}"
                lion_count += 1
            elif type(animal) is Tiger:
                tiger_string += f"\n{animal.__repr__()}"
                tiger_count += 1
            elif type(animal) is Cheetah:
                cheetah_string += f"\n{animal.__repr__()}"
                cheetah_count += 1
        return f"You have {len(self.animals)} animals\n" \
               f"----- {lion_count} Lions:" \
               f"{lion_string}\n" \
               f"----- {tiger_count} Tigers:" \
               f"{tiger_string}\n" \
               f"----- {cheetah_count} Cheetahs:" \
               f"{cheetah_string}"

    def workers_status(self):
        keeper_string = ""
        caretaker_string = ""
        vet_string = ""
        keeper_count = 0
        caretaker_count = 0
        vet_count = 0
        for worker in self.workers:
            if type(worker) is Keeper:
                keeper_string += f"\n{worker.__repr__()}"
                keeper_count += 1
            elif type(worker) is Caretaker:
                caretaker_string += f"\n{worker.__repr__()}"
                caretaker_count += 1
            elif type(worker) is Vet:
                vet_string += f"\n{worker.__repr__()}"
                vet_count += 1
        return f"You have {len(self.workers)} workers\n" \
               f"----- {keeper_count} Keepers:" \
               f"{keeper_string}\n" \
               f"----- {caretaker_count} Caretakers:" \
               f"{caretaker_string}\n" \
               f"----- {vet_count} Vets:" \
               f"{vet_string}"

