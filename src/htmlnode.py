class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ""
        if self.props:
            for key, value in self.props.items():
                result += f" {key}=\"{value}\""

        return result
    
    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children='{self.children}, props='{self.props}')"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag='{self.tag}', value='{self.value}', props='{self.props}')"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Not a valid HTML tag")
        if self.children is None:
            raise ValueError("No child nodes given")

        html_line = ""
        for child in self.children:
            html_line += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_line}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"