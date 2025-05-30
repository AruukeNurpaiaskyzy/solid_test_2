# class Figure:
#     def get_arena(self):
#         return 0
    
# class  Square(Shape):
#     def __init__(self, side):
#         self.side = side

#         def get_area(self):
#             return self.side **2
        
# class Rectangle(Figure):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def get_area(self):
#         return self.width * self.height

from abc import ABC, abstractmethod
class Figure (ABC):
    def get_area (self):
        pass
class Square(Figure):
    def __init__ (self, side):
        self.side = side
    def area (self):
        return self.side **2
    
class Rectangle(Figure):
    def __init__(self, width, height):
        self. width = width
        self.height = height
    def get_area(self):
        return self. width * self.height