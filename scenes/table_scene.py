from manim import *  # Import all Manim classes
from components.TableStructure import (
    TableStructure,
)  # Import the new class-based table


# ---------------- Table Demo ---------------- #
class TableDemo(Scene):
    def construct(self):
        # ----------------------------
        # Define labels for rows and columns
        # ----------------------------
        row_labels = ["A", "B", "C", "D"]  # 4 rows
        col_labels = ["1", "2", "3", "4", "5"]  # 5 columns

        # ----------------------------
        # Create the table using the class-based TableStructure
        # ----------------------------
        table = TableStructure(
            rows=4,
            cols=5,
            cell_width=0.9,
            cell_height=0.9,
            cell_stroke_width=2,
            row_labels=row_labels,
            col_labels=col_labels,
            title_text="Adjacency Table",
            position_shift=ORIGIN,
        )

        # ----------------------------
        # Center table in scene (optional)
        # ----------------------------
        table.move_to(ORIGIN)

        # ----------------------------
        # Animate the table
        # ----------------------------
        self.play(Create(table))
        self.wait(2)
