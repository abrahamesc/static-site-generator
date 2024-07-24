from textnode import TextNode

def main():
    OneNode = TextNode("Hello, this is node one", "bold", "https://google.com")
    TwoNode = TextNode("Hello, this is node two", "italic", "https://www.youtube.com")
    ThreeNode = TextNode("Hello, this is node one", "bold", "https://google.com")

    print(f"Is node one equal to node three? {OneNode == ThreeNode}") 
    print(f"Contents of Node One: {OneNode}")
    print(f"Contents of Node Two: {TwoNode}")
    print(f"Contents of Node Three: {TwoNode}")


main()

