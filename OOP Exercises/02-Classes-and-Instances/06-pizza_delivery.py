class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += quantity * ingredient_price

        else:
            self.ingredients[ingredient] = quantity
            self.price += quantity * ingredient_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * ingredient_price

    def pizza_ordered(self):
        self.ordered = True
        ingredients_quantity = ""
        count = 0
        for key, value in self.ingredients.items():
            count += 1
            if count == len(self.ingredients):
                ingredients_quantity += f"{key}: {value}"
                continue
            ingredients_quantity += f"{key}: {value}, "

        return f"You've ordered pizza {self.name} prepared " \
               f"with {ingredients_quantity} and the price will be {self.price}lv."