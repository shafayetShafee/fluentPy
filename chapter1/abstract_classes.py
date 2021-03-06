from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
# without these two abstrac method `go` and `stop`, the class Vehicle
# would not be an abstract class and we could have instantiate the
# Vehicle class. That is, an abstract class must have at least an
# abstract method to be an abstract class.

class Car(Vehicle):
    
    def go(self):
        print("You drive the car")
    
    def stop(self):
        print("This car is stopped")
        

class Motorcycle(Vehicle):
    
    def go(self):
        print("You drive the motorcycle")
    
    def stop(self):
        print("This motorcycle is stopped")

# Car class and Motorcycle is derived from, i.e. is a child class from
# the abstract class vehicle. So these classes must have implementations
# of the abstract methods (go, stop) of their parent abstract class.
# and it must happen.

# vehicle = Vehicle()
# since Vehicle is an abstract class. We can't instantiate this.

car = Car()
motor = Motorcycle()

car.go()
motor.go()