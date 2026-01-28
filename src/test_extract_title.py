import unittest

from main import (
    extract_title
)

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """# Copy Static

We've written a _lot_ of unit tests, it's time to start pulling all the pieces together into a working static site generator. Let's work on that `main.py` file that we've been neglecting.

## Assignment"""
        title = extract_title(markdown=md)
        self.assertEqual(
            title,
            "Copy Static"
        )
        
    def test_extract_title_2(self):
        md = """# LeafNode

Time to render some HTML strings!

A `LeafNode` is a type of `HTMLNode` that represents a single HTML tag _with no children_. For example, a simple `<p>` tag with some text inside of it:

```html
<p>This is a paragraph of text.</p>
```

We call it a "leaf" node because it's a "leaf" in the tree of HTML nodes. It's a node with no children. In this next example, `<p>` is _not_ a leaf node, but `<b>` is."""
        title = extract_title(md)
        self.assertEqual(
            title,
            "LeafNode"
        )
        
    def test_extract_title_3(self):
        md = """Time to render some HTML strings!

A `LeafNode` is a type of `HTMLNode` that represents a single HTML tag _with no children_. For example, a simple `<p>` tag with some text inside of it:

```html
<p>This is a paragraph of text.</p>
```"""
        with self.assertRaises(ValueError):
            title = extract_title(md)