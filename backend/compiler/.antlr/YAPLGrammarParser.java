// Generated from c:\Users\ravz2\Escritorio\lab0-compis-1\backend\compiler\YAPLGrammar.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPLGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CLASS=1, INHERITS=2, LPAREN=3, RPAREN=4, LBRACE=5, MINUS=6, RBRACE=7, 
		COLON=8, SEMICOLON=9, ASSIGN=10, INT=11, STRING=12, SELF=13, IF=14, THEN=15, 
		ELSE=16, LESS_THAN=17, GREAT_THAN=18, EQUALS=19, PLUS=20, MULT=21, DIV=22, 
		NEW=23, COMMA=24, IN=25, DOT=26, LET=27, OUT=28, UNDERSCORE=29, IDENTIFIER=30, 
		INT_LITERAL=31, STRING_LITERAL=32, WS=33, COMMENT=34, ERROR=35;
	public static final int
		RULE_program = 0, RULE_classDeclaration = 1, RULE_className = 2, RULE_methodName = 3, 
		RULE_type = 4, RULE_variable = 5, RULE_parameterCall = 6, RULE_primaryExpression = 7, 
		RULE_expression = 8, RULE_arithmeticExpression = 9, RULE_boolExpression = 10, 
		RULE_assignExpression = 11, RULE_declaration = 12, RULE_newVarDeclaration = 13, 
		RULE_varDeclaration = 14, RULE_letDeclaration = 15, RULE_methodCall = 16, 
		RULE_statement = 17, RULE_assignStatement = 18, RULE_ifStatement = 19, 
		RULE_statementList = 20, RULE_defineStatements = 21, RULE_formalParameter = 22, 
		RULE_parameterList = 23, RULE_methodDeclaration = 24, RULE_feature = 25;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "classDeclaration", "className", "methodName", "type", "variable", 
			"parameterCall", "primaryExpression", "expression", "arithmeticExpression", 
			"boolExpression", "assignExpression", "declaration", "newVarDeclaration", 
			"varDeclaration", "letDeclaration", "methodCall", "statement", "assignStatement", 
			"ifStatement", "statementList", "defineStatements", "formalParameter", 
			"parameterList", "methodDeclaration", "feature"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'inherits'", "'('", "')'", "'{'", "'-'", "'}'", "':'", 
			"';'", "'<-'", "'Int'", "'String'", "'self'", "'if'", "'then'", "'else'", 
			"'<'", "'>'", "'='", "'+'", "'*'", "'/'", "'new'", "','", "'in'", "'.'", 
			"'let'", "'out'", "'_'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CLASS", "INHERITS", "LPAREN", "RPAREN", "LBRACE", "MINUS", "RBRACE", 
			"COLON", "SEMICOLON", "ASSIGN", "INT", "STRING", "SELF", "IF", "THEN", 
			"ELSE", "LESS_THAN", "GREAT_THAN", "EQUALS", "PLUS", "MULT", "DIV", "NEW", 
			"COMMA", "IN", "DOT", "LET", "OUT", "UNDERSCORE", "IDENTIFIER", "INT_LITERAL", 
			"STRING_LITERAL", "WS", "COMMENT", "ERROR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "YAPLGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public YAPLGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public List<ClassDeclarationContext> classDeclaration() {
			return getRuleContexts(ClassDeclarationContext.class);
		}
		public ClassDeclarationContext classDeclaration(int i) {
			return getRuleContext(ClassDeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(52);
				classDeclaration();
				}
				}
				setState(55); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CLASS );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassDeclarationContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(YAPLGrammarParser.CLASS, 0); }
		public List<ClassNameContext> className() {
			return getRuleContexts(ClassNameContext.class);
		}
		public ClassNameContext className(int i) {
			return getRuleContext(ClassNameContext.class,i);
		}
		public TerminalNode LBRACE() { return getToken(YAPLGrammarParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(YAPLGrammarParser.RBRACE, 0); }
		public TerminalNode SEMICOLON() { return getToken(YAPLGrammarParser.SEMICOLON, 0); }
		public TerminalNode INHERITS() { return getToken(YAPLGrammarParser.INHERITS, 0); }
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
		public ClassDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDeclaration; }
	}

	public final ClassDeclarationContext classDeclaration() throws RecognitionException {
		ClassDeclarationContext _localctx = new ClassDeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_classDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(CLASS);
			setState(58);
			className();
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INHERITS) {
				{
				setState(59);
				match(INHERITS);
				setState(60);
				className();
				}
			}

			setState(63);
			match(LBRACE);
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NEW) | (1L << LET) | (1L << IDENTIFIER) | (1L << INT_LITERAL) | (1L << STRING_LITERAL))) != 0)) {
				{
				{
				setState(64);
				feature();
				}
				}
				setState(69);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(70);
			match(RBRACE);
			setState(71);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(YAPLGrammarParser.IDENTIFIER, 0); }
		public ClassNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_className; }
	}

	public final ClassNameContext className() throws RecognitionException {
		ClassNameContext _localctx = new ClassNameContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_className);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MethodNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(YAPLGrammarParser.IDENTIFIER, 0); }
		public MethodNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodName; }
	}

	public final MethodNameContext methodName() throws RecognitionException {
		MethodNameContext _localctx = new MethodNameContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_methodName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(YAPLGrammarParser.INT, 0); }
		public TerminalNode STRING() { return getToken(YAPLGrammarParser.STRING, 0); }
		public ClassNameContext className() {
			return getRuleContext(ClassNameContext.class,0);
		}
		public TerminalNode SELF() { return getToken(YAPLGrammarParser.SELF, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_type);
		try {
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				match(INT);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				match(STRING);
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 3);
				{
				setState(79);
				className();
				}
				break;
			case SELF:
				enterOuterAlt(_localctx, 4);
				{
				setState(80);
				match(SELF);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public TerminalNode LET() { return getToken(YAPLGrammarParser.LET, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(LET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParameterCallContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(YAPLGrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YAPLGrammarParser.COMMA, i);
		}
		public ParameterCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterCall; }
	}

	public final ParameterCallContext parameterCall() throws RecognitionException {
		ParameterCallContext _localctx = new ParameterCallContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_parameterCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			expression();
			setState(90);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(86);
				match(COMMA);
				setState(87);
				expression();
				}
				}
				setState(92);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrimaryExpressionContext extends ParserRuleContext {
		public TerminalNode INT_LITERAL() { return getToken(YAPLGrammarParser.INT_LITERAL, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(YAPLGrammarParser.STRING_LITERAL, 0); }
		public TerminalNode IDENTIFIER() { return getToken(YAPLGrammarParser.IDENTIFIER, 0); }
		public TerminalNode NEW() { return getToken(YAPLGrammarParser.NEW, 0); }
		public ClassNameContext className() {
			return getRuleContext(ClassNameContext.class,0);
		}
		public MethodNameContext methodName() {
			return getRuleContext(MethodNameContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(YAPLGrammarParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(YAPLGrammarParser.RPAREN, 0); }
		public ParameterCallContext parameterCall() {
			return getRuleContext(ParameterCallContext.class,0);
		}
		public PrimaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpression; }
	}

	public final PrimaryExpressionContext primaryExpression() throws RecognitionException {
		PrimaryExpressionContext _localctx = new PrimaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_primaryExpression);
		int _la;
		try {
			setState(105);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(93);
				match(INT_LITERAL);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(94);
				match(STRING_LITERAL);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(95);
				match(IDENTIFIER);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(96);
				match(NEW);
				setState(97);
				className();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(98);
				methodName();
				setState(99);
				match(LPAREN);
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NEW) | (1L << IDENTIFIER) | (1L << INT_LITERAL) | (1L << STRING_LITERAL))) != 0)) {
					{
					setState(100);
					parameterCall();
					}
				}

				setState(103);
				match(RPAREN);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public ArithmeticExpressionContext arithmeticExpression() {
			return getRuleContext(ArithmeticExpressionContext.class,0);
		}
		public MethodCallContext methodCall() {
			return getRuleContext(MethodCallContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expression);
		try {
			setState(110);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(107);
				primaryExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(108);
				arithmeticExpression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(109);
				methodCall();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArithmeticExpressionContext extends ParserRuleContext {
		public List<PrimaryExpressionContext> primaryExpression() {
			return getRuleContexts(PrimaryExpressionContext.class);
		}
		public PrimaryExpressionContext primaryExpression(int i) {
			return getRuleContext(PrimaryExpressionContext.class,i);
		}
		public TerminalNode MINUS() { return getToken(YAPLGrammarParser.MINUS, 0); }
		public TerminalNode MULT() { return getToken(YAPLGrammarParser.MULT, 0); }
		public TerminalNode PLUS() { return getToken(YAPLGrammarParser.PLUS, 0); }
		public TerminalNode DIV() { return getToken(YAPLGrammarParser.DIV, 0); }
		public ArithmeticExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithmeticExpression; }
	}

	public final ArithmeticExpressionContext arithmeticExpression() throws RecognitionException {
		ArithmeticExpressionContext _localctx = new ArithmeticExpressionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_arithmeticExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			primaryExpression();
			setState(113);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MINUS) | (1L << PLUS) | (1L << MULT) | (1L << DIV))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(114);
			primaryExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BoolExpressionContext extends ParserRuleContext {
		public List<PrimaryExpressionContext> primaryExpression() {
			return getRuleContexts(PrimaryExpressionContext.class);
		}
		public PrimaryExpressionContext primaryExpression(int i) {
			return getRuleContext(PrimaryExpressionContext.class,i);
		}
		public TerminalNode EQUALS() { return getToken(YAPLGrammarParser.EQUALS, 0); }
		public TerminalNode LESS_THAN() { return getToken(YAPLGrammarParser.LESS_THAN, 0); }
		public TerminalNode GREAT_THAN() { return getToken(YAPLGrammarParser.GREAT_THAN, 0); }
		public BoolExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boolExpression; }
	}

	public final BoolExpressionContext boolExpression() throws RecognitionException {
		BoolExpressionContext _localctx = new BoolExpressionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_boolExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			primaryExpression();
			setState(117);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS_THAN) | (1L << GREAT_THAN) | (1L << EQUALS))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(118);
			primaryExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignExpressionContext extends ParserRuleContext {
		public TerminalNode ASSIGN() { return getToken(YAPLGrammarParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignExpression; }
	}

	public final AssignExpressionContext assignExpression() throws RecognitionException {
		AssignExpressionContext _localctx = new AssignExpressionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_assignExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(ASSIGN);
			setState(121);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(YAPLGrammarParser.IDENTIFIER, 0); }
		public TerminalNode COLON() { return getToken(YAPLGrammarParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode LET() { return getToken(YAPLGrammarParser.LET, 0); }
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LET) {
				{
				setState(123);
				match(LET);
				}
			}

			setState(126);
			match(IDENTIFIER);
			setState(127);
			match(COLON);
			setState(128);
			type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NewVarDeclarationContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public AssignExpressionContext assignExpression() {
			return getRuleContext(AssignExpressionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(YAPLGrammarParser.SEMICOLON, 0); }
		public NewVarDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_newVarDeclaration; }
	}

	public final NewVarDeclarationContext newVarDeclaration() throws RecognitionException {
		NewVarDeclarationContext _localctx = new NewVarDeclarationContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_newVarDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			declaration();
			setState(132);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN) {
				{
				setState(131);
				assignExpression();
				}
			}

			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(134);
				match(SEMICOLON);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarDeclarationContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(YAPLGrammarParser.IDENTIFIER, 0); }
		public AssignExpressionContext assignExpression() {
			return getRuleContext(AssignExpressionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(YAPLGrammarParser.SEMICOLON, 0); }
		public VarDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclaration; }
	}

	public final VarDeclarationContext varDeclaration() throws RecognitionException {
		VarDeclarationContext _localctx = new VarDeclarationContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_varDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(IDENTIFIER);
			setState(138);
			assignExpression();
			setState(140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(139);
				match(SEMICOLON);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LetDeclarationContext extends ParserRuleContext {
		public TerminalNode LET() { return getToken(YAPLGrammarParser.LET, 0); }
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public TerminalNode IN() { return getToken(YAPLGrammarParser.IN, 0); }
		public LetDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letDeclaration; }
	}

	public final LetDeclarationContext letDeclaration() throws RecognitionException {
		LetDeclarationContext _localctx = new LetDeclarationContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_letDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			match(LET);
			setState(143);
			declaration();
			setState(144);
			match(IN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MethodCallContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(YAPLGrammarParser.IDENTIFIER, 0); }
		public TerminalNode DOT() { return getToken(YAPLGrammarParser.DOT, 0); }
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public MethodCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodCall; }
	}

	public final MethodCallContext methodCall() throws RecognitionException {
		MethodCallContext _localctx = new MethodCallContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_methodCall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			match(IDENTIFIER);
			setState(147);
			match(DOT);
			setState(148);
			primaryExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public AssignStatementContext assignStatement() {
			return getRuleContext(AssignStatementContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_statement);
		try {
			setState(152);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				assignStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				expression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignStatementContext extends ParserRuleContext {
		public NewVarDeclarationContext newVarDeclaration() {
			return getRuleContext(NewVarDeclarationContext.class,0);
		}
		public VarDeclarationContext varDeclaration() {
			return getRuleContext(VarDeclarationContext.class,0);
		}
		public AssignStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignStatement; }
	}

	public final AssignStatementContext assignStatement() throws RecognitionException {
		AssignStatementContext _localctx = new AssignStatementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_assignStatement);
		try {
			setState(156);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(154);
				newVarDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(155);
				varDeclaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfStatementContext extends ParserRuleContext {
		public LetDeclarationContext letDeclaration() {
			return getRuleContext(LetDeclarationContext.class,0);
		}
		public List<TerminalNode> IF() { return getTokens(YAPLGrammarParser.IF); }
		public TerminalNode IF(int i) {
			return getToken(YAPLGrammarParser.IF, i);
		}
		public List<BoolExpressionContext> boolExpression() {
			return getRuleContexts(BoolExpressionContext.class);
		}
		public BoolExpressionContext boolExpression(int i) {
			return getRuleContext(BoolExpressionContext.class,i);
		}
		public List<TerminalNode> THEN() { return getTokens(YAPLGrammarParser.THEN); }
		public TerminalNode THEN(int i) {
			return getToken(YAPLGrammarParser.THEN, i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<TerminalNode> ELSE() { return getTokens(YAPLGrammarParser.ELSE); }
		public TerminalNode ELSE(int i) {
			return getToken(YAPLGrammarParser.ELSE, i);
		}
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_ifStatement);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			letDeclaration();
			setState(159);
			match(IF);
			setState(160);
			boolExpression();
			setState(161);
			match(THEN);
			setState(162);
			statement();
			setState(171);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(163);
					match(ELSE);
					setState(164);
					match(IF);
					setState(165);
					boolExpression();
					setState(166);
					match(THEN);
					setState(167);
					statement();
					}
					} 
				}
				setState(173);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			}
			setState(176);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(174);
				match(ELSE);
				setState(175);
				statement();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementListContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public StatementListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statementList; }
	}

	public final StatementListContext statementList() throws RecognitionException {
		StatementListContext _localctx = new StatementListContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_statementList);
		try {
			setState(180);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(178);
				statement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(179);
				ifStatement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DefineStatementsContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(YAPLGrammarParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(YAPLGrammarParser.RBRACE, 0); }
		public List<StatementListContext> statementList() {
			return getRuleContexts(StatementListContext.class);
		}
		public StatementListContext statementList(int i) {
			return getRuleContext(StatementListContext.class,i);
		}
		public DefineStatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defineStatements; }
	}

	public final DefineStatementsContext defineStatements() throws RecognitionException {
		DefineStatementsContext _localctx = new DefineStatementsContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_defineStatements);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(LBRACE);
			setState(184); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(183);
				statementList();
				}
				}
				setState(186); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NEW) | (1L << LET) | (1L << IDENTIFIER) | (1L << INT_LITERAL) | (1L << STRING_LITERAL))) != 0) );
			setState(188);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormalParameterContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public FormalParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formalParameter; }
	}

	public final FormalParameterContext formalParameter() throws RecognitionException {
		FormalParameterContext _localctx = new FormalParameterContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_formalParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			declaration();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParameterListContext extends ParserRuleContext {
		public List<FormalParameterContext> formalParameter() {
			return getRuleContexts(FormalParameterContext.class);
		}
		public FormalParameterContext formalParameter(int i) {
			return getRuleContext(FormalParameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(YAPLGrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YAPLGrammarParser.COMMA, i);
		}
		public ParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterList; }
	}

	public final ParameterListContext parameterList() throws RecognitionException {
		ParameterListContext _localctx = new ParameterListContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_parameterList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			formalParameter();
			setState(197);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(193);
				match(COMMA);
				setState(194);
				formalParameter();
				}
				}
				setState(199);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MethodDeclarationContext extends ParserRuleContext {
		public MethodNameContext methodName() {
			return getRuleContext(MethodNameContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(YAPLGrammarParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(YAPLGrammarParser.RPAREN, 0); }
		public TerminalNode COLON() { return getToken(YAPLGrammarParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(YAPLGrammarParser.LBRACE, 0); }
		public DefineStatementsContext defineStatements() {
			return getRuleContext(DefineStatementsContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(YAPLGrammarParser.RBRACE, 0); }
		public TerminalNode SEMICOLON() { return getToken(YAPLGrammarParser.SEMICOLON, 0); }
		public ParameterListContext parameterList() {
			return getRuleContext(ParameterListContext.class,0);
		}
		public MethodDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodDeclaration; }
	}

	public final MethodDeclarationContext methodDeclaration() throws RecognitionException {
		MethodDeclarationContext _localctx = new MethodDeclarationContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_methodDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			methodName();
			setState(201);
			match(LPAREN);
			setState(203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LET || _la==IDENTIFIER) {
				{
				setState(202);
				parameterList();
				}
			}

			setState(205);
			match(RPAREN);
			setState(206);
			match(COLON);
			setState(207);
			type();
			setState(208);
			match(LBRACE);
			setState(209);
			defineStatements();
			setState(210);
			match(RBRACE);
			setState(211);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FeatureContext extends ParserRuleContext {
		public StatementListContext statementList() {
			return getRuleContext(StatementListContext.class,0);
		}
		public MethodDeclarationContext methodDeclaration() {
			return getRuleContext(MethodDeclarationContext.class,0);
		}
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_feature);
		try {
			setState(215);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(213);
				statementList();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(214);
				methodDeclaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%\u00dc\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\3\2\6\28\n\2\r\2\16\29\3\3\3\3\3\3\3\3\5\3@\n\3\3"+
		"\3\3\3\7\3D\n\3\f\3\16\3G\13\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6"+
		"\3\6\5\6T\n\6\3\7\3\7\3\b\3\b\3\b\7\b[\n\b\f\b\16\b^\13\b\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\5\th\n\t\3\t\3\t\5\tl\n\t\3\n\3\n\3\n\5\nq\n\n\3"+
		"\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\5\16\177\n\16\3\16"+
		"\3\16\3\16\3\16\3\17\3\17\5\17\u0087\n\17\3\17\5\17\u008a\n\17\3\20\3"+
		"\20\3\20\5\20\u008f\n\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23"+
		"\3\23\5\23\u009b\n\23\3\24\3\24\5\24\u009f\n\24\3\25\3\25\3\25\3\25\3"+
		"\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00ac\n\25\f\25\16\25\u00af\13"+
		"\25\3\25\3\25\5\25\u00b3\n\25\3\26\3\26\5\26\u00b7\n\26\3\27\3\27\6\27"+
		"\u00bb\n\27\r\27\16\27\u00bc\3\27\3\27\3\30\3\30\3\31\3\31\3\31\7\31\u00c6"+
		"\n\31\f\31\16\31\u00c9\13\31\3\32\3\32\3\32\5\32\u00ce\n\32\3\32\3\32"+
		"\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\5\33\u00da\n\33\3\33\2\2\34\2"+
		"\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\2\4\4\2\b\b\26"+
		"\30\3\2\23\25\2\u00dc\2\67\3\2\2\2\4;\3\2\2\2\6K\3\2\2\2\bM\3\2\2\2\n"+
		"S\3\2\2\2\fU\3\2\2\2\16W\3\2\2\2\20k\3\2\2\2\22p\3\2\2\2\24r\3\2\2\2\26"+
		"v\3\2\2\2\30z\3\2\2\2\32~\3\2\2\2\34\u0084\3\2\2\2\36\u008b\3\2\2\2 \u0090"+
		"\3\2\2\2\"\u0094\3\2\2\2$\u009a\3\2\2\2&\u009e\3\2\2\2(\u00a0\3\2\2\2"+
		"*\u00b6\3\2\2\2,\u00b8\3\2\2\2.\u00c0\3\2\2\2\60\u00c2\3\2\2\2\62\u00ca"+
		"\3\2\2\2\64\u00d9\3\2\2\2\668\5\4\3\2\67\66\3\2\2\289\3\2\2\29\67\3\2"+
		"\2\29:\3\2\2\2:\3\3\2\2\2;<\7\3\2\2<?\5\6\4\2=>\7\4\2\2>@\5\6\4\2?=\3"+
		"\2\2\2?@\3\2\2\2@A\3\2\2\2AE\7\7\2\2BD\5\64\33\2CB\3\2\2\2DG\3\2\2\2E"+
		"C\3\2\2\2EF\3\2\2\2FH\3\2\2\2GE\3\2\2\2HI\7\t\2\2IJ\7\13\2\2J\5\3\2\2"+
		"\2KL\7 \2\2L\7\3\2\2\2MN\7 \2\2N\t\3\2\2\2OT\7\r\2\2PT\7\16\2\2QT\5\6"+
		"\4\2RT\7\17\2\2SO\3\2\2\2SP\3\2\2\2SQ\3\2\2\2SR\3\2\2\2T\13\3\2\2\2UV"+
		"\7\35\2\2V\r\3\2\2\2W\\\5\22\n\2XY\7\32\2\2Y[\5\22\n\2ZX\3\2\2\2[^\3\2"+
		"\2\2\\Z\3\2\2\2\\]\3\2\2\2]\17\3\2\2\2^\\\3\2\2\2_l\7!\2\2`l\7\"\2\2a"+
		"l\7 \2\2bc\7\31\2\2cl\5\6\4\2de\5\b\5\2eg\7\5\2\2fh\5\16\b\2gf\3\2\2\2"+
		"gh\3\2\2\2hi\3\2\2\2ij\7\6\2\2jl\3\2\2\2k_\3\2\2\2k`\3\2\2\2ka\3\2\2\2"+
		"kb\3\2\2\2kd\3\2\2\2l\21\3\2\2\2mq\5\20\t\2nq\5\24\13\2oq\5\"\22\2pm\3"+
		"\2\2\2pn\3\2\2\2po\3\2\2\2q\23\3\2\2\2rs\5\20\t\2st\t\2\2\2tu\5\20\t\2"+
		"u\25\3\2\2\2vw\5\20\t\2wx\t\3\2\2xy\5\20\t\2y\27\3\2\2\2z{\7\f\2\2{|\5"+
		"\22\n\2|\31\3\2\2\2}\177\7\35\2\2~}\3\2\2\2~\177\3\2\2\2\177\u0080\3\2"+
		"\2\2\u0080\u0081\7 \2\2\u0081\u0082\7\n\2\2\u0082\u0083\5\n\6\2\u0083"+
		"\33\3\2\2\2\u0084\u0086\5\32\16\2\u0085\u0087\5\30\r\2\u0086\u0085\3\2"+
		"\2\2\u0086\u0087\3\2\2\2\u0087\u0089\3\2\2\2\u0088\u008a\7\13\2\2\u0089"+
		"\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\35\3\2\2\2\u008b\u008c\7 \2\2"+
		"\u008c\u008e\5\30\r\2\u008d\u008f\7\13\2\2\u008e\u008d\3\2\2\2\u008e\u008f"+
		"\3\2\2\2\u008f\37\3\2\2\2\u0090\u0091\7\35\2\2\u0091\u0092\5\32\16\2\u0092"+
		"\u0093\7\33\2\2\u0093!\3\2\2\2\u0094\u0095\7 \2\2\u0095\u0096\7\34\2\2"+
		"\u0096\u0097\5\20\t\2\u0097#\3\2\2\2\u0098\u009b\5&\24\2\u0099\u009b\5"+
		"\22\n\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b%\3\2\2\2\u009c\u009f"+
		"\5\34\17\2\u009d\u009f\5\36\20\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2"+
		"\2\u009f\'\3\2\2\2\u00a0\u00a1\5 \21\2\u00a1\u00a2\7\20\2\2\u00a2\u00a3"+
		"\5\26\f\2\u00a3\u00a4\7\21\2\2\u00a4\u00ad\5$\23\2\u00a5\u00a6\7\22\2"+
		"\2\u00a6\u00a7\7\20\2\2\u00a7\u00a8\5\26\f\2\u00a8\u00a9\7\21\2\2\u00a9"+
		"\u00aa\5$\23\2\u00aa\u00ac\3\2\2\2\u00ab\u00a5\3\2\2\2\u00ac\u00af\3\2"+
		"\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b2\3\2\2\2\u00af"+
		"\u00ad\3\2\2\2\u00b0\u00b1\7\22\2\2\u00b1\u00b3\5$\23\2\u00b2\u00b0\3"+
		"\2\2\2\u00b2\u00b3\3\2\2\2\u00b3)\3\2\2\2\u00b4\u00b7\5$\23\2\u00b5\u00b7"+
		"\5(\25\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7+\3\2\2\2\u00b8"+
		"\u00ba\7\7\2\2\u00b9\u00bb\5*\26\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3\2"+
		"\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be"+
		"\u00bf\7\t\2\2\u00bf-\3\2\2\2\u00c0\u00c1\5\32\16\2\u00c1/\3\2\2\2\u00c2"+
		"\u00c7\5.\30\2\u00c3\u00c4\7\32\2\2\u00c4\u00c6\5.\30\2\u00c5\u00c3\3"+
		"\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8"+
		"\61\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cb\5\b\5\2\u00cb\u00cd\7\5\2"+
		"\2\u00cc\u00ce\5\60\31\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce"+
		"\u00cf\3\2\2\2\u00cf\u00d0\7\6\2\2\u00d0\u00d1\7\n\2\2\u00d1\u00d2\5\n"+
		"\6\2\u00d2\u00d3\7\7\2\2\u00d3\u00d4\5,\27\2\u00d4\u00d5\7\t\2\2\u00d5"+
		"\u00d6\7\13\2\2\u00d6\63\3\2\2\2\u00d7\u00da\5*\26\2\u00d8\u00da\5\62"+
		"\32\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da\65\3\2\2\2\279?ES"+
		"\\gkp~\u0086\u0089\u008e\u009a\u009e\u00ad\u00b2\u00b6\u00bc\u00c7\u00cd"+
		"\u00d9";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}