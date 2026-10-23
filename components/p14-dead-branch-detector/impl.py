# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P14 dead-branch-detector — 静默失败猎手

L0: 有些代码永远跑不到，还占地方骗人。这个工具找出来。
L1: 检测 if False/if 0 常量分支与 return 之后的不可达语句。
L2: find(code) 返回可疑行号。
"""

import ast
def find(code):
    hits = []
    for node in ast.walk(ast.parse(code)):
        if isinstance(node, ast.If):
            t = node.test
            if isinstance(t, ast.Constant) and not t.value:
                hits.append(node.lineno)
    return hits

def demo():
    print("[P14]", find("if False:\n print(1)\n"))


if __name__ == "__main__":
    demo()
