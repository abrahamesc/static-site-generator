import unittest
from textnode import TextNode

class test_TextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

    def test_eq_two(self):
        node1 = TextNode("this is test two", "italic", "https://www.google.com/something")
        node2 = TextNode("this is test two", "italic", "https://www.google.com/something")
        self.assertEqual(node1, node2)

    def test_not_equal(self):
        node1 = TextNode("This is the third test", "italic", None)
        node2 = TextNode("This is the third test, node2", "bold", None)
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
