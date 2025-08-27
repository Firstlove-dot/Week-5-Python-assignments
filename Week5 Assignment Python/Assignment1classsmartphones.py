class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


class Smartphone(Device):
    def __init__(self, brand, model, battery, storage):
        super().__init__(brand, model)
        self.__battery = battery   # private attribute
        self.storage = storage

    def make_call(self, number):
        return f"Calling {number} from {self.device_info()}..."

    def get_battery(self):
        return f"Battery level: {self.__battery}%"

    def charge(self, amount):
        if amount > 0:
            self.__battery = min(100, self.__battery + amount)
        return f"Charged! {self.get_battery()}"


class SuperSmartphone(Smartphone):
    def charge(self, amount):
        fast_charge = amount * 2
        return super().charge(fast_charge)


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", 50, "256GB")
phone2 = SuperSmartphone("Apple", "iPhone 15 Pro", 20, "512GB")

# Use methods
print(phone1.device_info())
print(phone1.make_call("123-456-789"))
print(phone1.get_battery())
print(phone1.charge(30))  # Normal charging

print("\n--- Super Smartphone ---")
print(phone2.device_info())
print(phone2.make_call("987-654-321"))
print(phone2.get_battery())
print(phone2.charge(20))  # Faster charging
