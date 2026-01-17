from manim import *


class QueueStructure(Mobject):
    def __init__(self, element_width=0.8, fill_opacity=0.5, fill_color=GRAY, **kwargs):
        super().__init__(**kwargs)
        self.element_width = element_width
        self.elements = []

        # Create the queue structure with lines and fill area
        self.top_line = Line(start=LEFT * 2.7, end=RIGHT * 2.7, stroke_color=BLACK)
        self.bottom_line = Line(start=LEFT * 2.7, end=RIGHT * 2.7, stroke_color=BLACK)
        self.fill_area = Rectangle(
            width=5.4,
            height=0.8,
            fill_opacity=fill_opacity,
            fill_color=fill_color,
            stroke_width=0,
        )

        self.queue_structure = VGroup(self.top_line, self.fill_area, self.bottom_line)
        self.queue_structure.arrange(DOWN, buff=0)
        self.queue_structure.shift(DOWN)

    def create_element(self, text):
        square = Square(
            side_length=self.element_width,
            fill_opacity=1,
            fill_color=YELLOW,
            color=BLACK,
        ).scale(0.8)
        text = Text(text, font_size=44, color=BLACK).scale(0.8)
        return VGroup(square, text)

    def push(self, text, scene):
        element = self.create_element(text)
        element.next_to(self.queue_structure, RIGHT, buff=0.4)

        # Animate the new element into the queue
        scene.play(Create(element))
        if self.elements:
            # Shift all existing elements to the left
            shift_amount = self.element_width
            animations = [e.animate.shift(LEFT * shift_amount) for e in self.elements]
            scene.play(*animations)

        scene.play(
            element.animate.move_to(self.queue_structure.get_right() + LEFT * 0.4)
        )
        self.elements.append(element)
        scene.wait(0.2)

    def pop(self, scene):
        if self.elements:
            element = self.elements.pop(0)
            scene.play(
                element.animate.next_to(self.fill_area.get_left() + LEFT * 1.34),
                run_time=2,
            )
            scene.play(FadeOut(element), run_time=0.8)
            scene.wait(0.2)
            return element
        else:
            print("Queue is empty, cannot pop")
