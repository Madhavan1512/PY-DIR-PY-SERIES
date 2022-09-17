

class Vehicle :
    def general_usage(self):   
        print("General usage: Transportation")
        
        
class Car(Vehicle):
    def __init__(self) :
        print("I'm a car")
        self.wheels = 4
        self.has_roof = True
    def specific_usage(self) :
        print("Specific usage: commute to work , vacation with family")
class MotorCycle(Vehicle):
    def __init__(self) :
        print("I'm a motor cycle")
        self.wheels = 2
        self.has_roof = False
    def specific_usage(self) :
        print("Specific usage: road trip , racing")
        
c = Car()
c.general_usage()
c.specific_usage()

m = MotorCycle()
m.general_usage()
m.specific_usage()