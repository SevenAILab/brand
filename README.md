# Brand Naming Studio

一个品牌命名工作室型 OpenClaw Skill。

它不是随机起名器，而是一套把品牌命名从「灵感列表」推进到「判断结构」的工作流。

## 开源地址

https://github.com/SevenAILab/brand

## 一句话安装

如果你使用 Claude Code、OpenClaw、Cursor 或其他支持 Skills 的 AI 工具，可以在终端里直接运行：

```bash
npx -y skills add https://github.com/SevenAILab/brand -g --all
```

装好之后，对 AI 说这句就能触发：

```text
用 brand-naming-studio 帮我起一个品牌名。
```

如果你只想安装到当前项目，可以去掉 `-g`：

```bash
npx -y skills add https://github.com/SevenAILab/brand --all
```

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

安装完成后，直接把需求告诉 AI 即可，例如：

```text
用 brand-naming-studio 帮我给一个 AI 写作小程序起中文名。用户是小红书博主，功能是把语音想法整理成笔记草稿。名字要口语一点，适合在小红书传播。
```

如果你想直接阅读方法论，建议顺序是：

1. `SKILL.md`
2. `references/naming-standards.md`
3. `references/fatal-flaws.md`
4. `references/metaphor-mapping.md`
5. `references/ai-naming-workflow.md`

## 作者

Seven AI Lab
