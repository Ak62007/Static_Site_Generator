import unittest
from sync import (
    split_nodes_image,
    split_nodes_link
)
from textnode import (
    TextNode,
    TextType
)

class TestSplitImageLinkNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_split_links(self):
        node = TextNode(
            text="This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type=TextType.PLAIN_TEXT
        )
        new_nodes = split_nodes_link(old_nodes=[node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.PLAIN_TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.PLAIN_TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )
        
    def test_split_images_2(self):
        node1 = TextNode(
            text= "What is going on here? what is the image ![image](https://i.imgur.com/zjjcJKZ.png) and what about this ![image1](https://i.imgur.com/zjjcJKZ.png) and ![image2](https://i.imgur.com/zjjcJKZ.png) Htt!!!",
            text_type=TextType.PLAIN_TEXT
        )
        node2 = TextNode(
            text="what about this bold **oyeeeee**",
            text_type=TextType.BOLD_TEXT
        )
        new_nodes = split_nodes_image(old_nodes=[node1, node2])
        self.assertListEqual(
            [
                TextNode("What is going on here? what is the image ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and what about this ", TextType.PLAIN_TEXT),
                TextNode("image1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and ", TextType.PLAIN_TEXT),
                TextNode("image2", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" Htt!!!", TextType.PLAIN_TEXT),
                TextNode("what about this bold **oyeeeee**",TextType.BOLD_TEXT),
            ],
            new_nodes
        )