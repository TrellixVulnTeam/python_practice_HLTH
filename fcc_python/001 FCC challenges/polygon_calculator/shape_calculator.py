class Rectangle:
    def __init__(self, width , height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height>50:   return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture +=self.width*"*" + "\n"
        return picture

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_amount_inside(self, in_shape):
        out_shape = self.get_area()
        return out_shape//in_shape.get_area()

class Square(Rectangle):
    def __init__(self, side) -> None:
        self.width = side
        self.height = side
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side
    
    def set_height(self, side):
        self.width = side
        self.height = side

    def __str__(self) -> str:
        return f"Square(side={self.height})"



rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
 
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
 
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))