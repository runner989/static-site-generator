import unittest
from textnode import TextNode
from inline_markdown import split_nodes_image, split_nodes_link

class TestSplitNodesImageLink(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://avatars.githubusercontent.com/u/72108331?s=200&v=4) and another ![image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbQ0tSGTyEXuYHnUakuJw7MJaRcDaU9eopI-tqb5uUYSRYcV8cC8XrQoWAWaK2a2srXh0&usqp=CAU)",
            "text"
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", "text"),
            TextNode("image", "image", "https://avatars.githubusercontent.com/u/72108331?s=200&v=4"),
            TextNode(" and another ", "text"),
            TextNode("image", "image", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbQ0tSGTyEXuYHnUakuJw7MJaRcDaU9eopI-tqb5uUYSRYcV8cC8XrQoWAWaK2a2srXh0&usqp=CAU")
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and a second [link](https://www.google.com)",
            "text"
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a ", "text"),
            TextNode("link", "link", "https://www.boot.dev"),
            TextNode(" and a second ", "text"),
            TextNode("link", "link", "https://www.google.com")
        ]
        self.assertEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()