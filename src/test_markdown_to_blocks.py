import unittest
from markdown_to_blocks import (
    markdown_to_blocks, 
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
        This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items
        """
        
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]
        
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_empty_markdown(self):
        markdown = ""
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_only_newlines(self):
        markdown = "\n\n\n\n"
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_no_double_newlines(self):
        markdown = "This is a single block without double newlines."
        expected = ["This is a single block without double newlines."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading 1"), block_type_heading)
        self.assertEqual(block_to_block_type("```\nCode block\n```"), block_type_code)
        self.assertEqual(block_to_block_type("> Quote block"), block_type_quote)
        self.assertEqual(block_to_block_type("* Unordered list item\n* Another unordered list item"), block_type_unordered_list)
        self.assertEqual(block_to_block_type("1. Ordered list item\n2. Another ordered list item"), block_type_ordered_list)
        self.assertEqual(block_to_block_type("Just a normal paragraph."), block_type_paragraph)




if __name__ == "__main__":
    unittest.main()