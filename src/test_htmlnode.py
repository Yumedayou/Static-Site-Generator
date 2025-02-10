import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_html_node_init(self):
        node = HTMLNode(tag="p", value="Hello World", props={"class": "text-bold"})
        assert node.tag == "p"
        assert node.value == "Hello World"
        assert node.children is None
        assert node.props == {"class": "text-bold"}
    
    def test_props_to_html(self):
        node = HTMLNode(props={"id":"header", "class": "main-title"})
        assert node.props_to_html() == ' id="header" class="main-title"'

    def test_props_to_html_empty(self):
        node = HTMLNode()
        assert node.props_to_html() == ""

    def test_repr(self):
        node = HTMLNode(tag="div", value="Content", children=[], props={"style": "color:red;"})
        expected_repr = "HTMLNode(tag='div', value='Content', children='[], props='{'style': 'color:red;'}')"
        assert repr(node) == expected_repr

    def test_missing_props(self):
        node = HTMLNode(tag="span", value="No props here")
        assert node.props_to_html() == ""

    def test_leaf_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

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

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()