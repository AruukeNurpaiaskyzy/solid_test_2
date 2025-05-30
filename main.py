class Figure:
    def get_arena(self):
        return 0
    
class  Square(Shape):
    def __init__(self, side):
        self.side = side

        def get_area(self):
            return self.side **2
        
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height

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


# Solid- I
class OpenDocument:
    def open_document(self):
        pass
class SaveDocument:
    def save_document(self):
        pass
class CloseDocument:
    def close_document(self):


class FirstDocumentEditor(OpenDocument, CloseDocument):
     def open_document(self):
      def close_document(self):
class SecondDocumnetEditor:
    def save_document(self):
    def close_document(self):


