import sys

class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seats(self):
      return self.capacity - len(self.passengers)

    def add_passenger(self,name):
       if self.open_seats() > 0:
          self.passengers.append(name)
          return True

flight = Flight(3)
    
people = ["Ray","Wyatt","Jones","Angela","Aaron"]

for person in people:
    success = flight.add_passenger(person)

    if success:
        print(f'Added {person} to flight successfully!')
    else:
      print(f'No available seats for {person}')