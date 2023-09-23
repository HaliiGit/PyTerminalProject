class Insured:
    def __init__(self, name: str, surname: str, tel: str, age: int):
        self.name = name
        self.surname = surname
        self.tel = tel
        self.age = age
    def __str__(self):
        return f"{self.name.ljust(6)}{self.surname.ljust(12)}{self.age.ljust(15)}{self.tel}"