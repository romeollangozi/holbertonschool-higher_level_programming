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

    def __str__(self):
        return f"[{self.__class__.__name__} ({self.id}) {self.x}/{self.y}]\
 - {self.width}"
