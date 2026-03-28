
class HTMLNode:

    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        result = ""
        if self.props is not None and self.props is not {}:
            for pk in self.props.keys():
                result += f' {pk}="{self.props[pk]}"'
        return result

    def __repr__(self):
        str_children = "children:\n"
        for child in self.children:
            str_children += "\t{child}\n"
        return f"HTMLNODE\n\t{self.tag}\n\t{self.value}\n\t{str_children}\n\t{self.props_to_html()}"

