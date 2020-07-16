from datetime import date


class Building:
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = date.today()

    def purchase(self, buyer_name):
        self.owner = buyer_name


building_one = Building("5 Pennies Ln", 5)
building_one.construct()
building_one.purchase("Mighty Man")
print(f"{building_one.address} was purhcased by {building_one.owner} on {building_one.date_constructed} and has {building_one.stories} stories.")


building_two = Building("3 Yard St", 3)
building_two.construct()
building_two.purchase("Mighty Man")
print(f"{building_two.address} was purhcased by {building_two.owner} on {building_two.date_constructed} and has {building_two.stories} stories.")


building_three = Building("0 Candy Ave", 10)
building_three.construct()
building_three.purchase("Mighty Man")
print(f"{building_three.address} was purhcased by {building_three.owner} on {building_three.date_constructed} and has {building_three.stories} stories.")


building_four = Building("6 Lap Blvd", 20)
building_four.construct()
building_four.purchase("Mighty Man")
print(f"{building_four.address} was purhcased by {building_four.owner} on {building_four.date_constructed} and has {building_four.stories} stories.")


building_five = Building("9 Freed Way", 9)
building_five.construct()
building_five.purchase("Mighty Man")
print(f"{building_five.address} was purhcased by {building_five.owner} on {building_five.date_constructed} and has {building_five.stories} stories.")
