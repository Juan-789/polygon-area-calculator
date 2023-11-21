class Rectangle:
    def __innit__(self, width, height):
        self.width = width
        self.height = height


    def set_width(self):
        pass


    def set_height(self):
        pass

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return  (self.width*2) + (2*self.height)

    def get_diagonal(self):
        return (self.width ** 2) + (2 ** self.height) ** 5


    def get_picture(self) -> str:
        if self.width>50 or self.height>50:
            return "Too big for picture."
        pic = ""
        pic += "*" * self.width + "\n"
        for i in range(self.height-2):
            pic+= "*"+(self.width-2)*" "+"*"+"\n"
        pic +=  "*" * self.width
        return pic

    def get_amount_inside(self):
        pass    # perhaps do the areas or make a for loop where the bigger area shortens each time and rechecks
    # or get the width and height, if one of theres are lesser than the inner object then break

class Square(Rectangle):
    def __int__(self):
        super.__init__(self)
        pass
    def set_side(self):
        pass