import sys
import re
import textdistance
import difflib
import ast

filename1 = sys.argv[1]
filename2 = sys.argv[2]

with open(filename1) as f:
    text1 = f.read()
with open(filename2) as f:
    text2 = f.read()

uni_text1 = ast.unparse(ast.parse(text1))
uni_text2 = ast.unparse(ast.parse(text2))

dmp1 = ast.dump(ast.parse(uni_text1))
dmp2 = ast.dump(ast.parse(uni_text2))

keeeek = {'YieldFrom(': 'a', 'MatchMapping(': 'b', 'DictComp(': 'c', 'MatchClass(': 'd', 'Invert(': 'e', 'ExceptHandler(': 'f', 'Pow(': 'g', 'MatMult(': 'h', 'Starred(': 'i', 'Load(': 'j', 'Continue(': 'k', 'Eq(': 'l', 'Lambda(': 'm', 'Gt(': 'n', 'Import(': 'o', 'MatchStar(': 'p', 'Module(': 'q', 'MatchAs(': 'r', 'Dict(': 's', 'BinOp(': 't', 'FloorDiv(': 'u', 'Try(': 'v', 'JoinedStr(': 'w', 'BitAnd(': 'x', 'If(': 'y', 'Expression(': 'z', 'Nonlocal(': 'A', 'Call(': 'B', 'Add(': 'C', 'AsyncFor(': 'D', 'Slice(': 'E', 'Store(': 'F', 'Is(': 'G', 'ImportFrom(': 'H', 'BitXor(': 'I', 'For(': 'J', 'Set(': 'K', 'Raise(': 'L', 'MatchValue(': 'M', 'Name(': 'N', 'LtE(': 'O', 'Match(': 'P', 'MatchSequence(': 'Q', 'Not(': 'R', 'AsyncWith(': 'S', 'Del(': 'T', 'And(': 'U', 'List(': 'V', 'BoolOp(': 'W', 'MatchOr(': 'X', 'GeneratorExp(': 'Y', 'Compare(': 'Z', 'Assign(': '0', 'Pass(': '1', 'Delete(': '2', 'AnnAssign(': '3', 'UnaryOp(': '4', 'Expr(': '5', 'IfExp(': '6', 'FunctionDef(': '7', 'Await(': '8', 'SetComp(': '9', 'Interactive(': '!', 'NotEq(': '"', 'GtE(': '#', 'Global(': '$', 'USub(': '%', 'In(': '&', 'TypeIgnore(': "'", 'Constant(': '(', 'While(': ')', 'Lt(': '*', 'Tuple(': '+', 'UAdd(': ',', 'LShift(': '-', 'FunctionType(': '.', 'Attribute(': '/', 'Sub(': ':', 'BitOr(': ';', 'Yield(': '<', 'Div(': '=', 'With(': '>', 'AsyncFunctionDef(': '?', 'Or(': '@', 'ClassDef(': '[', 'ListComp(': '\\', 'FormattedValue(': ']', 'Subscript(': '^', 'RShift(': '_', 'Return(': '`', 'Assert(': '{', 'Mod(': '|', 'NULL(': '}', 'Break(': '~', 'NamedExpr(': 'я', 'IsNot(': 'ё', 'MatchSingleton(': 'ю', 'NotIn(': 'ы', 'AugAssign(': 'ъ', 'Mult(': 'ь'}

prep1 = ''.join(sym if not sym[0].isupper() else keeeek[sym] for sym in re.findall("[A-Z][A-Za-z]*\(|,|\)", dmp1))
prep2 = ''.join(sym if not sym[0].isupper() else keeeek[sym] for sym in re.findall("[A-Z][A-Za-z]*\(|,|\)", dmp1))

diff = textdistance.damerau_levenshtein.normalized_distance(prep1, prep2)
if diff <= 0.1:
    print(f"Plagiat {1-diff:.0%}!")
    print(difflib.HtmlDiff().make_file(uni_text1.split('\n'), uni_text2.split('\n')))
