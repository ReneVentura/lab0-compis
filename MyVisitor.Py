from YAPLGrammarVisitor import YAPLGrammarVisitor
from SymbolTable import SymbolTable  # Importa la clase SymbolTable creada anteriormente

class MyVisitor(YAPLGrammarVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()  # Crea una instancia de la tabla de símbolos
        self.current_class = None  # Variable para mantener el contexto de la clase actual

    # Implementa los métodos de visita para cada regla gramatical que necesites

    def visitClassDeclaration(self, ctx):
        class_name = ctx.className().getText()
        self.current_class = class_name  # Establece la clase actual
        self.symbol_table.add_symbol('class', class_name, 'class')  # Agrega la clase a la tabla de símbolos
        return super().visitClassDeclaration(ctx)

    def visitVarDeclaration(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        var_type = ctx.type().getText()
        self.symbol_table.add_symbol(self.current_class, var_name, var_type)  # Agrega la variable a la tabla de símbolos
        return super().visitVarDeclaration(ctx)

    def visitMethodDeclaration(self, ctx):
        method_name = ctx.methodName().getText()
        method_type = ctx.type().getText()
        self.symbol_table.add_symbol(self.current_class, method_name, method_type)  # Agrega el método a la tabla de símbolos
        return super().visitMethodDeclaration(ctx)

    # Implementa otros métodos de visita para las reglas restantes según tus necesidades.

    # Por ejemplo, puedes implementar métodos para manejar el alcance de las variables,
    # resolver nombres en la tabla de símbolos, etc.

    # Otras acciones semánticas utilizando self.symbol_table
    # Añade aquí otras acciones para consultar símbolos, manejar ámbitos, etc.
