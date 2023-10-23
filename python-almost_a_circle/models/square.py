#!/usr/bin/python3
'''
Module for demostrattive purposes
'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Class for Square objects
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        Function to update the instance attributes
        '''

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

        for i, value in enumerate(args):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.size = args[i]
            if i == 2:
                self.x = args[i]
            if i == 3:
                self.y = args[i]

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}\
 - {self.width}"

    def to_dictionary(self):
        '''
        Function that returns representation
        of an object as a dictionary
        '''

        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
