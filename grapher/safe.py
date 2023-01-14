import ast
import inspect
from typing import Any, Set


GRAPHER_ENV_NAMES: Set[str] = {
    'e',
    'pi', 'sin', 'cos', 'tan', 'cosec', 'sec', 'cot', 'factorial', 'sqrt', 'cbrt', 'ln', 'log'
}


def check_binop(operator: ast.BinOp) -> None:
    if type(operator.left) is ast.BinOp:
        check_binop(operator.left)
        return
    if type(operator.right) is ast.BinOp:
        check_binop(operator.right)
        return
    if type(operator.left) not in (ast.Name, ast.Constant, ast.Call):
        raise SyntaxError
    if type(operator.right) not in (ast.Name, ast.Constant, ast.Call):
        raise SyntaxError


def check_call(operator: ast.Call) -> None:
    assert isinstance(operator.func, ast.Name)
    if operator.func.id not in GRAPHER_ENV_NAMES:
        raise SyntaxError
    for arg in operator.args:
        if isinstance(arg, ast.Call):
            check_call(arg)
        elif isinstance(arg, ast.BinOp):
            check_binop(arg)
        elif not isinstance(arg, ast.Name):
            raise SyntaxError


def validate_code(code: str) -> None:
    for operator in ast.parse(code).body:
        assert isinstance(operator, ast.Expr)
        value = operator.value
        if isinstance(value, ast.BinOp):
            check_binop(value)
        elif isinstance(value, ast.Call):
            check_call(value)
        else:
            raise SyntaxError


def safe_eval(code: str, *args: Any) -> Any:
    validate_code(code)
    return eval(code, *args)
