
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

elevator = Elevator(0, 6)
elevator.go_to_floor(5)
print(f"{elevator.current_floor}")
elevator.go_to_floor(0)
print(f"{elevator.current_floor}")
