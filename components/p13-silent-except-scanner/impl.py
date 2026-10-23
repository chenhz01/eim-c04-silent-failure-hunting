# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P13 silent-except-scanner — 静默失败猎手

L0: 代码里最坑的 bug 是'出错了却装作没事'。这个工具把它们揪出来。
L1: AST 扫描裸 except / except: pass / 空 handler。
L2: scan(code) 返回问题列表 (行号, 类型)。
"""

import ast
def scan(code):
    hits = []
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler):
            if node.type is None:
                hits.append((node.lineno, "bare_except"))
            if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                hits.append((node.lineno, "except_pass"))
    return hits

def demo():
    src = "try:\n x=1\nexcept:\n pass\n"
    print("[P13]", scan(src))


if __name__ == "__main__":
    demo()
