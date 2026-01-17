from manim import *


# ---------------- Graph Skeleton ---------------- #
class GraphStructure(VGroup):
    def __init__(
        self,
        node_positions=None,
        edge_pairs=None,
        directed=False,
        node_stroke_color=PURPLE_C,
        node_fill_color=BLACK,
        node_label_color=WHITE,
        edge_color=DARK_BLUE,
        **kwargs
    ):
        """
        node_positions: dict -> {"A": [0,0,0], ...}
        edge_pairs: list of tuples -> [("A", "B"), ("B", "C")]
        directed: bool -> whether edges are arrows
        """
        super().__init__(**kwargs)

        # ---------------- Class Variables ---------------- #
        self.node_positions = node_positions or {}
        self.edge_pairs = edge_pairs or []
        self.directed = directed
        self.node_stroke_color = node_stroke_color
        self.node_fill_color = node_fill_color
        self.node_label_color = node_label_color
        self.edge_color = edge_color

        self.nodes = {}  # {label: VGroup(circle+text)}
        self.edges = []  # list of Line or Arrow

        # Build graph visually
        self.build_graph()

    # ---------------- Build the graph ---------------- #
    def build_graph(self):
        """Create nodes and edges based on class variables"""
        # Create nodes
        for label, pos in self.node_positions.items():
            circle = Circle(
                radius=0.5,
                fill_color=self.node_fill_color,
                fill_opacity=1,
                color=self.node_stroke_color,
                stroke_width=5,
            )
            circle.move_to(pos)
            text = Text(label, color=self.node_label_color).move_to(pos)
            self.nodes[label] = VGroup(circle, text)
            self.add(self.nodes[label])

        # Create edges
        for node1, node2 in self.edge_pairs:
            start = self.node_positions[node1]
            end = self.node_positions[node2]
            if self.directed:
                edge = Arrow(
                    start, end, buff=0.5, color=self.edge_color, stroke_width=4
                )
            else:
                edge = Line(start, end, color=self.edge_color, stroke_width=4)
            edge.z_index = -1
            self.edges.append(edge)
            self.add(edge)

    # ---------------- Optional: Highlight a node ---------------- #
    def highlight_node(self, scene, label, color=YELLOW_E):
        if label in self.nodes:
            circle = self.nodes[label][0]
            scene.play(circle.animate.set_fill(color), run_time=0.5)

    # ---------------- Optional: Highlight an edge ---------------- #
    def highlight_edge(self, scene, index, color=RED):
        if 0 <= index < len(self.edges):
            scene.play(self.edges[index].animate.set_color(color), run_time=0.5)
