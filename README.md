# wechat-wenceafeng

通用公众号全自动流水线——从一句话到草稿箱。

只需配置你的品牌信息，即可拥有完整的公众号内容自动化工作流。

## 它能做什么

```
"写一篇公众号文章"
  → 选题策划 → 框架写作 → SEO优化
  → 去AI腔调 → 卡片配图 → 信息图生成
  → 排版发布 → 草稿箱
```

## 快速开始

```bash
npx skills add MonkeyKEE/wechat-wenceafeng
```

安装后在你的项目里创建 `brand.yaml`：

```yaml
brand:
  name: "你的品牌名"
  author: "你的作者名"
footer:
  address: "你的地址"
  phone: "你的电话"
  email: "你的邮箱"
```

配置完成。说"写一篇公众号文章"即可触发。

## 四阶段流水线

| 阶段 | 技能 | 产出 |
|:--|:--|:--|
| ① | **WeWrite** — 热点→选题→框架→写作→SEO | `.md` 文章 |
| ② | **Humanizer-zh** — 去AI腔调 | 润色后 `.md` |
| ③ | **guizang** — 卡片配图 | 封面+社交卡片 PNG |
| ④ | **baoyu** — Seedream生图+排版+发布 | 公众号草稿箱 |

## 安装

```bash
npx skills add MonkeyKEE/wechat-wenceafeng
```

### 前置依赖

| 依赖 | 安装命令 |
|:--|:--|
| WeWrite | `npx skills add https://github.com/oaker-io/wewrite` |
| Humanizer-zh | `npx skills add https://github.com/op7418/Humanizer-zh` |
| RedFox Community | `npx skills add redfox-data/redfox-community` |
| baoyu-skills | `npx skills add JimLiu/baoyu-skills` |

## 使用方式

安装后在 Claude Code 或 Codex 中说：

```
写一篇公众号文章
```

或指定方向：

```
写一篇针对家庭客群的暑假非遗体验招募推文
写一篇非遗数字化的趋势分析
写一篇传承人手艺变现的方法论
```

## 规范体系

| 规范 | 内容 |
|:--|:--|
| 📏 字数分档 | 活动招募 2000-2500 / 传承人故事 3000-4000 / 专业观点 4000-5000 |
| 🗣️ 语言风格 | 不过度口语化，保留专业深度 |
| 🎨 排版 | 纪实导览风，图片70-85%，纯灰白，无装饰 |
| 🖼️ 配图 | 网络图 > 自有图 > AI生图；活动≥5张/日常≥8张 |
| 🤖 AI生图 | 真实摄影感、禁人物主体、禁生成文字 |

## 适用场景

- 🏮 非遗文化空间（掌上乾坤 · 演艺新空间）
- 📱 微信公众号内容运营
- 🎯 三类受众：非遗从业者 / 科技企业 / 家庭客群
- 🏛️ 活动招募、行业分析、传承人故事

## 兼容性

- ✅ Claude Code
- ✅ Codex (OpenAI)

## License

MIT
