import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_ital(self):
        node = TextNode("This is unoriginal text", TextType.ITALIC)
        node2 = TextNode("This is unoriginal text", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_text(self):
        node = TextNode("if (i < j)? return i: return j;", TextType.CODE)
        node2 = TextNode("if (i < j)? return i: return j;", TextType.CODE)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_neq_img(self):
        node = TextNode("Python 'two snakes'", TextType.IMAGE, "https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png")
        node2 = TextNode("Python 'two snakes'", TextType.IMAGE, None)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
