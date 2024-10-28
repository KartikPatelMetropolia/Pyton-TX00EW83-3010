import random

class Car:
    def __init__(self, reg_no, max_speed):
        self.registration_number = reg_no
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed = self.current_speed + change_of_speed
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed >= self.maximum_speed:
            self.current_speed = self.maximum_speed - 1

    def drive(self, no_of_hours):
        self.travelled_distance = self.travelled_distance + self.current_speed * no_of_hours

class ElectricCar(Car):

    def __init__(self, reg_no, max_speed, battery_capacity):
        super().__init__(reg_no, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):

    def __init__(self, reg_no, speed, tank_capacity):
        super().__init__(reg_no, speed)
        self.tank_capacity = tank_capacity

electriccar = ElectricCar("ABC-15", 180, 52.5)
gasolinecar = GasolineCar("ABC-123", 165, 32.3)

electriccar.current_speed = random.randint(0,100)
gasolinecar.current_speed = random.randint(0,100)

electriccar.drive(3)
gasolinecar.drive(3)

print(f"The electric car has travelled for {electriccar.travelled_distance}")
print(f"The gasoline car has travelled for {gasolinecar.travelled_distance}")