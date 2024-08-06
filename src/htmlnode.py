

class HTMLNode():
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        props = ""
        for key,value in self.props.items():
            props += f' {key}="{value}"'
        return props

    def __repr__(self):
        return f"HTMLNode=Tag={self.tag}, Value={self.value}, Children={self.children}, Props={self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

        if self.value == None:
            raise ValueError("No Value provided")

    def to_html(self):

        if self.tag == None:
            return f'{self.value}'

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag, None, children, None)

        if self.tag is None:
            raise ValueError("Invalid ParentNode: No tag")

        if self.children is None:
            raise ValueError("Invalid ParentNode: No Children")

    def to_html(self):

        parent_string = ""

        for children in self.children:
            parent_string += children.to_html()

        return f"<{self.tag}>{parent_string}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children})"

