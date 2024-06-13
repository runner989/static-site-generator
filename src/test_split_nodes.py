import unittest

from inline_markdown import split_nodes_delimiter
from textnode import (
    TextNode, 
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_text_with_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word",text_type_text)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_text_with_bold(self):
        node = TextNode("This is **bold** text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" text", text_type_text)
        ]
        self.assertEqual(new_nodes, expected)

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_split_text_with_italic(self):
        node = TextNode("This is *italic* text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" text", text_type_text)
        ]
        self.assertEqual(new_nodes, expected)

    def test_unmatched_delimiter_raises_error(self):
        node = TextNode("This is *italic text", text_type_text)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "*", text_type_italic)

    def test_no_delimiter(self):
        node = TextNode("This is plain text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        expected = [node]
        self.assertEqual(new_nodes, expected)

    def test_non_text_node(self):
        node = TextNode("Link text", "link", "https://example.com")
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        expected = [node]
        self.assertEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()