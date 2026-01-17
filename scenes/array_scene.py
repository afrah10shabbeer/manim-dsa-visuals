from manim import *
from components.ArrayStructure import ArrayStructure


class ArrayDemo(Scene):
    def construct(self):
        arr = ArrayStructure(capacity=6)
        self.play(Create(arr))
        self.wait(1)

        arr.set_value(self, 0, 10)
        arr.set_value(self, 1, 20)
        arr.set_value(self, 2, 30)
        arr.set_value(self, 2, 80)

        self.wait(2)
