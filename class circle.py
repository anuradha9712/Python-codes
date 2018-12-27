class circle:
    def __init__(self,r,X,Y):
        self.radius=r
        self.x=X
        self.y=Y

    def area(self):
        a= 3.14* self.radius * self.radius
        return a

    def circumference(self):
        c=2*3.14*self.radius
        return c

c1=circle(6,2,3)
print("area of the circle:",c1.area(),"\n","circumference of circle:",c1.circumference())

        

    
