from manim import *  # Import all classes and functions from Manim


# ---------------- Table Skeleton ---------------- #
class TableStructure(VGroup):
    def __init__(
        self,
        rows=3,
        cols=3,
        cell_width=1.0,
        cell_height=0.8,
        cell_stroke_width=2,
        row_labels=None,
        col_labels=None,
        title_text="Table",
        position_shift=ORIGIN,
        **kwargs
    ):
        """
        rows, cols: number of rows and columns
        cell_width, cell_height: size of each cell
        cell_stroke_width: border thickness of cells
        row_labels, col_labels: list of strings for row/column labels
        title_text: title above table
        position_shift: 3D vector to shift table position
        """
        super().__init__(**kwargs)

        # ---------------- Class Variables ---------------- #
        self.rows = rows
        self.cols = cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cell_stroke_width = cell_stroke_width
        self.row_labels = row_labels or ["" for _ in range(rows)]
        self.col_labels = col_labels or ["" for _ in range(cols)]
        self.title_text = title_text
        self.position_shift = position_shift

        # ---------------- Build Table ---------------- #
        self.title = Text(self.title_text, font_size=30).shift(
            UP * 3 + self.position_shift
        )

        # VGroups to hold parts of the table
        self.cells_group = VGroup()
        self.cell_contents = VGroup()
        self.row_labels_group = VGroup()
        self.col_labels_group = VGroup()

        # Build all components
        self.build_cells()
        self.build_labels()

        # Combine everything into this VGroup
        self.add(
            self.title,
            self.cells_group,
            self.cell_contents,
            self.row_labels_group,
            self.col_labels_group,
        )

    # ---------------- Build Cells ---------------- #
    def build_cells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pos_x = (
                    col - self.cols / 2 + 0.5
                ) * self.cell_width + self.position_shift[0]
                pos_y = (
                    self.rows / 2 - row - 0.5
                ) * self.cell_height + self.position_shift[1]

                # Rectangle cell
                cell = Rectangle(
                    width=self.cell_width,
                    height=self.cell_height,
                    stroke_width=self.cell_stroke_width,
                    color=WHITE,
                ).move_to([pos_x, pos_y, 0])

                # Empty text inside cell
                text = Text("", font_size=20).move_to(cell.get_center())

                self.cells_group.add(cell)
                self.cell_contents.add(text)

    # ---------------- Build Labels ---------------- #
    def build_labels(self):
        # Row labels (on left)
        for row in range(self.rows):
            pos_y = (
                self.rows / 2 - row - 0.5
            ) * self.cell_height + self.position_shift[1]
            label_text = self.row_labels[row] if row < len(self.row_labels) else ""
            label = Text(label_text, font_size=24).move_to(
                [
                    self.position_shift[0] - self.cols / 2 * self.cell_width - 0.4,
                    pos_y,
                    0,
                ]
            )
            self.row_labels_group.add(label)

        # Column labels (above)
        for col in range(self.cols):
            pos_x = (col - self.cols / 2 + 0.5) * self.cell_width + self.position_shift[
                0
            ]
            label_text = self.col_labels[col] if col < len(self.col_labels) else ""
            label = Text(label_text, font_size=24).move_to(
                [
                    pos_x,
                    self.position_shift[1] + self.rows / 2 * self.cell_height + 0.4,
                    0,
                ]
            )
            self.col_labels_group.add(label)
