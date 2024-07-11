import os
import random
import string
import unittest

from diagrams import Diagram
from diagrams import setcluster, setdiagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

class TestDiagram(unittest.TestCase):
    def setUp(self):
        self.diagram = Diagram(name="Test Diagram")

    def test_add_node(self):
        self.diagram.add_node("A", label="Node A")
        self.assertIn("A", self.diagram.dot.source)

    def test_add_edge(self):
        self.diagram.add_node("A", label="Node A")
        self.diagram.add_node("B", label="Node B")
        self.diagram.add_edge("A", "B", label="Edge from A to B")
        self.assertIn("A -> B", self.diagram.dot.source)

    def test_add_nodes(self):
        nodes = [{"node_id": "A", "label": "Node A"}, {"node_id": "B", "label": "Node B"}]
        self.diagram.add_nodes(nodes)
        self.assertIn("A", self.diagram.dot.source)
        self.assertIn("B", self.diagram.dot.source)

    def test_add_edges(self):
        self.diagram.add_node("A", label="Node A")
        self.diagram.add_node("B", label="Node B")
        edges = [{"start_node": "A", "end_node": "B", "label": "Edge from A to B"}]
        self.diagram.add_edges(edges)
        self.assertIn("A -> B", self.diagram.dot.source)