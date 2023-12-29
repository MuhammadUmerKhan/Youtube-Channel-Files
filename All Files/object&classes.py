class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce_self(self):
        print("My name is " +  self.name)
        print("My color is " +  self.color)
        print("My weight is " +  self.weight)
        
# r1 = Robot()
# r1.name = "Tom"
# r1.color = "Blue"
# r1.wight = 30

# r2 = Robot()
# r2.name = "Jerry"
# r2.color="Brown"
# r2.weight = 3


r1 = Robot("Tom","Blue","30")
r2 = Robot("Jerry", "Brown","3")
r3 = Robot("Umer","Medium","50")
r1.introduce_self()
r2.introduce_self()
r3.introduce_self()
