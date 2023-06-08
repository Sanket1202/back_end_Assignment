class Plane:
    def __init__(self, wings, mode):
        self.wings = wings
        self.mode = mode
    def disp(self):
        print(self.wings, self.mode)
class Jet(Plane):
    def __init__(self, wings, mode, color):
        Plane.__init__(self, wings, mode)
        self.color = color
    def disp(self):
        print("number of wings is:", self.wings)
        print("mode is:", self.mode)
        print("color is:", self.color)
class Passenger(Plane):
    def __init__(self,wings,mode,color):
        Plane.__init__(self,wings,mode)
        self.color = color
    def disp(self):
        print("number of wings is:", self.wings)
        print("mode is:", self.mode)
        print("color is:", self.color)
obj1 = Jet(2, "fly", "black")
obj2 = Jet(2, "fly", "white")
obj1.disp()
obj2.disp()
obj1 = Passenger(2, "fly", "blue")
obj2 = Passenger(2, "fly", "red")
obj1.disp()
obj2.disp()

