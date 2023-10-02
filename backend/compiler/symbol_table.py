from antlr4 import *
from YAPLGrammarLexer import YAPLGrammarLexer
from YAPLGrammarParser import YAPLGrammarParser
from YAPLGrammarVisitor import YAPLGrammarVisitor

# Define a class for semantic analysis using the visitor pattern
class SemanticAnalyzerVisitor(YAPLGrammarVisitor):
    def __init__(self):
        self.symbol_table = {}        
        self.temp_counter = 0
        self.code = []  # Lista para almacenar el código intermedio
        self.current_class = None  # Para rastrear la clase actual
        self.current_method = None  # Para rastrear el método actual
        self.current_function = None  # Para rastrear la función actual



    def visitDeclaration(self, ctx: YAPLGrammarParser.DeclarationContext):
        # Extract information from the Declaration node
        name = ctx.IDENTIFIER().getText()
        symbol_type = ctx.type_().getText()
        symbol_size = ctx.type_().size  # Obtener el tamaño definido en la gramática

        # Add the symbol to the symbol table with type and size information
        self.symbol_table[name] = {"type": symbol_type, "size": symbol_size}


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

    def visitArithmeticExpr(self, ctx: YAPLGrammarParser.ArithmeticExprContext):
        left = self.visit(ctx.primaryExpression())
        right = self.visit(ctx.expression())

        # Generar una variable temporal para almacenar el resultado de la operación
        temp_var = self.generate_temporary_variable()

        # Determinar el operador y generar el código de tres direcciones
        operator = ctx.ADD_OP().getText()
        code = f"{temp_var} <- {left} {operator} {right};"
        print(code)
        return temp_var
    
    def visitOutput(self, ctx: YAPLGrammarParser.OutputContext):
        expression_result = self.visit(ctx.expression())

        # Generar código de tres direcciones para la salida
        code = f"out {expression_result};"
        print(code)

    def visitExpression(self, ctx: YAPLGrammarParser.ExpressionContext):
        return self.visit(ctx.primaryExpression())
    
    def visitAssignment(self, ctx: YAPLGrammarParser.AssignmentContext):
        identifier = ctx.IDENTIFIER().getText()
        expression_result = self.visit(ctx.expression())

        # Generar una variable temporal para almacenar el resultado de la expresión
        temp_var = self.generate_temporary_variable()

        # Generar código de tres direcciones para la asignación
        code = f"{temp_var} <- {expression_result};"
        self.code.append(code)  # Agregar el código a la lista

        # Actualizar la tabla de símbolos con la nueva variable temporal
        self.symbol_table[identifier] = {"type": ctx.expression().symbol_type, "size": ctx.expression().symbol_size}

    
    def generate_temporary_variable(self):
        temp_var = f"temp_{self.temp_counter}"
        self.temp_counter += 1
        return temp_var
    
    def get_intermediate_code(self):
        return "\n".join(self.code)


    def generate_intermediate_code(code):
        lexer = YAPLGrammarLexer(InputStream(code))
        stream = CommonTokenStream(lexer)
        parser = YAPLGrammarParser(stream)
        tree = parser.program()

        visitor = SemanticAnalyzerVisitor()
        visitor.visit(tree)
        intermediate_code = visitor.get_intermediate_code()

        return intermediate_code

    def visitMethodCall(self, ctx: YAPLGrammarParser.MethodCallContext):
        # Realiza el seguimiento de las llamadas a métodos y verifica la recursividad
        method_name = ctx.IDENTIFIER().getText()
        if method_name == self.current_method or method_name == self.current_function:
            # La llamada al método/función actual dentro de sí mismo
            self.symbol_table[self.current_method]["is_recursive"] = True

    
    def visitMethodDeclaration(self, ctx: YAPLGrammarParser.MethodDeclarationContext):
        # Extraer información de la declaración de método
        method_name = ctx.methodName().getText()
        return_type = ctx.type_().getText()
        
        # Registrar el método en la tabla de símbolos
        self.symbol_table[method_name] = {
            "type": return_type,
            "class": self.current_class,  # Asociar el método con la clase actual
            "is_recursive": False  # Por defecto, no es recursivo
        }

        # Actualizar el método actual para el seguimiento de llamadas recursivas
        self.current_method = method_name

    def visitFunctionDeclaration(self, ctx: YAPLGrammarParser.FunctionDeclarationContext):
        # Extraer información de la declaración de función
        function_name = ctx.methodName().getText()
        return_type = ctx.type_().getText()
        
        # Registrar la función en la tabla de símbolos
        self.symbol_table[function_name] = {
            "type": return_type,
            "class": self.current_class,  # Asociar la función con la clase actual
            "is_recursive": False  # Por defecto, no es recursiva
        }

        # Restaurar el estado actual del método
        self.current_function = function_name


def parse_code(code):
    

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

def compile(code):
    # Example usage
    
    tree, symbol_table = parse_code(code)

    # Print the tree
    formatted_tree = format_tree(tree, indent="  ")
    #print("Árbol de Análisis Sintáctico:")
    #print(formatted_tree)
    result = []
    # Print the symbol table
    print("\nTabla de Símbolos:")
    for symbol_name, symbol_type in symbol_table.items():
        print(f"{symbol_name}: {symbol_type}")
        result.append(symbol_name + ":" + symbol_type)
    return formatted_tree, result