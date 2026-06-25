---
name: wechat-wenceafeng
description: 通用公众号全自动四阶段流水线——WeWrite写作→Humanizer去AI→卡片配图→生图排版发布草稿箱。只需配置品牌信息和API密钥即可使用。说"写一篇公众号文章"触发。
version: 2.0.0
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - WebSearch
  - WebFetch
---

# 公众号全自动四阶段流水线

## 快速开始

```bash
npx skills add MonkeyKEE/wechat-wenceafeng
```

然后在本项目创建 `brand.yaml`，填入你的品牌信息（见下方模板）。配置完成后说"写一篇公众号文章"即可触发全流程。

## 四阶段流水线

```
① WeWrite       → 热点→选题→框架→写作→SEO  → .md
② Humanizer-zh  → 去AI腔调                    → .md
③ guizang-card  → 卡片配图                    → PNG
④ baoyu         → WebSearch生图→插入→发布     → 草稿箱
```

## 前置依赖

| 依赖 | 安装 |
|:--|:--|
| wewrite | `npx skills add https://github.com/oaker-io/wewrite` |
| humanizer-zh | `npx skills add https://github.com/op7418/Humanizer-zh` |
| redfox-community | `npx skills add redfox-data/redfox-community` |
| baoyu-skills | `npx skills add JimLiu/baoyu-skills` |

---

## 配置：brand.yaml

在项目根目录或 `.claude/skills/wechat-wenceafeng/` 下创建 `brand.yaml`：

```yaml
# ── 必填 ──
brand:
  name: "你的品牌名"              # 如：掌上乾坤 · 演艺新空间
  author: "你的作者名"             # 如：云麓非遗小掌柜

footer:
  address: "你的地址"              # 如：湖南省XX市XX区XX路XX号
  phone: "你的电话"               # 如：133XXXXXXXX（姓氏）
  email: "你的邮箱"

wechat:
  appid: ""                      # 公众号AppID（API模式需要）
  secret: ""                     # 公众号AppSecret（API模式需要）

image:
  provider: "seedream"           # 可选：seedream/dashscope/openai
  api_key: ""                    # AI生图API Key

# ── 可选 ──
audience:                        # 你的目标受众（可自定义）
  - { name: "受众A", strategy: "写作策略" }
  - { name: "受众B", strategy: "写作策略" }
  - { name: "受众C", strategy: "写作策略" }

style_references: []             # 风格对标公众号名称（可选）
```

---

## 阶段一：写作

### 字数分档

| 类型 | 字数 |
|:--|:--|
| 活动发布/招募 | 2000-2500字 |
| 故事/人物 | 3000-4000字 |
| 专业观点/分析 | 4000-5000字 |

### 语言风格

不过度口语化，保留专业深度。比朋友圈正式，比行业报告轻松。
禁用网络流行语、表情符号、过度感叹。

### 写作规则

- 不生成标题备选，只用一个标题（20-28中文字）
- 开头从具体场景切入，不直接讲活动信息
- SEO关键词放在前200字内
- 结尾使用 `brand.yaml` 中配置的品牌信息

### 风格对标（可选）

在 `brand.yaml` 中配置 `style_references`，如 `["自然造物"]`。
配置后，「故事/人物」类文章将自动对标该公众号的叙事风格。

---

## 阶段二：去AI腔（Humanizer-zh）

1. 删除填充短语
2. 打破公式化结构
3. 变化句子节奏
4. 去除金句感
5. 保留专业深度
6. 减少宣传腔
7. 信任读者
8. 适度正式

---

## 阶段三：卡片配图（guizang）

从文章提取关键信息生成微信封面和社交卡片。

---

## 阶段四：配图+发布（baoyu）

### 排版规则

见 `references/layout-rules.md`。

### 生图规则

执行顺序（不可跳过）：

1. **WebSearch 搜索真实图片**（强制执行）
2. **检查项目自有素材**
3. **AI 生图**（仅在前两步不足时使用）

约束：真实摄影感、禁人物主体（只允许背影/侧影/手部）、禁生成文字。

### 最低图数

活动≥5张，日常分享≥8张。

### 发布

```bash
# 浏览器模式（无需 AppSecret）
bun run .agents/skills/baoyu-post-to-wechat/scripts/wechat-article.ts \
  --markdown "文章.md" --theme modern --author "作者名"

# API 模式（需配置 brand.yaml 中的 wechat.appid/secret）
bun run .agents/skills/baoyu-post-to-wechat/scripts/wechat-api.ts \
  "文章.md" --theme modern --author "作者名" --cover "cover.png"
```

### 素材存储

```
素材库/
├── 活动集锦照片/
├── AI生图照片/
└── web搜索下载照片/
```

## 参考

- `references/layout-rules.md` — 排版规则
- `references/image-rules.md` — 配图与生图规则
- `references/writing-style.md` — 文案风格示例
- `references/style-exemplar-ziranzaowu.md` — 自然造物风格对标（可选参考）
