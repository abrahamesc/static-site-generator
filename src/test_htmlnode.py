import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class test_HTMLNode(unittest.TestCase):
    def test_HTMLNode_props(self):
        node1 = HTMLNode("p", "This is the paragraph",None, {"href":"https://www.google.com"})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com"')

    def test_no_props(self):
        node1 = HTMLNode('p', "This is just a paragraph", None, None)
        self.assertEqual(node1.props_to_html(), "")

    def test_props_two(self):
        node1 = HTMLNode("a", "This is the paragraph",None, {"href":"https://www.google.com", "target":"_blank"})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_multiple(self):
        node1 = HTMLNode("a", "This is the paragraph",None, {"href":"https://www.google.com", "target":"_blank", "download":"report.pdf"})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank" download="report.pdf"')

    def test_repr(self):
        node1 = HTMLNode("a", "This is the paragraph",None, {"href":"https://www.google.com", "target":"_blank"})
        self.assertEqual(repr(node1), "HTMLNode=Tag=a, Value=This is the paragraph, Children=None, Props={'href': 'https://www.google.com', 'target': '_blank'}")
        
class test_LeafNode(unittest.TestCase):
    def test_leaf_p(self):
        leaf1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf1.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_a(self):
        leaf1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf1.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_a_plus(self):
        leaf1 = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target":"_blank", "download":"report.pdf"})
        self.assertEqual(leaf1.to_html(), '<a href="https://www.google.com" target="_blank" download="report.pdf">Click me!</a>')

    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)
        


class test_ParentNode(unittest.TestCase):
    def test_multiple_children(self):
        node1 = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
                )
        self.assertEqual(node1.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode(
                    "a",
                    None)

    def test_no_tag(self):

        with self.assertRaises(ValueError):
            
            ParentNode(
                    None,
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                    )

    def test_multiple_parents(self):
        node1 = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    ParentNode("div", [LeafNode("i", "Nested Italic Text")]),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
                )
        self.assertEqual(node1.to_html(), "<p><b>Bold text</b>Normal text<div><i>Nested Italic Text</i></div><i>italic text</i>Normal text</p>")
