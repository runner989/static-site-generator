import unittest

from textnode import TextNode 

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is also a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node1 = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node1, node2)

    def test_eq_link(self):
        node1 = TextNode("This is a text node", "link", "https://www.google.com")
        node2 = TextNode("This is a text node", "link", "https://www.google.com")
        self.assertEqual(node1, node2)

    def test_not_eq_link(self):
        node1 = TextNode("This is a text node", "link", "https://www.cnn.com")
        node2 = TextNode("This is a text node", "link", "https://www.google.com")
        self.assertNotEqual(node1, node2)

    def test_eq_link_None(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
