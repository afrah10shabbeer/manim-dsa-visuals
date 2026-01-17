from manim import *


# ---------------- Stack Cell ---------------- #
# Represents a single element in the stack (value + box)
class StackCell(VGroup):
    def __init__(self, value, **kwargs):
        # Initialize VGroup internals (required for Manim grouping)
        super().__init__(**kwargs)

        # Rectangle representing the stack cell container
        box = Rectangle(
            height=0.52,
            width=1.1,
            fill_color=BLUE_D,
            fill_opacity=1,
            stroke_color=BLACK,
        )

        # Text label to display the stored value
        label = Text(str(value), font_size=26, color=BLACK)

        # Center the text inside the rectangle
        label.move_to(box.get_center())

        # Group rectangle and text together
        self.add(box, label)


# ---------------- Stack Structure ---------------- #
# Visual representation of a stack data structure
class StackStructure(VGroup):
    def __init__(self, capacity=5, **kwargs):
        # Initialize parent VGroup
        super().__init__(**kwargs)

        # Maximum number of elements allowed in the stack
        self.capacity = capacity

        # Internal list to track stack elements (LIFO order)
        self.items = []

        # Build the visual container for the stack
        self._create_container()

    # Creates the open-top stack container (bucket)
    def _create_container(self):
        # Container dimensions based on stack capacity
        width = 1.25
        height = self.capacity * 0.7

        # Semi-transparent filled background of the stack
        fill_area = Rectangle(
            width=width,
            height=height,
            fill_color=LIGHT_GRAY,
            fill_opacity=0.18,
            stroke_width=0,
        ).shift(UP * height / 2)

        # Outline to give the stack an open-top bucket look
        frame = VGroup(
            Line(LEFT * width / 2, RIGHT * width / 2),  # bottom edge
            Line(LEFT * width / 2, LEFT * width / 2 + UP * height),  # left wall
            Line(RIGHT * width / 2, RIGHT * width / 2 + UP * height),  # right wall
        ).set_stroke(GRAY)

        self.add(Text("Stack", font_size=30).shift(DOWN * 2.5))
        # Combine fill and outline, then position on screen
        self.container = VGroup(fill_area, frame).shift(DOWN * 2.2)

        # Add container to the stack group
        self.add(self.container)

    # ---------------- Stack Operations ---------------- #

    # Push a new value onto the stack
    def push(self, scene, value, run_time=0.9):
        # Handle stack overflow
        if len(self.items) == self.capacity:
            scene.play(Indicate(self.container, color=RED))
            return

        # Create a new stack cell
        cell = StackCell(value)

        # Start animation above the container
        cell.next_to(self.container, UP)

        # Animate appearance of the cell
        scene.play(FadeIn(cell, shift=DOWN))

        # Determine final position based on current stack height
        if self.items:
            # Place on top of the previous element
            destination = self.items[-1].get_top() + UP * 0.3
        else:
            # Place at the bottom of the container
            destination = self.container[0].get_bottom() + UP * 0.32

        # Animate cell moving into position
        scene.play(cell.animate.move_to(destination), run_time=run_time)

        # Update internal stack state
        self.items.append(cell)
        self.add(cell)

    # Pop the top value from the stack
    def pop(self, scene):
        # Handle stack underflow
        if not self.items:
            scene.play(Indicate(self.container, color=RED))
            return

        # Remove top element (LIFO)
        top_block = self.items.pop()
        self.remove(top_block)

        # Animate removal of the element
        scene.play(top_block.animate.shift(UP * 2.5))
        scene.play(FadeOut(top_block))
