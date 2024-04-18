class Cars:
    def __init__ (self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

    def get_name(self):
        return self.name

    def get_multiplied_mileage(self):
        return self.mileage * 10

car1 = Cars("honda", 120, 25)
print(car1.get_name())
print(car1.get_multiplied_mileage())