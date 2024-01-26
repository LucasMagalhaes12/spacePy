import pygame

class Text:
    def __init__(self, language:dict):
        self.language = language

    
    def names(self, menu:str=None):
        return tuple(self.language[menu].keys())
    

    def positions(self, menu:str=None):
        return tuple(self.language[menu].Values())
    

    def indexofName(self, menu:str=None, name:str=None):
        return self.language[menu].index(name)
    

    def length(self, menu:str=None, name:str=None):
        return len(self.language[menu])