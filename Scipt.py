import sys

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine_started = False  # Track engine state
    
    def start_engine(self, prompt):
        start = input(prompt).strip().lower()

        if start == "yes" and self.year >= 2000:
            self.engine_started = True
            print("The car has started successfully!")
        elif start == "no":
            print("You are just sitting in your car...")
        else:
            print("The car has stalled due to an unknown issue.")

        return self.engine_started

    def stop_engine(self, prompt):
        if not self.engine_started:
            print("The engine is already off.")
            return False

        stop = input(prompt).strip().lower()
        if stop == "yes":
            self.engine_started = False
            print("The engine has stopped successfully!")
            return True
        else:
            print("The engine is still running.")
            return False

    def drive(self):
        if not self.engine_started:
            print("You can't drive. The engine is off!")
            return
        print(f"The road looks great! You are now driving your {self.make} {self.model}.")
        
# Create a Car object
car = Car("Hyundai", "Sedan", 2024)

def main():
    # Start the car
    if not car.start_engine("Would you like to start your car? (yes/no): "):
        print("Exiting program. Goodbye!")
        return

    # While engine is on, allow driving
    while car.engine_started:
        opt2 = input("Would you like to drive the car? (yes/no): ").strip().lower()

        if opt2 == "yes":
            car.drive()

            # Ask if the user wants to stop the engine
            if car.stop_engine("Would you like to stop the engine? (yes/no): "):
                print("Goodbye! Drive safely next time.")
                break
        elif opt2 == "no":
            print("You are enjoying the comfortable hum of the engine.")
        else:
            print("Invalid option. Please answer 'yes' or 'no'.")

if __name__ == "__main__":
    main()
