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
        self.travelled_distance = self.current_speed * no_of_hours

car1 = Car("ABC-123", 142)
print(f"The registration number of the object is {car1.registration_number}")
print(f"The maximum speed of the object is {car1.maximum_speed}")
print(f"The current speed of the object is {car1.current_speed}")
print(f"The travelled distance of the object is {car1.current_speed}")
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f"The current speed of the car is {car1.current_speed}")
car1.accelerate(-200)
print(f"Speed after applying a emergency brake {car1.current_speed}")