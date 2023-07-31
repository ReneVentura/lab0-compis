from antlr4 import *
from YAPLGrammarLexer import YAPLGrammarLexer
from YAPLGrammarParser import YAPLGrammarParser
from YAPLGrammarVisitor import YAPLGrammarVisitor

# Define a class for semantic analysis using the visitor pattern
class SemanticAnalyzerVisitor(YAPLGrammarVisitor):
    def __init__(self):
        self.symbol_table = {}

    def visitDeclaration(self, ctx: YAPLGrammarParser.DeclarationContext):
        # Extract information from the Declaration node
        name = ctx.IDENTIFIER().getText()
        symbol_type = ctx.type_().getText()

        # Add the symbol to the symbol table
        self.symbol_table[name] = symbol_type

    def visitArithmeticExpression(self, ctx: YAPLGrammarParser.ArithmeticExpressionContext):
        left = self.visit(ctx.primaryExpression(0))
        right = self.visit(ctx.primaryExpression(1))
        operator = ctx.getChild(1).getText()

        if isinstance(left, int) and isinstance(right, int):
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                return left / right
            else:
                return (f"Unsupported arithmetic operator: {operator}")
        else:
            return ("Arithmetic expressions must contain integer operands.")

    def visitPrimaryExpression(self, ctx: YAPLGrammarParser.PrimaryExpressionContext):
        if ctx.INT_LITERAL():
            print(int(ctx.INT_LITERAL().getText()))
            return int(ctx.INT_LITERAL().getText())
        elif ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText()[1:-1]  # Remove the quotes from the string literal
        elif ctx.IDENTIFIER():
            # Get the type from the symbol table
            identifier = ctx.IDENTIFIER().getText()
            symbol_type = self.symbol_table.get(identifier)
            if symbol_type is not None:
                return symbol_type
            else:
                raise ValueError(f"Variable or method '{identifier}' not defined.")
        elif ctx.NEW():
            class_name = ctx.className().getText()
            return f"new {class_name}"
        # Add other cases for NEW, method calls, etc.

def parse_code(file_path):
    with open(file_path, "r") as file:
        code = file.read()

    lexer = YAPLGrammarLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = YAPLGrammarParser(stream)
    tree = parser.program()

    # Perform semantic analysis using the visitor
    visitor = SemanticAnalyzerVisitor()
    visitor.visit(tree)

    return tree, visitor.symbol_table

def format_tree(node, indent=""):
    if isinstance(node, TerminalNode):
        return indent + node.getText()
    
    result = indent + type(node).__name__ + "\n"
    for child in node.getChildren():
        result += format_tree(child, indent + "  ") + "\n"
    return result


# Example usage
file_path = "source.cl"
tree, symbol_table = parse_code(file_path)

# Print the tree
formatted_tree = format_tree(tree, indent="  ")
print("Árbol de Análisis Sintáctico:")
print(formatted_tree)

# Print the symbol table
print("\nTabla de Símbolos:")
for symbol_name, symbol_type in symbol_table.items():
    print(f"{symbol_name}: {symbol_type}")
