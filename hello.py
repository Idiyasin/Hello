class Flight():
    def __init__(self, capacity):
        self.capacity= capacity
        self.passengers = []
    
    def add_passenger(self, name):
        self.passengers.append(name)
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
