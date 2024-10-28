class Car:
    def __init__(self, reg_no, max_speed):
        self.registration_number = reg_no
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

Car1 = Car("ABC-123", 142)
print(f"The registration number of the object is {Car1.registration_number}")
print(f"The maximum speed of the object is {Car1.maximum_speed}")
print(f"The current speed of the object is {Car1.current_speed}")
print(f"The travelled distance of the object is {Car1.current_speed}")
