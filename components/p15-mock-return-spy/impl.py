# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P15 mock-return-spy — 静默失败猎手

L0: 测试用的假数据偷偷跑到正式运行里，结果全是假的。这个工具抓它。
L1: 检测 except 分支里 return None/常量 的'假成功'模式。
L2: spy(code) 返回可疑行号。
"""

import ast
def spy(code):
    hits = []
    for node in ast.walk(ast.parse(code)):
        if isinstance(node, ast.ExceptHandler):
            for st in node.body:
                if isinstance(st, ast.Return) and (st.value is None or
                   isinstance(getattr(st, "value", None), ast.Constant)):
                    hits.append(st.lineno)
    return hits

def demo():
    print("[P15]", spy("try:\n f()\nexcept:\n return None\n"))


if __name__ == "__main__":
    demo()
