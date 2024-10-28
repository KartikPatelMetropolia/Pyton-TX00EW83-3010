import random

class Car:

    def __init__(self, reg_no):
        self.registration_number = reg_no
        self.maximum_speed = random.randint(100, 200)
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

class Race:

    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hours_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        i = 0
        for car in self.cars:
            print(f"Car no.{i + 1}  {car.registration_number} with maximum speed of {car.maximum_speed} and total travel distance of {car.travelled_distance}")
            i += 1

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance > self.distance:
                return True
        return False

cars = []
for i in range(10):
    car = Car("ABC-" + str(i + 1))
    cars.append(car)

race = Race("Grand Demolition Derby", 10000, cars)

win = False
i = 1
while not win:
    race.hours_passes()
    if race.race_finished():
        win = True
    if i % 10 == 0:
        race.print_status()
    i += 1

print("Race has finished")
race.print_status()