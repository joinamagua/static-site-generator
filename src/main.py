from textnode import TextType, TextNode

def main(): 
    text_sample = "This is some anchor text"
    text_type_sample = TextType.LINK_TEXT
    text_url_sample = "https://www.boot.dev"
    sample = TextNode(text_sample,
                      text_type_sample,
                      text_url_sample)
    print(sample)

if __name__ == "__main__":
    main()
