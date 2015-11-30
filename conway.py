"""
conway.py
Author: Sawyer Hanlon
Credit: 
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Cell(Sprite):
    cell = RectangleAsset(10, 10, 