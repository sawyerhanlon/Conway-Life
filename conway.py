"""
conway.py
Author: Sawyer Hanlon
Credit: 
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, Color, Frame

Black = Color(0, 1)
White = Color(0xffffff, 1)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def coordinates(x,y):
    return([[x-10, y-10], [x-10, y], [x-10, y+10], [x, y-10], [x, y+10], [x+10, y-10], [x+10, y], [x+10, y+10]])
    
def

class Cell(Sprite):
    cell = RectangleAsset(10, 10, Black)
    
    def__init__(self, position):
        super().__init__(Cell.cell, position)
        self.x = x
        self.y = y