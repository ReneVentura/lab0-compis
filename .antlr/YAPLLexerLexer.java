// Generated from c:\Users\ravz2\Escritorio\lab0-compis\scanner\Grammar.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPLLexerLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, INT=3, FLOAT=4, STRING=5, IDENTIFIER=6, WS=7, SEMICOLON=8, 
		COLON=9, LBRACE=10, RBRACE=11, LPAREN=12, RPAREN=13, COMMA=14, DOT=15, 
		ARROW=16, COMMENT=17, LINE_COMMENT=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "INT", "FLOAT", "STRING", "IDENTIFIER", "WS", "SEMICOLON", 
			"COLON", "LBRACE", "RBRACE", "LPAREN", "RPAREN", "COMMA", "DOT", "ARROW", 
			"COMMENT", "LINE_COMMENT"
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


	public YAPLLexerLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Grammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24\u0089\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\4\6\48\n\4\r\4\16\49\3\5\6\5=\n\5\r\5\16\5>\3\5\3\5\6\5C\n\5"+
		"\r\5\16\5D\3\6\3\6\7\6I\n\6\f\6\16\6L\13\6\3\6\3\6\3\7\3\7\7\7R\n\7\f"+
		"\7\16\7U\13\7\3\b\6\bX\n\b\r\b\16\bY\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13"+
		"\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22\3\22"+
		"\3\22\3\22\7\22u\n\22\f\22\16\22x\13\22\3\22\3\22\3\22\3\22\3\22\3\23"+
		"\3\23\3\23\3\23\7\23\u0083\n\23\f\23\16\23\u0086\13\23\3\23\3\23\3v\2"+
		"\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35"+
		"\20\37\21!\22#\23%\24\3\2\b\3\2\62;\5\2\f\f\17\17$$\5\2C\\aac|\6\2\62"+
		";C\\aac|\5\2\13\f\17\17\"\"\4\2\f\f\17\17\2\u0090\2\3\3\2\2\2\2\5\3\2"+
		"\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21"+
		"\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2"+
		"\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3"+
		"\2\2\2\5-\3\2\2\2\7\67\3\2\2\2\t<\3\2\2\2\13F\3\2\2\2\rO\3\2\2\2\17W\3"+
		"\2\2\2\21]\3\2\2\2\23_\3\2\2\2\25a\3\2\2\2\27c\3\2\2\2\31e\3\2\2\2\33"+
		"g\3\2\2\2\35i\3\2\2\2\37k\3\2\2\2!m\3\2\2\2#p\3\2\2\2%~\3\2\2\2\'(\7e"+
		"\2\2()\7n\2\2)*\7c\2\2*+\7u\2\2+,\7u\2\2,\4\3\2\2\2-.\7k\2\2./\7p\2\2"+
		"/\60\7j\2\2\60\61\7g\2\2\61\62\7t\2\2\62\63\7k\2\2\63\64\7v\2\2\64\65"+
		"\7u\2\2\65\6\3\2\2\2\668\t\2\2\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\29"+
		":\3\2\2\2:\b\3\2\2\2;=\t\2\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2"+
		"?@\3\2\2\2@B\7\60\2\2AC\t\2\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2"+
		"\2E\n\3\2\2\2FJ\7$\2\2GI\n\3\2\2HG\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2"+
		"\2KM\3\2\2\2LJ\3\2\2\2MN\7$\2\2N\f\3\2\2\2OS\t\4\2\2PR\t\5\2\2QP\3\2\2"+
		"\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\16\3\2\2\2US\3\2\2\2VX\t\6\2\2WV\3\2"+
		"\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\b\b\2\2\\\20\3\2\2\2]"+
		"^\7=\2\2^\22\3\2\2\2_`\7<\2\2`\24\3\2\2\2ab\7}\2\2b\26\3\2\2\2cd\7\177"+
		"\2\2d\30\3\2\2\2ef\7*\2\2f\32\3\2\2\2gh\7+\2\2h\34\3\2\2\2ij\7.\2\2j\36"+
		"\3\2\2\2kl\7\60\2\2l \3\2\2\2mn\7/\2\2no\7@\2\2o\"\3\2\2\2pq\7\61\2\2"+
		"qr\7,\2\2rv\3\2\2\2su\13\2\2\2ts\3\2\2\2ux\3\2\2\2vw\3\2\2\2vt\3\2\2\2"+
		"wy\3\2\2\2xv\3\2\2\2yz\7,\2\2z{\7\61\2\2{|\3\2\2\2|}\b\22\2\2}$\3\2\2"+
		"\2~\177\7\61\2\2\177\u0080\7\61\2\2\u0080\u0084\3\2\2\2\u0081\u0083\n"+
		"\7\2\2\u0082\u0081\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2\u0084"+
		"\u0085\3\2\2\2\u0085\u0087\3\2\2\2\u0086\u0084\3\2\2\2\u0087\u0088\b\23"+
		"\2\2\u0088&\3\2\2\2\13\29>DJSYv\u0084\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}