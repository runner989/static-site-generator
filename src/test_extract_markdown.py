import unittest
from inline_markdown import extract_markdown_links, extract_markdown_images

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self): 
        text = "This is text with an ![image](https://avatars.githubusercontent.com/u/72108331?s=200&v=4) and ![another](https://blog.boot.dev/img/800/bootdev-explorer.png.webp)"
        expected = [
            ("image", "https://avatars.githubusercontent.com/u/72108331?s=200&v=4"),
            ("another", "https://blog.boot.dev/img/800/bootdev-explorer.png.webp")
        ]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.boot.dev) and [another](https://www.google.com)"
        expected = [
            ("link", "https://www.boot.dev"),
            ("another", "https://www.google.com")
        ]
        self.assertEqual(extract_markdown_links(text), expected)

if __name__ == "__main__":
    unittest.main()