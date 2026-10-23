# P14 · dead-branch-detector

> 机制簇：**静默失败猎手** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
有些代码永远跑不到，还占地方骗人。这个工具找出来。

**L1 · 机制本质**
检测 if False/if 0 常量分支与 return 之后的不可达语句。

**L2 · 怎么用上**
find(code) 返回可疑行号。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P14] [1]
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | CI 前置检查、重构后回归、接手他人代码时的快速体检。 |
| **不该用** | 大量动态生成/元编程代码（误报率高）；需要语义理解的业务逻辑错误。 |
| **常见误用** | 把裸 except 一律判死——有些是刻意的降级路径，必须报告而非直接改。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P13` silent-except-scanner · `P15` mock-return-spy · `P16` closure-faker-linter
- 本仓是 **P14 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P14-dead-branch-detector/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](../../LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](../../LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P14 · dead-branch-detector © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](../../NOTICE)。
