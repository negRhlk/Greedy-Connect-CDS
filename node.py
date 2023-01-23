import numpy as np
import random


class node:
    def __init__(self, ID, Xposition=0, Yposition=9):
        self.COLOR = "yellow"
        self.whiteCount = 0
        self.ID = ID
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.component = -10

        self.neighbors = []
