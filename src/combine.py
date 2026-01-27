import re
from typing import Literal
from sync import (
    markdown_to_blocks,
    text_to_textnodes,
    text_node_to_html_node,
)
from blocks import (
    block_to_block_type,
    BlockType
)
from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode
)
from textnode import (
    TextNode,
    TextType
)

# Helper functions
def inline_md_to_html_nodes(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text=text)
    html_nodes = list(map(text_node_to_html_node, text_nodes))
    return html_nodes

def manage_para(block: str) -> list[LeafNode]:
    return inline_md_to_html_nodes(" ".join(block.split("\n")))

def manage_code(block: str) -> str:
    lines = block.split("\n")
    if len(lines) > 2:
        return "\n".join(lines[1:-1])
    return ""
    
def manage_ol_ul(block: str, type: Literal["ol", "ul"]) -> list[ParentNode]:
    points = []
    for point in block.split("\n"):
        tag = "li"
        if type == "ol":
            children = inline_md_to_html_nodes(text=point[3:])
        else:
            children = inline_md_to_html_nodes(text=point[2:])
        points.append(
            ParentNode(
                tag=tag,
                children=children
            )
        )
    return points

def manage_quotes(block: str) -> str:
    return " ".join(list(map(lambda x : x[2:] if x.startswith("> ") else x[1:], block.split("\n"))))
        

def markdown_to_html_node(markdown: str):
    # step 1 convert the raw matkdown into typed markdown blocks
    block_list = markdown_to_blocks(markdown=markdown)
    u_children = []
    for block in block_list:
        if block.strip() == "":
            continue            
        # print(f"Processing block: {block}")
        # determining the block type
        block_type = block_to_block_type(block=block)
        # Creating the HTMLNode
        if block_type == BlockType.HEADING:
            pattern = r"^#+"
            result = re.match(pattern, block)
            tag = f"h{len(result.group())}"
            children = inline_md_to_html_nodes(text=block[result.end()+1:])
            u_children.append(
                ParentNode(
                    tag=tag,
                    children=children,
                )
            )
        elif block_type == BlockType.QUOTE:
            tag = "blockquote"
            children = inline_md_to_html_nodes(text=manage_quotes(block=block))
            u_children.append(
                ParentNode(
                    tag=tag,
                    children=children,
                )
            )
            
        elif block_type == BlockType.ORDERED_LIST:
            tag = "ol"
            children = manage_ol_ul(block=block, type='ol')
            u_children.append(
                ParentNode(
                    tag=tag,
                    children=children
                )
            )
            
        elif block_type == BlockType.UNORDERED_LIST:
            tag = "ul"
            children = manage_ol_ul(block=block, type='ul')
            u_children.append(
                ParentNode(
                    tag=tag,
                    children=children
                )
            )
            
        elif block_type == BlockType.CODE:
            code_node = text_node_to_html_node(
                            text_node=TextNode(
                                text=manage_code(block=block),
                                text_type=TextType.CODE_TEXT
                            )
                        )
            pre_node = ParentNode(
                tag="pre",
                children=[code_node]
            )
            
            u_children.append(pre_node)
        else:
            # this has to be paragraph type
            tag = "p"
            children = manage_para(block=block)
            u_children.append(
                ParentNode(
                    tag=tag,
                    children=children
                )
            )
            
    parent_node = ParentNode(
        tag="div",
        children=u_children,
    )
    
    return parent_node


if __name__ == "__main__":
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """
    node = markdown_to_html_node(markdown=md)
    print(node.to_html())