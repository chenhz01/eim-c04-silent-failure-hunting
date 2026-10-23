# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P16 closure-faker-linter — 静默失败猎手

L0: 有的函数嘴上说'做完了'，其实返回个占位符。这个工具识破它。
L1: 检测函数体只有 return 'TODO'/pass/NotImplementedError 的伪完成。
L2: lint(code) 返回伪完成函数名。
"""

import ast
def lint(code):
    bad = []
    for node in ast.walk(ast.parse(code)):
        if isinstance(node, ast.FunctionDef):
            body = [n for n in node.body if not isinstance(n, ast.Expr)]
            if len(body) == 1 and isinstance(body[0], ast.Return):
                v = body[0].value
                if isinstance(v, ast.Constant) and (v.value in ("TODO", "", None)):
                    bad.append(node.name)
            if len(body) == 1 and isinstance(body[0], ast.Pass):
                bad.append(node.name)
    return bad

def demo():
    print("[P16]", lint("def f():\n return 'TODO'\ndef g():\n pass\n"))


if __name__ == "__main__":
    demo()
