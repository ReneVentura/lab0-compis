import json
from antlr4 import *
from YAPLGrammarLexer import YAPLGrammarLexer
from YAPLGrammarParser import YAPLGrammarParser
from YAPLGrammarVisitor import YAPLGrammarVisitor

class SemanticAnalyzerVisitor(YAPLGrammarVisitor):
    def __init__(self):
        self.class_symbol_tables = {}  # Tablas de símbolos por clase        self.current_class = None
        self.inheritance_map = {}
        self.parent_class = None
        self.intermediate_code = []  # Lista para almacenar el código intermedio generado
        self.current_function_label = None
        self.current_full_function_name = None
         # Tabla de símbolos global

    def get_type_with_size(self, type_name):
        # Define default sizes for types here
        print()
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
    def generate_label(self):
        """
        Genera un nombre de etiqueta única utilizando un contador.
        Puedes personalizar este método según tus necesidades.
        """
        if not hasattr(self, "label_counter"):
            self.label_counter = 0

        label = f"Label_{self.label_counter}"
        self.label_counter += 1
        return label
    
    def generate_temporary(self):
        """
        Genera un nombre para una variable temporal única.
        Puedes personalizar este método según tus necesidades.
        """
        temp_name = f"temp_{len(self.intermediate_code)}"
        return temp_name

    # def visitVarDeclaration(self, ctx:YAPLGrammarParser.VarDeclarationContext):
    #     variable_name = ctx.IDENTIFIER().getText()
    #     expression = ctx.assignExpression()

    #     # Generar código para la expresión a la derecha de la asignación
    #     expr_code = self.visit(expression)

    #     # Agregar código intermedio para la asignación
    #     assign_temp = self.generate_temporary()
    #     assign_code = f"{assign_temp} = {expr_code}"
    #     self.intermediate_code.append(assign_code)

    #     # Actualizar la tabla de símbolos si es necesario
    #     if f"{self.current_class}.{variable_name}" in self.symbol_table:
    #         class_var = f"{self.current_class}.{variable_name}"
    #         self.symbol_table[class_var]["code"] = assign_temp
    #     else:
    #         self.symbol_table[variable_name]["code"] = assign_temp
    def visitPrimaryExpression(self, ctx: YAPLGrammarParser.PrimaryExpressionContext):
        if ctx.IDENTIFIER():
            # Si es un identificador, devuelve el nombre de la variable
            return ctx.IDENTIFIER().getText()
        elif ctx.INT_LITERAL():
            # Si es un literal entero, devuelve su valor como cadena
            return ctx.INT_LITERAL().getText()
        elif ctx.STRING_LITERAL():
            # Si es un literal de cadena, devuelve su valor como cadena
            return ctx.STRING_LITERAL().getText()
        elif ctx.boolDeclaration():
            # Si es la palabra clave 'true', devuelve "true"
            return ctx.boolDeclaration().getText()

        elif ctx.SELF():
            # Si es la palabra clave 'self', devuelve "self"
            return "self"
        elif ctx.NEW():
            # Si es la palabra clave 'new', devuelve "new"
            return "new"
        elif ctx.methodName():
            # Si es una llamada a método, devuelve el nombre del método
            method_name = ctx.methodName().getText()
            # Puedes manejar los argumentos aquí si es necesario
            # Deberías agregar el manejo de argumentos según la estructura de tu lenguaje
            return method_name

        # Agrega más casos según sea necesario para otros tipos de expresiones
        else:
            # Si ninguno de los casos anteriores coincide, maneja el caso según corresponda
            return None
    def visitIfStatement(self, ctx: YAPLGrammarParser.IfStatementContext):
        code = []

        # Genera etiquetas únicas para las instrucciones de salto
        label_then = self.generate_label()
        label_else = self.generate_label()
        label_fi = self.generate_label()

        if ctx.LET():
            # Agrega código para manejar LET si está presente
            code.append("Handle LET here")  # Reemplaza esto con el código real

        # Itera sobre las expresiones booleanas
        for bool_expr_ctx in ctx.boolExpression():
            bool_expr_code = self.visit(bool_expr_ctx)
            # Agrega el código generado para la expresión booleana a la lista de código
            code.extend(bool_expr_code)
            self.intermediate_code.extend(bool_expr_code)

        # Agrega código de salto condicional a la etiqueta "label_then" o "label_else"
        code.append(f"if {bool_expr_code} goto {label_then}")
        self.intermediate_code.append(f"if {bool_expr_code} goto {label_then}")
        code.append(f"goto {label_else}")
        self.intermediate_code.append(f"goto {label_else}")

        # Etiqueta para la rama "then"
        code.append(f"{label_then}:")
        self.intermediate_code.append(f"{label_then}:")

        # Visita y agrega los statements del bloque THEN
        then_code_list = []  # Lista para almacenar los códigos de los statements del bloque THEN
        for then_statement in ctx.statement():
            then_code = self.visit(then_statement)
            code.extend(then_code)
            self.intermediate_code.extend(then_code)  # Acumula los códigos en la lista
        print("STATEMENTS")
        print(then_code_list)

        # Agrega código de salto incondicional a la etiqueta "label_fi"
        code.append(f"goto {label_fi}")
        self.intermediate_code.append(f"goto {label_fi}")
        # Etiqueta para la rama "else"
        code.append(f"{label_else}:")
        self.intermediate_code.append(f"{label_else}:")

        # Visita bloques ELSE-IF (si están presentes)
        for i in range(1, len(ctx.boolExpression())):
            bool_expr_ctx = ctx.boolExpression(i)
            for bool_expr_ctx1 in ctx.boolExpression():
                bool_expr_code = self.visit(bool_expr_ctx1)
                # Agrega el código generado para la expresión booleana a la lista de código
                code.extend(bool_expr_code)
                self.intermediate_code.extend(bool_expr_code)
            code.append(f"if {bool_expr_code} goto {label_then}")
            self.intermediate_code.append(f"if {bool_expr_code} goto {label_then}")
            code.append(f"goto {label_else}")
            self.intermediate_code.append(f"goto {label_else}")

        # Visita y agrega los statements del bloque ELSE (si está presente)
        if ctx.ELSE():
            else_code  = self.visit(ctx.statement(len(ctx.boolExpression())))
            print("ELSE CODE")
            print(else_code)
            code.extend(else_code)
            self.intermediate_code.extend(else_code)

        # Etiqueta para el final del IF
        code.append(f"{label_fi}:")
        self.intermediate_code.append(f"{label_fi}:")
        print(code)
        return code, None

    def get_intermediate_code(self):
        """
        Método para obtener el código intermedio generado hasta el momento.
        """
        return self.intermediate_code


    def visitArithmeticExpression(self, ctx: YAPLGrammarParser.ArithmeticExpressionContext):
        # Visita la primera expresión
        left_temp = self.visit(ctx.primaryExpression(0))

        # Inicializa el código intermedio como una lista vacía
        intermediate_code = []

        # Itera a través de los operadores y las expresiones
        for i in range(1, len(ctx.primaryExpression())):
            operator = ctx.getChild(2 * (i - 1) + 1).getText()  # Obtener el operador

            right_temp = self.visit(ctx.primaryExpression(i))

            # Genera un nombre temporal para el resultado de la operación actual
            result_temp = self.generate_temporary()
            print(self.current_function_label)
            # Agrega la operación al código intermedio como una instrucción de tres direcciones
            if self.current_function_label:
                intermediate_code.append(f"{result_temp} = {left_temp} {operator} {self.current_function_label}")
                self.intermediate_code.append(f"{result_temp} = {left_temp} {operator} {self.current_function_label}")
            else:
                intermediate_code.append(f"{result_temp} = {left_temp} {operator} {right_temp}")
                self.intermediate_code.append(f"{result_temp} = {left_temp} {operator} {right_temp}")

            # Actualiza left_temp con el resultado de la operación actual
            left_temp = result_temp
        print(intermediate_code)
        # Devuelve  el último nombre temporal y el tipo (que podría ser "Int" en este caso)
        return left_temp,  intermediate_code


    def visitDeclaration(self, ctx: YAPLGrammarParser.DeclarationContext):
        method_name = ctx.IDENTIFIER().getText()
        method_type = self.get_type_with_size(ctx.type_().getText())

        if self.current_class:
             class_name = self.current_class
             self.class_symbol_tables[class_name][method_name] = {
                "type": method_type,
                "class": self.current_class,
            }
        else:
            self.symbol_table[method_name] = {
                "type": method_type,
                "class": None,
            }
    


    def visitVarDeclaration(self, ctx: YAPLGrammarParser.VarDeclarationContext):
        identifier = ctx.IDENTIFIER().getText()
        assign_code = self.visit(ctx.assignExpression())
        intermediate_code = []
        # Genera una instrucción de asignación de tres direcciones
        label_code = self.generate_label()
        assignment_code = f"{label_code} <- {assign_code};"
        
        # Agrega la instrucción de asignación al código intermedio
        self.intermediate_code.append(assignment_code)
        intermediate_code.append(assignment_code)
        print(self.intermediate_code)
        return intermediate_code
    
    def visitNewVarDeclaration(self, ctx: YAPLGrammarParser.NewVarDeclarationContext):
        identifier = ctx.IDENTIFIER().getText()
        type_ = ctx.type_().getText()
        assign_code = self.visit(ctx.assignExpression()) if ctx.assignExpression() else None
        intermediate_code = []

        # Genera una instrucción de asignación de tres direcciones
        label_code = self.generate_label()
        if assign_code is not None:
            assignment_code = f"{label_code} <- {assign_code};"
            intermediate_code.append(assignment_code)

        # Agrega la variable a la tabla de símbolos con su tipo
        if self.current_class:
            class_name = self.current_class
            self.class_symbol_tables[class_name][identifier] = {
                "type": type_,
                "class": class_name,
            }
        else:
            self.symbol_table[identifier] = {
                "type": type_,
                "class": None,
            }

        # Agrega la instrucción de declaración al código intermedio
        declaration_code = f"Declare {identifier} as {type_};"
        intermediate_code.append(declaration_code)

        # Agrega el código intermedio generado a la lista global
        self.intermediate_code.extend(intermediate_code)
        print("NEVAR")
        print(intermediate_code)
        print("NEVAR")
        return intermediate_code


    def visitClassDeclaration(self, ctx: YAPLGrammarParser.ClassDeclarationContext):
        class_name = ctx.className().getText()
        self.current_class = class_name

        if ctx.INHERITS():
            parent_class = ctx.classNameParent().getText()
            self.inheritance_map[class_name] = parent_class
            self.parent_class = parent_class
        else:
            self.parent_class = None
        self.class_symbol_tables[class_name] = {}
        self.visitChildren(ctx)
        self.current_class = None
    def visitDefineStatements(self, ctx: YAPLGrammarParser.DefineStatementsContext):
        intermediate_code = []

        # Visita cada statementList en la secuencia
        for statement_list_ctx in ctx.statementList():
            statement_list_code = self.visit(statement_list_ctx)
            
            # Agrega el código intermedio generado por el statementList actual
            if statement_list_code:
                intermediate_code.extend(statement_list_code)
                self.intermediate_code.extend(statement_list_code)
        print("VISIT STATEMENT")
        print(intermediate_code)
        print("VISIT STATEMENT")
        return intermediate_code

    def visitMethodDeclaration(self, ctx: YAPLGrammarParser.MethodDeclarationContext):
        method_name = ctx.methodName().getText()
        method_type = self.get_type_with_size(ctx.type_().getText())

        if self.current_class:
            class_name = self.current_class
            self.class_symbol_tables[class_name][method_name] = {
                "type": method_type,
                "class": self.current_class,
            }
        else:
            self.symbol_table[method_name] = {
                "type": method_type,
                "class": None,
            }

        # Establece el método actual antes de visitar el cuerpo del método
        self.current_method = method_name

        # Genera una etiqueta única para esta función
        function_label = self.generate_label()

        # Almacena el nombre de la etiqueta en la tabla de símbolos con una clave "label"
        if self.current_class:
            self.current_full_function_name = f"{self.current_class}.{method_name}"
            self.class_symbol_tables[self.current_class][method_name]["label"] = function_label
            self.current_function_label = function_label
        else:
            self.symbol_table[method_name]["label"] = function_label
            self.current_function_label = function_label

        # Inicializa el código intermedio para este método
        intermediate_code = []

        # Agrega la etiqueta de inicio de la función
        intermediate_code.append(f"{function_label}:")
        self.intermediate_code.append(f"{function_label}:")

        # Visita el cuerpo del método y obtén el código intermedio
        method_body_code = self.visit(ctx.defineStatements())

        # Agrega el código del cuerpo del método a la lista de código intermedio
        intermediate_code.extend(method_body_code)
        self.intermediate_code.extend(method_body_code)

        # Restablece el método actual después de visitar el cuerpo del método
        self.current_method = None

        # Agrega código de retorno (por ejemplo, un return implícito)
        # Esto dependerá de cómo manejas los valores de retorno en tu lenguaje
        # Puedes agregar aquí una instrucción como "return ret_variable;"

        return intermediate_code


    def visitMethodCall(self, ctx: YAPLGrammarParser.MethodCallContext):
        method_name = ctx.primaryExpression().methodName().getText()
        class_name = self.current_class
        print("current method")
        print(self.current_full_function_name)
        current_class = class_name
        while current_class:
            full_method_name = f"{current_class}.{method_name}"
            print("current method")
            print(self.current_full_function_name)
            if full_method_name in self.current_full_function_name:
                # Obtiene el nombre de la etiqueta almacenado en la tabla de símbolos
                function_label = self.symbol_table[full_method_name]["label"]
                # Aquí puedes usar function_label en el código intermedio
                return_code = f"call {function_label};"
                return return_code
            elif self.inheritance_map.get(current_class):
                parent_class = self.inheritance_map[current_class]
                full_method_name_parent = f"{parent_class}.{method_name}"
                print("current method")
                print(self.current_full_function_name)
                if full_method_name_parent in self.current_full_function_name:
                    # Obtiene el nombre de la etiqueta almacenado en la tabla de símbolos
                    function_label = self.symbol_table[full_method_name_parent]["label"]
                    # Aquí puedes usar function_label en el código intermedio
                    self.current_function_label = function_label
                    return_code = f"call {function_label};"
                    print("function label")
                    print(self.current_function_label)
                    return return_code
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
    # Obtener el código intermedio generado por el analizador semántico
    intermediate_code = visitor.get_intermediate_code()

    # Imprimir el código intermedio
    print("FSFKSLJFJS------------------")
    print()
    print()
    print(intermediate_code)
    for code_line in intermediate_code:
        print(code_line)

    return tree, visitor.class_symbol_tables,intermediate_code

def generate_mips_code(intermediate_code):
    mips_code = []
    visitor = SemanticAnalyzerVisitor()
    # Instrucción de inicio del programa MIPS
    mips_code.append(".text")
    mips_code.append("main:")
    mips_code.append("    li $v0, 10")  # Código de salida del programa
    mips_code.append("    syscall")

    for line in intermediate_code:
        parts = line.split()
        
        # Ignora las líneas vacías
        if not parts or len(parts) == 1:
            continue

        if parts[0] == 'if':
            # Traduce una instrucción condicional
            condition = parts[1]
            target_label = parts[3]
            mips_code.append(f"    beqz {condition}, {target_label}")
        elif parts[0] == 'goto':
            # Traduce una instrucción de salto incondicional
            target_label = parts[1]
            mips_code.append(f"    j {target_label}")
        elif parts[1] == '<-':
            # Traduce una instrucción de asignación
            variable = parts[0]
            value = parts[2]
            mips_code.append(f"    li $t0, {value}")
            mips_code.append(f"    sw $t0, {variable}")
        elif parts[1] == '+':
            # Traduce una instrucción de suma
            result_variable = parts[0]
            operand1 = parts[2]
            operand2 = parts[4]
            mips_code.append(f"    lw $t1, {operand1}")  # Carga el primer operando en $t1
            mips_code.append(f"    lw $t2, {operand2}")  # Carga el segundo operando en $t2
            mips_code.append(f"    add $t3, $t1, $t2")  # Realiza la suma y almacena en $t3
            mips_code.append(f"    sw $t3, {result_variable}")  # Almacena el resultado en la variable
        elif parts[1] == '*':
            # Traduce una instrucción de multiplicación
            result_variable = parts[0]
            operand1 = parts[2]
            operand2 = parts[4]
            mips_code.append(f"    lw $t1, {operand1}")  # Carga el primer operando en $t1
            mips_code.append(f"    lw $t2, {operand2}")  # Carga el segundo operando en $t2
            mips_code.append(f"    mul $t3, $t1, $t2")  # Realiza la multiplicación y almacena en $t3
            mips_code.append(f"    sw $t3, {result_variable}")  # Almacena el resultado en la variable
        elif parts[0] == 'Declare':
            # Traduce una declaración de variable
            variable_name = parts[1]
            variable_type = parts[3]  # Suponiendo que el tipo de variable está presente en el código intermedio
            print(variable_type)
            # Obtén el tamaño del tipo de variable desde tu función get_type_with_size
            variable_size = visitor.get_type_with_size(variable_type)
            print(variable_size)
            # Reserva espacio en la memoria para la variable según su tamaño
            mips_code.append(f"    li $t0, {variable_size}")  # Carga el tamaño en $t0
            mips_code.append(f"    li $v0, 9")  # Código para reservar memoria
            mips_code.append(f"    syscall")  # Llama al sistema para reservar memoria
            mips_code.append(f"    move $s0, $v0")  # Guarda la dirección de memoria en $s0

            # Asigna el valor inicial a la variable según su tipo y tamaño
            if variable_type == 'Int':
                # Para una variable de tipo Int, asigna el valor 0
                mips_code.append(f"    li $t1, 0")
            elif variable_type == 'String':
                # Para una variable de tipo String, puedes asignar un valor predeterminado adecuado
                # Aquí asumimos que la dirección de memoria del valor inicial de String está en $t1
                mips_code.append(f"    la $t1, initial_string_value")
            else:
                # Para otros tipos de variables, agrega la lógica correspondiente
                # Puedes personalizar esto según los tipos de datos admitidos en tu lenguaje
                pass

            # Almacena el valor inicial en la dirección de memoria reservada
            mips_code.append(f"    sw $t1, 0($s0)")  # Almacena el valor en la dirección de memoria

            # Asigna la dirección de memoria de la variable a su nombre en la tabla de símbolos
            # Esto puede variar según cómo estés gestionando las variables en tu compilador
           


    # Instrucción de finalización del programa MIPS
    mips_code.append("    li $v0, 10")  # Código de salida del programa
    mips_code.append("    syscall")
    
    return mips_code

def format_tree(node, indent=""):
    if isinstance(node, TerminalNode):
        return indent + node.getText()

    result = indent + type(node).__name__ + "\n"
    for child in node.getChildren():
        result += format_tree(child, indent + "  ") + "\n"
    return result

def compile(code):
    tree, symbol_table, intermediate_code = parse_code(code)
    formatted_tree = format_tree(tree, indent="  ")
  #  print(formatted_tree)
    print("\nTabla de Símbolos:")
    for symbol_name, symbol_type in symbol_table.items():
        print(f"{symbol_name}: {symbol_type}")
    mips_assembly = generate_mips_code(intermediate_code)

# Imprime el código MIPS resultante
    print(mips_assembly)
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


