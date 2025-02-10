import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node = TextNode("Yippee", TextType.BOLD_TEXT)
        node2 = TextNode("Yahoo", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_not_equal_url(self):
        node = TextNode("Yippee", TextType.BOLD_TEXT, "www.differentwebsite.com")
        node2 = TextNode("Yahoo", TextType.BOLD_TEXT, "www.webiste.com")
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("Yippee", TextType.NORMAL_TEXT)
        self.assertIsNone(node.url)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.NORMAL_TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGES, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()