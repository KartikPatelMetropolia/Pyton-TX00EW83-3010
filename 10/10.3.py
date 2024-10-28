class Building:
    def __init__(self, bottom_floor, top_floor, no_of_elevators):
        self.elevators = []
        for i in range(no_of_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_num, destination_floor):
        self.elevators[elevator_num - 1].go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(0)

class Elevator:
    def __init__(self, bottom_floor, highest_floor):
        self.bottom_floor = bottom_floor
        self.highest_floor = highest_floor
        self.current_floor = self.bottom_floor

    def floor_up(self):
        self.current_floor += 1
        if self.current_floor > self.highest_floor:
            self.current_floor = self.highest_floor

    def floor_down(self):
        self.current_floor -= 1
        if self.current_floor < self.bottom_floor:
            self.current_floor = self.bottom_floor

    def go_to_floor(self, destination_floor):
        if self.current_floor > destination_floor:
            while not self.current_floor == destination_floor:
                self.floor_down()
        else:
            while not self.current_floor == destination_floor:
                self.floor_up()

building = Building(0,5,2)
building.run_elevator(2, 5)
print(f"The elevator is currently at {building.elevators[1].current_floor}")
building.run_elevator(2, 0)
print(f"The elevator is currently at {building.elevators[1].current_floor}")
building.fire_alarm()
print("The fire alarm is rang!!!!!!!!!!")
for i in range(2):
    print(f"The elevator no {i} is at {building.elevators[i].current_floor} floor")