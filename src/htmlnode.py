class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        pair_string = [f" {key}={value} " for key, value in self.props.items()]
        return "".join(pair_string)
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props_to_html})"
    
    