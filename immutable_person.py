class ImmutablePerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__setattr__("city", "İstanbul")

    def __setattr__(self, key, value):
        print(key, value)
        if hasattr(self, key):
            raise AttributeError("Özellik değiştirilemez.")
        else:
            super().__setattr__(key, value)

    def __getattribute__(self, item):
        print("getattribute", item)
        if item == "city":
            raise AttributeError("__getattribute__ Özellik değiştirilemez.")
        value = super().__getattribute__(item)
        value = f"({value})"
        return "A"

    def __getattr__(self, item):
        if item == "salary":
            return 10000
        raise AttributeError("__getattr__ Özellik değiştirilemez.")

    def __delattr__(self, item):
        pass

person = ImmutablePerson("Serkan", 30)
print(person.name, person.age)
person.surname = "Bayram"
print(person.name, person.surname, person.age, person.salary)

del person.age

print(person.name, person.surname, person.age, person.salary)
