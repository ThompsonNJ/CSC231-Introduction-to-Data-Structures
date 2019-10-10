class RegularPolygon:
    def __init__(self, num, length):
        self.num_sides = num
        self.length = length

    def compute_perimeter(self):
        return (self.num_sides*self.length)

class EqualiaterialTriangle(RegularPolygon):
    def compute_area(self):
        return (3**(1/2.0) * self.length)

class Square(RegularPolygon):
    def compute_area(self):
        return self.length**2

poly_list = []

with open('polygons.csv', 'r') as rfile:
    line = rfile.readline().strip()
    for s in line:
        line = s.split(',')
        if line[0] == '3':
            
            
