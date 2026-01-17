from manim import *
from components.QueueStructure import (
    QueueStructure,
)  # Assuming your Queue class is in components/queue.py


class QueueDemo(Scene):
    def construct(self):
        # Create the queue
        queue = QueueStructure()
        queue.move_to(UP * 2)  # Center the queue
        self.add(queue.queue_structure)  # Add just the structure first

        # ---------------- Enqueue elements ---------------- #
        queue.push("10", self)  # Push element 10
        queue.push("20", self)  # Push element 20
        queue.push("30", self)  # Push element 30

        self.wait(1)

        # ---------------- Dequeue elements ---------------- #
        queue.pop(self)  # Remove front element (10)
        queue.pop(self)  # Remove front element (20)

        self.wait(1)

        # ---------------- Enqueue another element ---------------- #
        queue.push("99", self)

        self.wait(2)
