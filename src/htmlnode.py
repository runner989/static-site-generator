class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag 
        self.value = value 
        self.children = children 
        self.props = props 

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        if value is None:
            raise ValueError("All leaf nodes require a value")
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.tag is None:
            return self.value 
        
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag, None, children)
        if tag is None:
            raise ValueError("ParentNode tag is required")
        if not children:
            raise ValueError("At least one child is required")
        self.tag = tag 
        self.children = children

    def to_html(self):
        if not self.children:
            raise ValueError("ParentNode requires at least one child")
        children_html = ''.join(child.to_html() for child in self.children)

        return f"<{self.tag}>{children_html}</{self.tag}>"


