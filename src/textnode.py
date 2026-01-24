from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "plain_text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINK = "link"
    IMAGE = "image"
    
class TextNode:
    def __init__(self, text, text_type : TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, value):
        return ((self.text == value.text) and (self.text_type == value.text_type) and (self.url == value.url))

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        
    