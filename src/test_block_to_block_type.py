import unittest
from blocks import (
    BlockType,
    block_to_block_type
)

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_blocktype_unlist(self):
        eg = """- matches any word character ([alphanumeric](https://en.wikipedia.org/wiki/Alphanumericals) characters and underscores)
- means "one or more of the preceding character"
- is just a literal  symbol that we want to match
- is a literal that we want to match (The is a special character in regex, so we escape it with a leading backslash)
"""
        result = block_to_block_type(block=eg)
        self.assertEqual(
            result,
            BlockType.UNORDERED_LIST
        )
    
    def test_block_to_blocktype_code(self):
        eg = """```python
text = "My email is lane@example.com and my friend's email is hunter@example.com"
print(matches)  # [('lane', 'example.com'), ('hunter', 'example.com')]
```"""
        result = block_to_block_type(block=eg)
        self.assertEqual(
            result,
            BlockType.CODE
        )
        
    def test_block_to_blocktype_heading(self):
        eg = "## Testing Regexes"
        result = block_to_block_type(block=eg)
        self.assertEqual(
            result,
            BlockType.HEADING
        )
        
    def test_block_to_blocktype_quote(self):
        eg = """> My name is Aditya kumar
> What is your name ?"""
        result = block_to_block_type(block=eg)
        self.assertEqual(
            result,
            BlockType.QUOTE
        )
        
    def test_block_to_blocktype_quote(self):
        eg = """> 1.My name is Aditya kumar
> What is your name ?"""
        result = block_to_block_type(block=eg)
        self.assertEqual(
            result,
            BlockType.QUOTE
        )
        
    def test_block_to_blocktype_o_list(self):
        eg = """1. what is going on?
2. what is your name?
3. what ???"""
        result = block_to_block_type(block=eg)
        self.assertEqual(
            result,
            BlockType.ORDERED_LIST
        )
        
    def test_block_to_blocktype_para(self):
        eg = """what is going on here>"""
        result = block_to_block_type(block=eg)
        self.assertEqual(
            result,
            BlockType.PARAGRAPH
        )
        
    def test_block_to_blocktype_para_2(self):
        eg = """what is 2.going on here 1."""
        result = block_to_block_type(block=eg)
        self.assertEqual(
            result,
            BlockType.PARAGRAPH
        )
        
    