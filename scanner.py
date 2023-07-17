from antlr4 import *
from YAPLGrammarLexer import YAPLGrammarLexer

class YAPLGrammarScanner:
    def __init__(self):
        self.errors = []

    def scan_code(self, file_path):
        with open(file_path, "r") as file:
            code = file.read()

        lexer = YAPLGrammarLexer(InputStream(code))
        stream = CommonTokenStream(lexer)
        stream.fill()

        token_lexemes = []
        
        for token in stream.tokens:
            if token.type == -1:
                token_type = lexer.symbolicNames[-1]
                lexeme = token.text
                token_lexemes.append((token_type, lexeme))
            else:
                token_type = lexer.symbolicNames[token.type]
                lexeme = token.text
                token_lexemes.append((token_type, lexeme))

        return token_lexemes

# Example usage
file_path = "source.cl"

scanner = YAPLGrammarScanner()
token_lexemes = scanner.scan_code(file_path)
for token, lexeme in token_lexemes:
    print(f"Token: {token}\tLexeme: {lexeme}")
