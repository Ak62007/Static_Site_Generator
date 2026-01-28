class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return None
        else:
            pair_string = [f' {key}="{value}" ' for key, value in self.props.items()]
            return "".join(pair_string)
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props_to_html()})"
    
    
# Leaf node
class LeafNode(HTMLNode):
    def __init__(self, tag , value, props = None):
        super().__init__(tag=tag, value=value, props=props)
        
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Value not provided")
        
        if not self.tag:
            return self.value
        
        if self.tag == 'p':
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        elif self.tag == 'a':
            if not self.props:
                raise ValueError("props is not given for the link tag.")
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
        elif self.tag == 'img':
            if not self.props:
                raise ValueError("props is not given for the img tag")
            return f'<{self.tag}{self.props_to_html()}alt="{self.value}"/>'
        
        elif "h" in self.tag:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props_to_html()})"
    
# Parent node    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag, children=children, props=props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag not provided")
        
        if not self.children:
            raise ValueError("Parent node must have a children")
        
        result = ""
        for child in self.children:
            result += child.to_html()
            
        return f"<{self.tag}>{result}</{self.tag}>"