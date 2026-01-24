import re
from textnode import TextType, TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.PLAIN_TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE_TEXT:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value=text_node.text, props={"src": text_node.url})
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")
    
    
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        else:
            splited_text = node.text.split(delimiter)
            if len(splited_text) % 2 == 0:
                raise Exception("Invalid Markdown Syntax!")
            nodes = []
            for i in range(len(splited_text)):
                if splited_text[i] == "":
                    continue
                if i % 2 == 0:
                    nodes.append(TextNode(text=splited_text[i], text_type=TextType.PLAIN_TEXT))
                else:
                    nodes.append(TextNode(text=splited_text[i], text_type=text_type))    
            new_nodes.extend(nodes)        
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)
    
                                   
if __name__ == "__main__":
    # old_node = TextNode(
    #     text="This is text with a `code block` word",
    #     text_type=TextType.PLAIN_TEXT
    #     )
    
    # new_nodes = split_nodes_delimiter(old_nodes=[old_node], delimiter="`", text_type=TextType.CODE_TEXT)
    # print(len(new_nodes))
    # print(new_nodes)
    
    text1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(f"Extracting images: {extract_markdown_images(text1)}")
    print(f"Extracting links: {extract_markdown_links(text2)}")