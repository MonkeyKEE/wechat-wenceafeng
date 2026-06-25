---
name: wechat-wenceafeng
description: 云麓智联公众号全自动四阶段流水线——WeWrite写作→Humanizer去AI→guizang卡片→baoyu配图发布。含完整文案规范、排版规则、生图约束。说"写一篇公众号文章"即可触发。
version: 1.0.0
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

# 云麓智联公众号全自动流水线

## 触发方式

"写一篇公众号文章" / "/wechat-pipeline 主题" / "发一篇推文"

## 四阶段流水线

```
① WeWrite       → 热点→选题→框架→写作→SEO  → .md
② Humanizer-zh  → 去AI腔调                    → .md
③ guizang-card  → 卡片配图                    → PNG
④ baoyu         → Seedream生图→插入→发布      → 草稿箱
```

## 前置依赖

本技能依赖以下插件（需预先安装）：

| 依赖 | 来源 | 用途 |
|:--|:--|:--|
| wewrite | https://github.com/oaker-io/wewrite | 热点→选题→写作→SEO |
| humanizer-zh | https://github.com/op7418/Humanizer-zh | 去AI腔调 |
| redfox-community | https://github.com/redfox-data/redfox-community | 热搜数据 |
| baoyu-skills | https://github.com/JimLiu/baoyu-skills | 生图+发布 |

---

## 阶段一：写作（WeWrite + 品牌规范）

### 字数分档

| 类型 | 字数 | 适用 |
|:--|:--|:--|
| 活动发布/招募 | 2000-2500字 | 周末活动、体验课报名 |
| 非遗故事/传承人 | 3000-4000字 | 手艺人物、行业观察 |
| 专业分享/观点 | 4000-5000字 | 文化科技、产业分析 |

### 语言风格

不过度口语化，保留专业分析深度。比朋友圈正式，比行业报告轻松。
禁用：网络流行语、表情符号、过度感叹。

### 三类受众策略

| 受众 | 策略 |
|:--|:--|
| 非遗从业者 | 痛点共鸣 + 可落地的商业方法论 |
| 科技企业负责人 | 趋势洞察 + 数据/案例支撑 |
| 家庭客群 | 温暖叙事 + 适度体验解析 |

### 写作规则

- 不生成标题备选，只用一个标题（20-28中文字）
- 开头从具体场景切入，不直接讲活动信息
- 每篇自然出现"湖南省木偶皮影艺术保护传承中心"和"掌上乾坤"
- 不用"云麓智联旗下品牌"，用"运营这个空间、服务这个项目"
- SEO关键词放在前200字

### 固定品牌结尾

```
**掌上乾坤 · 演艺新空间**
湖南省木偶皮影艺术保护传承中心 一楼
由掌上乾坤运营的非遗文化体验空间

📍 湖南省木偶皮影艺术保护传承中心 一楼
📞 13308485831（侯先生）
📮 godmrik@gmail.com
```

详细的受众策略和叙事路径见 `references/writing-style.md`。

---

## 阶段二：去AI腔（Humanizer-zh）

1. 删除填充短语
2. 打破公式化结构（不要编号式三步）
3. 变化句子节奏（不过度追求极短句）
4. 去除金句感
5. 保留专业深度（不把分析改成大白话）
6. 减少宣传腔
7. 信任读者（不过度引导）
8. 适度正式

---

## 阶段三：卡片配图（guizang）

从文章中提取关键信息，生成微信封面(16:9)和社交卡片(3:4)。

---

## 阶段四：配图+排版+发布（baoyu）

### 排版规则

见 `references/layout-rules.md`，核心：

- **纪实导览风**：图片占70-85%，短文字导览，留白控制节奏
- **极简灰白**：底色#FFF，标题#1F1F1F，正文#333。无品牌色注入
- **标题左对齐无装饰**：18-20px加粗，不加色块/图标/竖条
- **正文14-15px**：行距1.7-1.9，每段1-3行，30-80字
- **图片全宽**：不加边框/投影/拼图
- **模块分割只用留白**：不用装饰线/花纹/色块

### 生图规则

见 `references/image-rules.md`，核心：

- **来源优先级**：网络真实图 > 项目自有图 > AI生图
- **最低数量**：活动≥5张，日常≥8张
- **AI约束**：真实摄影感、禁人物主体(只允许背影/侧影/手部)、禁生成文字
- **尺寸**：全景4:3/3:2、细节1:1/4:5、封面16:9

### 素材三分区

```
05_素材库/
├── 活动集锦照片/     ← 用户拍摄
├── AI生图照片/       ← 含prompts.txt
└── web搜索下载照片/  ← 网络下载
```

### 发布命令

```bash
# 浏览器模式
bun run .agents/skills/baoyu-post-to-wechat/scripts/wechat-article.ts \
  --markdown "文章.md" --theme modern --author "云麓非遗小掌柜"

# API模式
export WECHAT_APP_ID="wx9f01ac04fe0b16c2"
export WECHAT_APP_SECRET="0232c7d3642c0605f2e88ca502d22fb6"
bun run .agents/skills/baoyu-post-to-wechat/scripts/wechat-api.ts \
  "文章.md" --theme modern --author "云麓非遗小掌柜" --cover "cover.png"
```

## 目录规范

```
新媒体内容创造/
├── 00_品牌与运营规则/
├── 04_项目内容资产/掌上乾坤演艺新空间/每周公众号/
├── 05_素材库/{活动集锦照片,AI生图照片,web搜索下载照片}/
└── 06_发布日历与复盘/发布记录/
```
