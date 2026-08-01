from abc import ABC, abstractmethod

# Product Interface
class Vehicle(ABC):
    @abstractmethod
    def getType(self):
        pass


# Concrete Products
class Car(Vehicle):
    def getType(self):
        return "Car"


class Truck(Vehicle):
    def getType(self):
        return "Truck"


class Bike(Vehicle):
    def getType(self):
        return "Bike"


# Factory Interface
class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self):
        pass


# Concrete Factories
class CarFactory(VehicleFactory):
    def createVehicle(self):
        return Car()


class TruckFactory(VehicleFactory):
    def createVehicle(self):
        return Truck()


class BikeFactory(VehicleFactory):
    def createVehicle(self):
        return Bike()