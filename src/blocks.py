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
    
    if re.match(pattern=heading_pattern):
        return BlockType.HEADING
    elif re.match(pattern=code_pattern):
        return BlockType.CODE
        
    