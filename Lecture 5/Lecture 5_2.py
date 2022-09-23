class Cylinder:
    pi = 22/7    
    def __init__(self, r, h):
        
        # Assign to self object
        self.r = r
        self.h = h

    def cal_volume(self):
        return Cylinder.pi*(self.r**2)*self.h

    def cal_area(self):
        return 2*Cylinder.pi*self.r*self.h      # Calculate only the curved surface area

class Barrel(Cylinder):
    def __init__(self, r, h):
        super().__init__(r,h)

    def cal_area(self):
        return 2*Cylinder.pi*self.r*self.h + 2*super(Barrel,self).pi*(self.r**2)

Barrel1 = Barrel(7, 10)

print(Barrel1.cal_volume())
print(Barrel1.cal_area())