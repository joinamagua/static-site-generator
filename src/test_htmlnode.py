import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props(self):
        test_prop = {"href": "https://google.com",}
        result_prop = " href=\"https://google.com\""
        
        node = HTMLNode("a", "text", None, test_prop)
        self.assertEqual(node.props_to_html(), result_prop)

    def test_multiple_props(self):
        test_props = {"href": "https://www.google.com","target": "_blank",}
        result_props = " href=\"https://www.google.com\" target=\"_blank\""

        node = HTMLNode("p", "text", None, test_props)
        self.assertEqual(node.props_to_html(),result_props)

    def test_no_props(self):
        test_props = {}
        result_props = ""

        node = HTMLNode("b", "noprops", None, None)
        self.assertEqual(node.props_to_html(), result_props)



