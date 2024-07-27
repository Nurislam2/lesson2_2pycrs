import math as m


class Figure:
    unit="cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self,side_length):
        super().__init__()
        self.__side_length=side_length

    def calculate_area(self):
        S=m.pow(self.__side_length,2)
        return S

    def calculate_perimeter(self):
        P=4*self.__side_length
        return P

    def info(self):
        print(f"Square side length: {self.__side_length}{Square.unit}, area: {self.calculate_area()}{Square.unit}")

class Rectangle(Figure):

    def __init__(self,length,width):
        super().__init__()
        self.__length=length
        self.__width=width

    def calculate_area(self):
        S=self.__length*self.__width
        return S

    def info(self):
        print(f"Rectangle length: {self.__length}{Rectangle.unit},width: {self.__width}{Rectangle.unit}, area: {self.calculate_area()}{Rectangle.unit}")



sqr1=Square(5)
sqr2=Square(9)
rect1=Rectangle(1,4)
rect2=Rectangle(3,2)
rect3=Rectangle(2,8)
figure=[sqr1,sqr2,rect1,rect2,rect3]
for i in range(0,len(figure)):
    figure[i].info()