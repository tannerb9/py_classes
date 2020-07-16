class Pizza:
    def __init__(self):
        self.size = ""
        self.style = ""
        self.toppings = []

    def add_topping(self, *toppings):
        for topping in toppings:
            self.toppings.append(topping)

    def print_order(self):
        print(
            f"I would like a {self.size}-inch, {self.style} pizza with {self.toppings}.")


meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "deep-dish"
meat_lovers.add_topping("pepperoni", "olives")
meat_lovers.print_order()
