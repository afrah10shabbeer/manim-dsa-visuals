from manim import *
from components.StackStructure import StackStructure


class StackDemo(Scene):
    def construct(self):
        # Create stack instance
        stack = StackStructure(capacity=5).shift(UP * 0.2)

        # Show stack container
        self.play(Create(stack))
        self.wait(1)

        # Push elements
        stack.push(self, 12)
        stack.push(self, 1)
        stack.push(self, 0)

        self.wait(1)

        # Pop top element
        stack.pop(self)
        self.wait(1)

        # Push another element
        stack.push(self, 99)

        self.wait(2)
