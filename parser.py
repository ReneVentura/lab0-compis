from antlr4 import *
from YAPLGrammarLexer import YAPLGrammarLexer
from YAPLGrammarParser import YAPLGrammarParser

def parse_code(file_path):
    with open(file_path, "r") as file:
        code = file.read()

    lexer = YAPLGrammarLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = YAPLGrammarParser(stream)
    tree = parser.program()
    return tree

def format_tree(node, indent=""):
    if isinstance(node, TerminalNode):
        return indent + node.getText()
    
    result = indent + type(node).__name__ + "\n"
    for child in node.getChildren():
        result += format_tree(child, indent + "  ") + "\n"
    return result

# Example usage
file_path = "source.cl"

tree = parse_code(file_path)
formatted_tree = format_tree(tree, indent="  ")
print(formatted_tree)
