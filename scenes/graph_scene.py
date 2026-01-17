from manim import *
from components.GraphStructure import (
    GraphStructure,
)  # Your refactored class


class GraphDemo(Scene):
    def construct(self):
        # ----------------------------
        # Define node positions
        # ----------------------------
        node_positions = {
            "A": [-2, 2, 0],
            "B": [2, 2, 0],
            "C": [-4, 0, 0],
            "D": [4, 0, 0],
            "E": [2, -2, 0],
            "F": [-2, -2, 0],
            "G": [0, 0, 0],
        }

        # ----------------------------
        # Define edges as pairs of nodes
        # ----------------------------
        edge_pairs = [
            ("A", "B"),
            ("A", "C"),
            ("B", "G"),
            ("E", "F"),
            ("F", "G"),
            ("C", "F"),
            ("A", "D"),
            ("D", "F"),
        ]

        # ----------------------------
        # Create graph (undirected)
        # ----------------------------
        graph = GraphStructure(
            node_positions=node_positions,
            edge_pairs=edge_pairs,
            directed=False,
            node_stroke_color=PURPLE_C,
            node_fill_color=BLACK,
            node_label_color=WHITE,
            edge_color=DARK_BLUE,
        )

        # Center the graph on screen
        graph.move_to(ORIGIN)

        # ----------------------------
        # Animate nodes and edges
        # ----------------------------
        # First, animate nodes
        self.play(*[GrowFromCenter(node) for node in graph.nodes.values()])

        # Then, animate edges
        self.play(*[GrowFromCenter(edge) for edge in graph.edges])

        # ----------------------------
        # Optional: Highlight examples
        # ----------------------------
        graph.highlight_node(self, "A")
        graph.highlight_edge(self, 2)

        self.wait(2)
