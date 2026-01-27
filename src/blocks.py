import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH="paragraph"
    HEADING="heading"
    CODE="code"
    QUOTE="quote"
    UNORDERED_LIST="unordered_list"
    ORDERED_LIST="ordered_list"
    
def block_to_block_type(block: str) -> BlockType:
    
    # Heading 
    heading_pattern = r"(?<!\*)\#{1,6} "
    # Code
    code_pattern = r"^```[a-zA-Z0-9]*\n[\s\S]*?\n```$"
    # ordered list
    ordered_list_pattern = r"^[1-9]\d*\. "
    
    if re.match(heading_pattern, block):
        return BlockType.HEADING
    elif re.match(code_pattern, block):
        return BlockType.CODE
    # quote block
    elif all(sen[0] == ">" for sen in block.split("\n") if sen != ""):
        return BlockType.QUOTE
    # unordered list
    elif all((sen[0] == "-") and (sen[1] == " ") for sen in block.split("\n") if sen != ""):
        return BlockType.UNORDERED_LIST
    # ordered list
    elif all(re.match(ordered_list_pattern, sen) for sen in block.split("\n")):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
        
    