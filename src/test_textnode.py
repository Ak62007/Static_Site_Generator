import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
        
    def test_not_eq(self):
        node = TextNode("wtf!!!", TextType.CODE_TEXT)
        node2 = TextNode("whattt!!!", TextType.CODE_TEXT)
        self.assertNotEqual(node, node2)
        
    def test_not_eq_2(self):
        node = TextNode("wtf!!!", TextType.BOLD_TEXT)
        node2 = TextNode("whattt!!!", TextType.CODE_TEXT)
        self.assertNotEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()