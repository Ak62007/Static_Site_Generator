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

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        else:
            extracted_images = extract_markdown_images(node.text)
            first = 0
            img_first = 0
            nodes = []
            for img in extracted_images:
                image = f"![{img[0]}]({img[1]})"
                img_first = node.text.find(image)
                # Adding text
                nodes.append(
                    TextNode(
                        text=node.text[first:img_first],
                        text_type=TextType.PLAIN_TEXT
                    )
                )
                # Adding image
                nodes.append(
                    TextNode(
                        text=img[0],
                        text_type=TextType.IMAGE,
                        url=img[1]
                    )
                )
                first = img_first + len(image)
                
            # Adding the last part if there is something
            if node.text[first:] == "":
                # Extending the final list of nodes
                new_nodes.extend(nodes)
                continue
            else:
                nodes.append(
                    TextNode(
                        text=node.text[first:],
                        text_type=TextType.PLAIN_TEXT,
                    )
                )
                
                # Extending the final list of nodes
                new_nodes.extend(nodes)
    return new_nodes
                
def split_nodes_link(old_nodes : list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        else:
            extracted_links = extract_markdown_links(text=node.text)
            nodes = []
            first = 0
            img_first = 0
            for ext_link in extracted_links:
                link = f"[{ext_link[0]}]({ext_link[1]})"
                img_first = node.text.find(link)
                
                # Adding the text
                nodes.append(
                    TextNode(
                        text=node.text[first:img_first],
                        text_type=TextType.PLAIN_TEXT
                    )
                )
                
                # Adding the link
                nodes.append(
                    TextNode(
                        text=ext_link[0],
                        text_type=TextType.LINK,
                        url=ext_link[1]
                    )
                )
                
                # updating first
                first = img_first + len(link)

            if node.text[first:] == "":
                # Expending the new_nodes list
                new_nodes.extend(nodes)
                continue
            else:
                # Adding the remaining text
                nodes.append(
                    TextNode(
                        text=node.text[first:],
                        text_type=TextType.PLAIN_TEXT
                    )
                )
                # Extending
                new_nodes.extend(nodes)
    return new_nodes

# Finally using all the functions in one function
def text_to_textnodes(text):
    node = TextNode(
        text=text,
        text_type=TextType.PLAIN_TEXT
    )
    # Handling bold
    new_nodes = split_nodes_delimiter(
                    old_nodes=[node],
                    delimiter="**",
                    text_type=TextType.BOLD_TEXT
                )
    
    # Handling italic
    new_nodes = split_nodes_delimiter(
        old_nodes=new_nodes,
        delimiter="_",
        text_type=TextType.ITALIC_TEXT,
    )
    # Handling code
    new_nodes = split_nodes_delimiter(
        old_nodes=new_nodes,
        delimiter="`",
        text_type=TextType.CODE_TEXT,
    )
    # Handling Images
    new_nodes = split_nodes_image(
        old_nodes=new_nodes
    )
    # Handling Links
    new_nodes = split_nodes_link(
        old_nodes=new_nodes
    )
    
    return new_nodes

                                   
if __name__ == "__main__":
    # old_node = TextNode(
    #     text="This is text with a `code block` word",
    #     text_type=TextType.PLAIN_TEXT
    #     )
    
    # new_nodes = split_nodes_delimiter(old_nodes=[old_node], delimiter="`", text_type=TextType.CODE_TEXT)
    # print(len(new_nodes))
    # print(new_nodes)
    
    # text1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # print(f"Extracting images: {extract_markdown_images(text1)}")
    # print(f"Extracting links: {extract_markdown_links(text2)}")
    
    # Testing the split_nodes_image
    # node = TextNode(
    #     text=text1,
    #     text_type=TextType.PLAIN_TEXT
    # )
    
    # new_nodes = split_nodes_image(old_nodes=[node])
    # print(f"splited images:\n{new_nodes}\n")
    
    # Testing the split_nodes_link.
    # node = TextNode(
    #     text=text2,
    #     text_type=TextType.PLAIN_TEXT
    # )
    # new_nodes = split_nodes_link(old_nodes=[node])
    # print(f"splited links:\n{new_nodes}")
    
    # Testing the final function to test all the functions all at once
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    new_nodes = text_to_textnodes(text=text)
    print(f"Text: {text}\n")
    for i, node in enumerate(new_nodes):
        print(f"node {i+1}: {node}")