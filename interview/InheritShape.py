#inheritance shape
class shape():
    def values(self):
        print("shape is the base class")
        self.PI=3.14
        self.r=5.0
        self.l=10
        self.b=15
class circle(shape):
    def area(self):
        area=self.PI*self.r*self.r
        print("area of circle is",area)
class rectangle(shape):
    def area(self):
        area=self.l*self.b
        print("area of rectangle is,area",area)
shapes=circle()
shapes.values()
shapes.area()
shape1=rectangle()
shape1.values()
shape1.area()
