import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from sync import text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="<p>", value="oyee", props={"oyee": 2})
        result = node.props_to_html()
        self.assertTrue((result.find("oyee") != -1) and (result.find("2") != -1))
        
    def test_leaf_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_a(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" >Click me!</a>')
        
    def test_leaf_to_html_img(self):
        node = LeafNode(tag="img", value="Description of image", props={"src": "url/of/image.jpg"})
        self.assertEqual(node.to_html(), '<img src="url/of/image.jpg" alt="Description of image"/>')
        
    def test_leaf_to_html_h(self):
        node = LeafNode(tag="h2", value="oyeeeeeee!!!!")
        self.assertEqual(node.to_html(), '<h2>oyeeeeeee!!!!</h2>')
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_with_complex_nest(self):
        grand_grand_child_node_1 = LeafNode("h1", "oyeee")
        grand_grand_child_node_2 = LeafNode("h2", "oyee")
        grand_child_node_1 = ParentNode("span", [grand_grand_child_node_1, grand_grand_child_node_2])
        child_node = ParentNode("div", [grand_child_node_1])
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<p><div><span><h1>oyeee</h1><h2>oyee</h2></span></div></p>"
        )
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        