import unittest
from htmlnode import HTMLNode 

class TestHTMLNode(unittest.TestCase):
    #def test_props_to_html(self):
    #    node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
     #   self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_repr(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.boot.dev"})
        self.assertEqual(repr(node), "HTMLNode(tag=a, value=Click here, children=None, props={'href': 'https://www.boot.dev'})")

if __name__ == "__main__":
    unittest.main()
