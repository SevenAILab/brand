# Brand Naming Studio

一个品牌命名工作室型 OpenClaw Skill。

它不是随机起名器，而是一套把品牌命名从「灵感列表」推进到「判断结构」的工作流。

## 它解决什么问题

很多命名工具的问题是，只会一次性生成几十个名字，但不给判断标准。

`brand-naming-studio` 更关注这些问题：

- 品牌定位没说清楚时，先追问，不急着起名
- 先建立命名约束，再进入关键词和隐喻发散
- 按不同命名原型生成多个方向，而不是堆一堆相似名字
- 用「好记、相关、有戏、能用、包容」做 shortlist 评估
- 同时检查 fatal flaw，提前排除传播、域名、商标、跨文化和 AI 味命名风险
- 最终交付的不是名字列表，而是一套方便团队做决策的命名判断结构

## 适用场景

- 品牌名 / 公司名 / 产品名 / 项目名 / 栏目名 / 子品牌名
- 现有名字评审
- shortlist 筛选
- 重命名
- 命名系统构建
- Naming Agent / 起名工具 / 命名网站的 prompt、PRD 或 workflow

## 核心工作流

1. 定位 + 命名约束
2. 关键词 + 隐喻发散
3. 多原型候选生成
4. 五标准 + fatal flaw 筛选 shortlist
5. 收敛推荐 + 可调旋钮

## 文件结构

```text
.
├── SKILL.md
├── assets
│   └── shortlist-template.md
└── references
    ├── ai-naming-workflow.md
    ├── fatal-flaws.md
    ├── metaphor-mapping.md
    └── naming-standards.md
```

## 使用方式

把本仓库作为一个 skill 文件夹安装到 OpenClaw / Claude Code / 其他支持 skill 的 agent 系统中即可。

核心入口是：

```text
SKILL.md
```

如果你想直接阅读方法论，建议顺序是：

1. `SKILL.md`
2. `references/naming-standards.md`
3. `references/fatal-flaws.md`
4. `references/metaphor-mapping.md`
5. `references/ai-naming-workflow.md`

## 作者

Seven AI Lab

