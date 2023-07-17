// Generated from c:\Users\ravz2\Escritorio\lab0-compis\scanner\YAPLLexer.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPLLexerParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, INT=3, FLOAT=4, STRING=5, IDENTIFIER=6, WS=7, SEMICOLON=8, 
		COLON=9, LBRACE=10, RBRACE=11, LPAREN=12, RPAREN=13, COMMA=14, DOT=15, 
		ARROW=16, COMMENT=17, LINE_COMMENT=18;
	public static final int
		RULE_program = 0, RULE_classDeclaration = 1, RULE_className = 2, RULE_feature = 3, 
		RULE_methodFeature = 4, RULE_attributeFeature = 5, RULE_methodDeclaration = 6, 
		RULE_attributeDeclaration = 7, RULE_expression = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "classDeclaration", "className", "feature", "methodFeature", 
			"attributeFeature", "methodDeclaration", "attributeDeclaration", "expression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'inherits'", null, null, null, null, null, "';'", "':'", 
			"'{'", "'}'", "'('", "')'", "','", "'.'", "'->'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "INT", "FLOAT", "STRING", "IDENTIFIER", "WS", "SEMICOLON", 
			"COLON", "LBRACE", "RBRACE", "LPAREN", "RPAREN", "COMMA", "DOT", "ARROW", 
			"COMMENT", "LINE_COMMENT"
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
	public String getGrammarFileName() { return "YAPLLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public YAPLLexerParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public ClassDeclarationContext classDeclaration() {
			return getRuleContext(ClassDeclarationContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			classDeclaration();
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
		public List<ClassNameContext> className() {
			return getRuleContexts(ClassNameContext.class);
		}
		public ClassNameContext className(int i) {
			return getRuleContext(ClassNameContext.class,i);
		}
		public TerminalNode LBRACE() { return getToken(YAPLLexerParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(YAPLLexerParser.RBRACE, 0); }
		public TerminalNode SEMICOLON() { return getToken(YAPLLexerParser.SEMICOLON, 0); }
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
			setState(20);
			match(T__0);
			setState(21);
			className();
			setState(22);
			match(T__1);
			setState(23);
			className();
			setState(24);
			match(LBRACE);
			setState(28);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IDENTIFIER) {
				{
				{
				setState(25);
				feature();
				}
				}
				setState(30);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(31);
			match(RBRACE);
			setState(32);
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
		public TerminalNode IDENTIFIER() { return getToken(YAPLLexerParser.IDENTIFIER, 0); }
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
			setState(34);
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

	public static class FeatureContext extends ParserRuleContext {
		public MethodFeatureContext methodFeature() {
			return getRuleContext(MethodFeatureContext.class,0);
		}
		public AttributeFeatureContext attributeFeature() {
			return getRuleContext(AttributeFeatureContext.class,0);
		}
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_feature);
		try {
			setState(38);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(36);
				methodFeature();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(37);
				attributeFeature();
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

	public static class MethodFeatureContext extends ParserRuleContext {
		public MethodDeclarationContext methodDeclaration() {
			return getRuleContext(MethodDeclarationContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(YAPLLexerParser.SEMICOLON, 0); }
		public MethodFeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodFeature; }
	}

	public final MethodFeatureContext methodFeature() throws RecognitionException {
		MethodFeatureContext _localctx = new MethodFeatureContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_methodFeature);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			methodDeclaration();
			setState(41);
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

	public static class AttributeFeatureContext extends ParserRuleContext {
		public AttributeDeclarationContext attributeDeclaration() {
			return getRuleContext(AttributeDeclarationContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(YAPLLexerParser.SEMICOLON, 0); }
		public AttributeFeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attributeFeature; }
	}

	public final AttributeFeatureContext attributeFeature() throws RecognitionException {
		AttributeFeatureContext _localctx = new AttributeFeatureContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_attributeFeature);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			attributeDeclaration();
			setState(44);
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

	public static class MethodDeclarationContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(YAPLLexerParser.IDENTIFIER, 0); }
		public TerminalNode LPAREN() { return getToken(YAPLLexerParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(YAPLLexerParser.RPAREN, 0); }
		public TerminalNode COLON() { return getToken(YAPLLexerParser.COLON, 0); }
		public ClassNameContext className() {
			return getRuleContext(ClassNameContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(YAPLLexerParser.LBRACE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(YAPLLexerParser.RBRACE, 0); }
		public MethodDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodDeclaration; }
	}

	public final MethodDeclarationContext methodDeclaration() throws RecognitionException {
		MethodDeclarationContext _localctx = new MethodDeclarationContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_methodDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(IDENTIFIER);
			setState(47);
			match(LPAREN);
			setState(48);
			match(RPAREN);
			setState(49);
			match(COLON);
			setState(50);
			className();
			setState(51);
			match(LBRACE);
			setState(52);
			expression();
			setState(53);
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

	public static class AttributeDeclarationContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(YAPLLexerParser.IDENTIFIER, 0); }
		public TerminalNode COLON() { return getToken(YAPLLexerParser.COLON, 0); }
		public ClassNameContext className() {
			return getRuleContext(ClassNameContext.class,0);
		}
		public AttributeDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attributeDeclaration; }
	}

	public final AttributeDeclarationContext attributeDeclaration() throws RecognitionException {
		AttributeDeclarationContext _localctx = new AttributeDeclarationContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_attributeDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(IDENTIFIER);
			setState(56);
			match(COLON);
			setState(57);
			className();
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
		public TerminalNode STRING() { return getToken(YAPLLexerParser.STRING, 0); }
		public TerminalNode DOT() { return getToken(YAPLLexerParser.DOT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(YAPLLexerParser.IDENTIFIER, 0); }
		public TerminalNode LPAREN() { return getToken(YAPLLexerParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(YAPLLexerParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(YAPLLexerParser.SEMICOLON, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(STRING);
			setState(60);
			match(DOT);
			setState(61);
			match(IDENTIFIER);
			setState(62);
			match(LPAREN);
			setState(63);
			match(RPAREN);
			setState(64);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24E\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\7\3\35\n\3\f\3\16\3 \13\3\3\3\3\3\3\3\3\4\3\4\3\5"+
		"\3\5\5\5)\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n"+
		"\f\16\20\22\2\2\2=\2\24\3\2\2\2\4\26\3\2\2\2\6$\3\2\2\2\b(\3\2\2\2\n*"+
		"\3\2\2\2\f-\3\2\2\2\16\60\3\2\2\2\209\3\2\2\2\22=\3\2\2\2\24\25\5\4\3"+
		"\2\25\3\3\2\2\2\26\27\7\3\2\2\27\30\5\6\4\2\30\31\7\4\2\2\31\32\5\6\4"+
		"\2\32\36\7\f\2\2\33\35\5\b\5\2\34\33\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2"+
		"\36\37\3\2\2\2\37!\3\2\2\2 \36\3\2\2\2!\"\7\r\2\2\"#\7\n\2\2#\5\3\2\2"+
		"\2$%\7\b\2\2%\7\3\2\2\2&)\5\n\6\2\')\5\f\7\2(&\3\2\2\2(\'\3\2\2\2)\t\3"+
		"\2\2\2*+\5\16\b\2+,\7\n\2\2,\13\3\2\2\2-.\5\20\t\2./\7\n\2\2/\r\3\2\2"+
		"\2\60\61\7\b\2\2\61\62\7\16\2\2\62\63\7\17\2\2\63\64\7\13\2\2\64\65\5"+
		"\6\4\2\65\66\7\f\2\2\66\67\5\22\n\2\678\7\r\2\28\17\3\2\2\29:\7\b\2\2"+
		":;\7\13\2\2;<\5\6\4\2<\21\3\2\2\2=>\7\7\2\2>?\7\21\2\2?@\7\b\2\2@A\7\16"+
		"\2\2AB\7\17\2\2BC\7\n\2\2C\23\3\2\2\2\4\36(";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}