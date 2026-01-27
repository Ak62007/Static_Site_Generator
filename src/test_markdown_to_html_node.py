import unittest
from combine import (
    markdown_to_html_node
)

class TestMDToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )
    
    def test_paragraph(self):
        md = """
This is a simple paragraph with **bold** text and _italic_ words.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a simple paragraph with <b>bold</b> text and <i>italic</i> words.</p></div>",
        )

    def test_headings(self):
        md = """
# Heading 1

## Heading 2

### Heading 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>",
        )

    def test_blockquote(self):
        md = """
> This is a quote
> spanning multiple lines
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # Note: Your implementation joins quote lines with spaces
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote spanning multiple lines</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- Item 1
- Item 2
- Item **bold** 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item <b>bold</b> 3</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li></ol></div>",
        )
        
#     def test_full_document(self):
#         # Integration test with mixed types
#         md = """
# # Main Title

# This is a paragraph with [link](https://boot.dev).

# - List item 1
# - List item 2

# > A wise quote.
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
        
#         expected_html = (
#             "<div>"
#             "<h1>Main Title</h1>"
#             '<p>This is a paragraph with <a href="https://boot.dev">link</a>.</p>'
#             "<ul><li>List item 1</li><li>List item 2</li></ul>"
#             "<blockquote>A wise quote.</blockquote>"
#             "</div>"
#         )
#         self.assertEqual(html, expected_html)