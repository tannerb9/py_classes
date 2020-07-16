class Employee:

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date


class Company:

    def __init__(self, name, address, industry):
        self.name = name
        self.address = address
        self.industry = industry
        self.employees = []


smile_club = Company("Smile Club", "123 My Way", "dental")
rayban = Company("Rayban", "456 Ventura Blvd", "eyewear")

josh = Employee("Josh Prose", "Janitor", "03/04/2020")
shelly = Employee("Shelly Epper", "Dentist", "03/04/2020")
kyle = Employee("Kyle Blerg", "Photographer", "03/04/2020")
rebecca = Employee("Rebecca Zerf", "Manager", "03/04/2020")
ty = Employee("Ty Rone", "Assistant", "03/04/2020")


smile_club.employees.append(shelly)
smile_club.employees.append(ty)
rayban.employees.append(josh)
rayban.employees.append(kyle)
rayban.employees.append(rebecca)

print(f"{smile_club.name} is in the {smile_club.industry} industry and has the following employees:")
for employee in smile_club.employees:
    print(f"    * {employee.name}")

print(f"{rayban.name} is in the {rayban.industry} industry and has the following employees:")
for employee in rayban.employees:
    print(f"    * {employee.name}")
