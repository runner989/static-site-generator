from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text 
        self.text_type = text_type 
        self.url = url 

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and 
            self.url == other.url 
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def to_html(self):
        if self.text_type == "link":
            return f'<a href="{self.url}">{self.text}</a>'
        elif self.text_type == "image":
            return f'<img src="{self.url}" alt="{self.text}" />'
        elif self.text_type == "bold":
            return f'<b>{self.text}</b>'
        elif self.text_type == "italic":
            return f'<i>{self.text}</i>'
        elif self.text_type == "code":
            return f'<code>{self.text}</code>'
        else:
            return self.text


def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        if text_node.url is None:
            raise ValueError("Link TextNode requires a URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "image":
        if text_node.url is None:
            raise ValueError("Image TextNode requires a URL")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")

