class Square:
    #Constructor to create a square given a side
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2
    
    def perimeter(self):
        return 4 * self.side
    
    #ToString 
    def __repr__(self):
        sqr = 'Square with side = ' + str(self.side) + '\n' + \
        'Area = ' + str(self.area()) + '\n' + \
        'Perimeter = ' + str(self.perimeter())
        return sqr
    
if __name__ == '__main__':
    side = int(input('Enter a side length to create a Square: '))
    square = Square(side)
    print(square)