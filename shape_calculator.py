class Rectangle:
    def __init__(self, width: int, height: int):
        self.set_width(width)
        self.set_height(height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return  (self.width*2) + (2*self.height)

    def get_diagonal(self):
        return ((self.width ** 2) + (self.height**2)) ** 0.5


    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        pic = ""
        for i in range(self.height):
            pic += "*"*self.width+"\n"
        return pic

    def get_amount_inside(self, shape):
        return (self.width*self.height)//(shape.width*shape.height)
            # perhaps do the areas or make a for loop where the bigger area shortens each time and rechecks
    # or get the width and height, if one of theres are lesser than the inner object then break

class Square(Rectangle):
    def __init__(self, side: int):
            self.set_side(side)

    def __str__(self):
        return f"Square(side={self.width})"
    def set_side(self, side):
        self.set_width(side)
        self.set_height( side)
