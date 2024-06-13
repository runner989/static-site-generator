# src/test_converters.py

import unittest
from textnode import TextNode, text_node_to_html_node

class TestConverters(unittest.TestCase):
    def test_text_to_html(self):
        text_node = TextNode("This is text", "text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "This is text")

    def test_bold_to_html(self):
        text_node = TextNode("Bold text", "bold")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_italic_to_html(self):
        text_node = TextNode("Italic text", "italic")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_code_to_html(self):
        text_node = TextNode("Code text", "code")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code text</code>")

    def test_link_to_html(self):
        text_node = TextNode("Click me!", "link", "https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.example.com">Click me!</a>')

    def test_image_to_html(self):
        text_node = TextNode("Alt text", "image", "https://www.example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.example.com/image.png" alt="Alt text"></img>')

    def test_unknown_type(self):
        text_node = TextNode("Unknown type", "unknown")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()

