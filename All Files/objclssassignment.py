# Task-1. You are tasked with creating a Python program to represent
# vehicles using a class. Each car should have attributes for maximum speed and mileage.
class Vehicle:
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage
# Task-2. Update the class with the default color for all vehicles," white".
class Vehicle:
    color = "White"
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage
# Task-3. Additionally, you need to create methods in the Vehicle class to assign
# seating capacity to a vehicle.
class Vehicle:
    color = "White"
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage
    def seating_Capacity(self,seatingCapacity):
        self.seatingCapacity = seatingCapacity
# Task-4. Create a method to display all the properties of an object of the class.
class Vehicle:
    color = "White"
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage
    def seating_Capacity(self,seatingCapacity):
        self.seatingCapacity = seatingCapacity
    def display_properties(self):
        print("Properties of the vehicles")
        print("Color: ",self.color)
        print("Mex Speed: ",self.maxSpeed)
        print("Mileage: ",self.mileage)
        print("Seating Capacity is: ",self.seatingCapacity)
# Task-5. Additionally, you need to create two objects of the Vehicle class object
# that should have a max speed 
# of 200kmph and mileage of 20kmpl with five seating capacities, 
# and another car object should have a max speed of 180kmph and mileage of 25kmpl
# with four seating capacities.
class Vehicle:
    color = "White"
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage
    def seating_Capacity(self,seatingCapacity):
        self.seatingCapacity = seatingCapacity
    def display_properties(self):
        print("Properties of the vehicles")
        print("Color: ",self.color)
        print("Mex Speed: ",self.maxSpeed)
        print("Mileage: ",self.mileage)
        print("Seating Capacity is: ",self.seatingCapacity)
        

Vehicle1 = Vehicle(200, 20)
Vehicle1.seating_Capacity(5)
Vehicle1.display_properties()

Vehicle2 = Vehicle(180, 25)
Vehicle2.seating_Capacity(4)
Vehicle2.display_properties()

