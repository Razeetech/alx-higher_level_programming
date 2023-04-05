#!/usr/bin/python3
'''Class that restricts atttribute assignment'''

class LockedClass:
    '''simple class that only allows assigning attributes names first_name'''

    __slots__ = ('first_name')
    '''The attribute that limits other attribute creatioin pythonn'''
