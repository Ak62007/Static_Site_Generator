import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="<p>", value="oyee", props={"oyee": 2})
        result = node.props_to_html()
        self.assertTrue((result.find("oyee") != -1) and (result.find("2") != -1))
        
    