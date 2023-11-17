import json
from antlr4 import *
from YAPLGrammarLexer import YAPLGrammarLexer
from YAPLGrammarParser import YAPLGrammarParser
from YAPLGrammarVisitor import YAPLGrammarVisitor
from tac import TACGeneratorVisitor

class SemanticAnalyzerVisitor(YAPLGrammarVisitor):
    def __init__(self):
        self.symbol_table = {}
        self.current_class = None
        self.inheritance_map = {}
        self.parent_class = None

    def get_type_with_size(self, type_name):
        # Define default sizes for types here
        default_sizes = {
            'Int': 4,
            'Bool': 1,
            'String': 256  # Default size for String
            # Add more default sizes for other types as needed
        }
        
        if type_name in default_sizes:
            return f"{type_name} Size: {default_sizes[type_name]}"
        else:
            return type_name

    def visitDeclaration(self, ctx: YAPLGrammarParser.DeclarationContext):
        method_name = ctx.IDENTIFIER().getText()
        method_type = self.get_type_with_size(ctx.type_().getText())

        if self.current_class:
            self.symbol_table[f"{self.current_class}.{method_name}"] = {
                "type": method_type,
                "class": self.current_class,
            }
        else:
            self.symbol_table[method_name] = {
                "type": method_type,
                "class": None,
            }

    def visitClassDeclaration(self, ctx: YAPLGrammarParser.ClassDeclarationContext):
        class_name = ctx.className().getText()
        self.current_class = class_name

        if ctx.INHERITS():
            parent_class = ctx.classNameParent().getText()
            self.inheritance_map[class_name] = parent_class
            self.parent_class = parent_class
        else:
            self.parent_class = None

        self.visitChildren(ctx)
        self.current_class = None

    def visitMethodDeclaration(self, ctx: YAPLGrammarParser.MethodDeclarationContext):
        method_name = ctx.methodName().getText()
        method_type = self.get_type_with_size(ctx.type_().getText())

        if self.current_class:
            self.symbol_table[f"{self.current_class}.{method_name}"] = {
                "type": method_type,
                "class": self.current_class,
            }
        else:
            self.symbol_table[method_name] = {
                "type": method_type,
                "class": None,
            }

    def visitMethodCall(self, ctx: YAPLGrammarParser.MethodCallContext):
        method_name = ctx.primaryExpression().methodName().getText()
        class_name = self.current_class

        current_class = class_name
        while current_class:
            full_method_name = f"{current_class}.{method_name}"
            if full_method_name in self.symbol_table:
                return self.symbol_table[full_method_name]["type"]
            elif self.inheritance_map.get(current_class):
                parent_class = self.inheritance_map[current_class]
                full_method_name_parent = f"{parent_class}.{method_name}"
                if full_method_name_parent in self.symbol_table:
                    return self.symbol_table[full_method_name_parent]["type"]
                current_class = parent_class
            else:
                current_class = None

        raise ValueError(f"Method '{method_name}' not defined in class '{class_name}' or its ancestors.")

def parse_code(code):
    lexer = YAPLGrammarLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = YAPLGrammarParser(stream)
    tree = parser.program()

    visitor = SemanticAnalyzerVisitor()
    visitor.visit(tree)
    tacCoder = TACGeneratorVisitor()
    tactree = parser.program()
    visitor.visit(tree)


    return tree, visitor.symbol_table

def format_tree(node, indent=""):
    if isinstance(node, TerminalNode):
        return indent + node.getText()

    result = indent + type(node).__name__ + "\n"
    for child in node.getChildren():
        result += format_tree(child, indent + "  ") + "\n"
    return result

def compile(code):
    tree, symbol_table = parse_code(code)
    formatted_tree = format_tree(tree, indent="  ")

    print("\nTabla de Símbolos:")
    for symbol_name, symbol_type in symbol_table.items():
        print(f"{symbol_name}: {symbol_type}")

    return formatted_tree, symbol_table

code = """
class MyClass {
    let myInt: Int;
    let myString: String;
    let myBool: Bool;
}

class YourClass {
    let yourInt: Int;
}
"""

formatted_tree, symbol_table = compile(code)
