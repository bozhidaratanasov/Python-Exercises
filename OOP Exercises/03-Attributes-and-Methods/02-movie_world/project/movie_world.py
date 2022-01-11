from project.customer import Customer
from project.dvd import DVD

class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < 10:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < 15:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        c_id = [index for index in range(len(self.customers)) if self.customers[index].id == customer_id][0]
        d_id = [index for index in range(len(self.dvds)) if self.dvds[index].id == dvd_id][0]
        current_customer = self.customers[c_id]
        current_dvd = self.dvds[d_id]
        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"
        if current_dvd.is_rented:
            return "DVD is already rented"
        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"
        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        c_id = [index for index in range(len(self.customers)) if self.customers[index].id == customer_id][0]
        d_id = [index for index in range(len(self.dvds)) if self.dvds[index].id == dvd_id][0]
        current_customer = self.customers[c_id]
        current_dvd = self.dvds[d_id]
        if current_dvd not in current_customer.rented_dvds:
            return f"{current_customer.name} does not have that DVD"
        current_customer.rented_dvds.remove(current_dvd)
        current_dvd.is_rented = False
        return f"{current_customer.name} has successfully returned {current_dvd.name}"

    def __repr__(self):
        customer_rep = '\n'.join(customer.__repr__() for customer in self.customers)
        dvd_rep = '\n'.join([dvd.__repr__() for dvd in self.dvds])
        return f"{customer_rep}\n{dvd_rep}"


