# C04 · Silent Failure Hunting

> **机制簇**：静默失败猎手 ｜ **家族**：EIM-1.0（Emergent Intelligence Mechanisms）｜ **组件数**：4
>
> 本仓是 EIM-1.0 的**簇级入口**：一个机制簇 + 该簇全部可运行参考实现。
> 单组件仓与旗舰合集见文末「家族」段。

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
代码出错却装作没事（吞异常、返回空值），这类 bug 最难查。这簇工具专门把它们揪出来。

**L1 · 机制本质**
静态 AST 识别裸 except / 空 handler / 静默 None；调用图定位「可能返回 None 的来源」；运行期把被吞掉的异常升级为可观测事件。

**L2 · 怎么用上**
silent-except-scanner 静态扫；none-source-tracer 追 None 源头；failure-escalator 把吞异常变告警。

## 30 秒跑起来

```bash
git clone https://github.com/chenhz01/eim-c04-silent-failure-hunting.git && cd eim-c04-silent-failure-hunting
python run_all.py        # 跑全簇 4 个组件，逐个 selftest + 输出快照比对
```

单个组件也可独立跑：

```bash
python components/p13-silent-except-scanner/impl.py        # 看 demo 输出
python components/p13-silent-except-scanner/selftest.py    # 断言 + 与 golden_output.txt 比对
```

零第三方依赖，Python 3.9+ 即可。

## 本簇组件

| ID | 组件 | 机制本质 | 目录 |
|---|---|---|---|
| `P13` | silent-except-scanner | AST 扫描裸 except / except: pass / 空 handler。 | `components/p13-silent-except-scanner/` |
| `P14` | dead-branch-detector | 检测 if False/if 0 常量分支与 return 之后的不可达语句。 | `components/p14-dead-branch-detector/` |
| `P15` | mock-return-spy | 检测 except 分支里 return None/常量 的'假成功'模式。 | `components/p15-mock-return-spy/` |
| `P16` | closure-faker-linter | 检测函数体只有 return 'TODO'/pass/NotImplementedError 的伪完成。 | `components/p16-closure-faker-linter/` |

## 该用 / 不该用 / 常见误用

**该用**
接手遗留代码、上线前体检、AI 生成代码的准入审查。

**不该用**
用显式返回值表达失败的 API（如 Result/Either 类型），静态扫法会大量误报。

**常见误用（这条最重要）**
把所有 except 都判成坏味。合法的兜底 + 日志 + 指标是好的；有问题的只是「没人知道发生了」。

## 这份代码是什么、不是什么

- **是**：可直接运行、带断言与输出快照的最小参考实现。每个 `impl.py` 都能单独跑出 demo，`selftest.py` 会在行为漂移时报错。
- **不是**：生产级库。缺少配置化、并发安全、错误恢复、性能优化。**生产使用请按自己的约束扩展**，不要原样上生产。
- **诚实边界**：本簇解决的是「机制怎么落地」这个问题，不承诺在任何数据分布下都优于基线。基准数据请自测。

## 家族

- **旗舰合集（55 组件）**：https://github.com/chenhz01/emergent-mechanisms
- **单组件仓**：`eim-p01-…` ~ `eim-p55-…`，与 `components/` 内文件一致，任一处修复会双向同步。

## 许可（双许可）

- **代码**：**Apache-2.0**（Apache License 2.0）— 见 [LICENSE](LICENSE)
- **规范/文档**：**CC BY 4.0**（Creative Commons Attribution 4.0 International）— 见 [LICENSE-SPEC](LICENSE-SPEC)

声明符合 EIM-1.0 规范时须署名：

```
EIM-1.0 · C04 · Silent Failure Hunting © 2026 chenhz01, CC BY 4.0
```

详见 [NOTICE](NOTICE)。
