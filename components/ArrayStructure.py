from manim import *


# ---------------------- Array Cell ----------------------
class ArrayCell(VGroup):
    """
    This class represents a single cell of an array,
    containing a colored rectangle and a value inside it.
    """

    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)

        # Create the rectangle for the cell
        box = Rectangle(
            height=1,  # height of the cell
            width=1,  # width of the cell
            fill_color=GREEN,  # background color
            fill_opacity=1,  # fully opaque
            stroke_color=GRAY,  # border color
        )

        # Create the text label for the value
        label = Text(str(value), font_size=26, color=BLACK)
        # Center the label inside the rectangle
        label.move_to(box.get_center())

        # Add both the rectangle and the label to the cell group
        self.add(box, label)


# ---------------------- Array Structure ----------------------
class ArrayStructure(VGroup):
    """
    This class represents an entire array visualization.
    It includes:
      - a background rectangle
      - individual empty slots for array elements
      - index labels below each slot
      - a title at the top
    """

    def __init__(self, capacity=5, **kwargs):
        super().__init__(**kwargs)

        self.capacity = capacity  # number of slots in the array
        self.items = []  # stores the actual ArrayCell objects

        # Build the visual structure of the array
        self._build_array_frame()

    def _build_array_frame(self):
        """
        Internal method to create the array frame:
          - creates empty slots (Rectangles)
          - adds index labels
          - adds background and title
        """
        cell_size = 1  # size of each cell
        spacing = 0.1  # space between cells
        padding = 0.15  # extra padding around the array

        self.cells = VGroup()  # group to hold all the slots
        self.index_labels = VGroup()  # group to hold all the indices

        # -------- Create slots --------
        for i in range(self.capacity):
            # Create rectangle for the slot (empty cell)
            slot = Rectangle(
                height=cell_size,
                width=cell_size,
                stroke_color=GRAY,
                stroke_width=2,
            )

            # Position the slot horizontally with spacing
            slot.move_to(RIGHT * i * (cell_size + spacing))
            self.cells.add(slot)

            # Create index text below the slot
            index_text = Text(str(i), font_size=22, color=GRAY)
            index_text.next_to(slot, DOWN, buff=0.2)
            self.index_labels.add(index_text)

        # Center all cells around the origin
        self.cells.move_to(ORIGIN)

        # -------- Background ONLY for cells --------
        total_width = (
            self.capacity * cell_size + (self.capacity - 1) * spacing + padding * 2
        )
        total_height = cell_size + padding * 2

        # Background rectangle behind the slots
        background = Rectangle(
            width=total_width,
            height=total_height,
            fill_color=LIGHT_GRAY,
            fill_opacity=0.18,
            stroke_color=GRAY,
        )

        # Ensure background is behind all other elements
        background.z_index = -1
        background.move_to(self.cells.get_center())

        # Title at the top
        title = Text("Array", font_size=30).shift(UP * 1)
        self.add(title)

        # Move indices slightly below the background rectangle
        self.index_labels.next_to(background, DOWN, buff=0.15)

        # Group everything together
        self.container = VGroup(background, self.cells, self.index_labels)
        # Add to the main VGroup
        self.add(self.container)

    def set_value(self, scene, index, value):
        """
        Set a value at a specific index in the array.
        If the index is invalid, highlight the container in red.
        Otherwise, fade in a new ArrayCell at the index position.
        """
        if index < 0 or index >= self.capacity:
            # Invalid index: indicate error by flashing the array container
            scene.play(Indicate(self.container, color=RED))
            return

        # Create a new ArrayCell for the value
        cell = ArrayCell(value)
        # Position it exactly over the target slot
        cell.move_to(self.cells[index].get_center())

        # Animate the appearance of the new cell
        scene.play(FadeIn(cell))
        # Keep track of added items
        self.items.append(cell)
        # Add the cell to the VGroup (for proper rendering)
        self.add(cell)
