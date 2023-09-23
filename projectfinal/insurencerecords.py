class InsuranceRecords:
    def __init__(self, database):
        self.database = database
        self.id = 0
    def add(self, insured):
        self.id += 1
        id = self.id
        self.database[id] = {
            "name": insured.name,
            "surname": insured.surname,
            "tel": insured.tel,
            "age": insured.age
        }

    def reader(self):
        output = ""
        for index, insured_data in self.database.items():
            name = insured_data['name'].ljust(12)
            surname = insured_data['surname'].ljust(12)
            age = insured_data['age'].ljust(15)
            tel = insured_data['tel']
            output += f"{name}{surname}{age}{tel}\n"
        return output

    def id_finder(self, insured):
        for id, insured_data in self.database.items():
            if insured_data['name'] == insured.name and insured_data['surname'] == insured.surname:
                return f"{self.database[id]['name'].ljust(12)}{self.database[id]['surname'].ljust(12)}{self.database[id]['age'].ljust(15)}{self.database[id]['tel']}"
        return None