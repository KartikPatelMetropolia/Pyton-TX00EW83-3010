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

cars = []
for i in range(10):
    car = Car("ABC-"+str(i+1))
    cars.append(car)

win = False
while not win:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            win = True

for i in range(10):
    print(f"Car no.{i + 1}  {cars[i].registration_number} with maximum speed of {cars[i].maximum_speed} and total travel distance of {cars[i].travelled_distance}")