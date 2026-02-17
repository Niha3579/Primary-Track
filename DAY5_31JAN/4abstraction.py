#ABSTRACT METHODS:

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car Engine Started")

c=Car()
c.start_engine()

