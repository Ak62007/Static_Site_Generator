import re
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
def manage_code(block: str) -> str:
    return block.strip("```").strip("\n")
    
def manage_ol_ul(block: str) -> list[ParentNode]:
    points = []
    for point in block.split("\n"):
        tag = "li"
        children = inline_md_to_html_nodes(text=point[2:])
        points.append(
            ParentNode(
                tag=tag,
                children=children
            )
        )

def manage_quotes(block: str) -> str:
    return " ".join(list(map(lambda x : x[1:], block.split("\n"))))

def inline_md_to_html_nodes(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text=text)
    html_nodes = list(map(text_node_to_html_node, text_nodes))
    return html_nodes
        

def markdown_to_html_node(markdown: str):
    # step 1 convert the raw matkdown into typed markdown blocks
    block_list = markdown_to_blocks(markdown=markdown)
    u_children = []
    for block in block_list:
        # determining the block type
        block_type = block_to_block_type(block=block)
        # Creating the HTMLNode
        if block_type == BlockType.HEADING:
            pattern = r"^#+ "
            result = re.match(pattern, block)
            tag = f"h{len(result.group())}"
            children = inline_md_to_html_nodes(text=block[result.end()+1:])
            u_children.append(
                HTMLNode(
                    tag=tag,
                    children=children,
                )
            )
        elif block_type == BlockType.QUOTE:
            tag = "blockquote"
            children = inline_md_to_html_nodes(text=manage_quotes(block=block))
            u_children.append(
                HTMLNode(
                    tag=tag,
                    children=children,
                )
            )
            
        elif block_type == BlockType.ORDERED_LIST:
            tag = "ol"
            children = manage_ol_ul(block=block)
            u_children.append(
                HTMLNode(
                    tag=tag,
                    children=children
                )
            )
            
        elif block_type == BlockType.UNORDERED_LIST:
            tag = "ul"
            children = manage_ol_ul(block=block)
            u_children.append(
                HTMLNode(
                    tag=tag,
                    children=children
                )
            )
            
        elif block_type == BlockType.CODE:
            u_children.append(
                text_node_to_html_node(
                    text_node=TextNode(
                        text=manage_code(block=block),
                        text_type=TextType.CODE_TEXT
                    )
                )
            )
            
        else:
            # this has to be paragraph type
            tag = "p"
            children = inline_md_to_html_nodes(text=block)
            u_children(
                HTMLNode(
                    tag=tag,
                    children=children
                )
            )
            
    parent_node = ParentNode(
        tag="div",
        children=u_children,
    )
    
    return parent_node