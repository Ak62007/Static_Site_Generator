import unittest
from sync import text_to_textnodes
from textnode import (
    TextNode,
    TextType,
)

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text=text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("text", TextType.BOLD_TEXT),
                TextNode(" with an ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" word and a ", TextType.PLAIN_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" and an ", TextType.PLAIN_TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )
        
    def test_text_to_textnode_2(self):
        text = 'Before we build the next bit, we need to understand a bit about [regex](https://docs.python.org/3/library/re.html)es, or "regular expressions". "Regex" for short, is a programming-language-agnostic way of **searching for patterns in text**.'
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode('Before we build the next bit, we need to understand a bit about ', TextType.PLAIN_TEXT),
                TextNode('regex', TextType.LINK, 'https://docs.python.org/3/library/re.html'),
                TextNode('es, or "regular expressions". "Regex" for short, is a programming-language-agnostic way of ', TextType.PLAIN_TEXT),
                TextNode('searching for patterns in text', TextType.BOLD_TEXT),
                TextNode('.', TextType.PLAIN_TEXT),
            ],
            new_nodes
        )
        
    def test_text_to_textnode_3(self):
        text = "The general syntax is `(?<!pattern)` where `pattern` is what you don't want to see before your match"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("The general syntax is ", TextType.PLAIN_TEXT),
                TextNode("(?<!pattern)", TextType.CODE_TEXT),
                TextNode(" where ", TextType.PLAIN_TEXT),
                TextNode("pattern", TextType.CODE_TEXT),
                TextNode(" is what you don't want to see before your match", TextType.PLAIN_TEXT)
            ],
            new_nodes
        )