from enum import Enum

class TextType(Enum):
    PLAIN_TEXT="plain"
    BOLD_TEXT="bold"
    ITALIC_TEXT="italic"
    CODE_TEXT="code"
    LINK_TEXT="link"
    IMAGE_TEXT="image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        text_matches = self.text == other.text
        text_type_matches = self.text_type == other.text_type
        url_matches = self.url == other.url
        return text_matches and text_type_matches and url_matches

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


