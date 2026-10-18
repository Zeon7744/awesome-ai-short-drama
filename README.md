# 🎬 Awesome AI Short Drama
> ✅ **国产短剧引擎已并入**：原 `domestic-drama` 仓的引擎(`drama-scripts/drama_engine.py`)、
> 测试、素材已迁入本仓 `drama-scripts/`；`domestic-drama` 归档停止独立维护。


> **AI 短剧创作全链路解决方案** — 从剧本到成片，这一套就够了  
> 开源短剧剧本库 · 创作工具 · 方法论 · 资源清单

[![GitHub Stars](https://img.shields.io/github/stars/Zeon7744/awesome-ai-short-drama?style=social)](https://github.com/Zeon7744/awesome-ai-short-drama)
[![GitHub Forks](https://img.shields.io/github/forks/Zeon7744/awesome-ai-short-drama?style=social)](https://github.com/Zeon7744/awesome-ai-short-drama/forks)
[![GitHub License](https://img.shields.io/github/license/Zeon7744/awesome-ai-short-drama)](https://github.com/Zeon7744/awesome-ai-short-drama/blob/main/LICENSE)
[![Gitee Stars](https://gitee.com/Zeon7744/awesome-ai-short-drama/badge/star.svg?theme=gvp)](https://gitee.com/Zeon7744/awesome-ai-short-drama)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Redfruit Ready](https://img.shields.io/badge/红果-ready-success.svg)](https://www.shortdramas.com)

---

## 📌 这是 GitHub 官方主仓

> **Gitee 镜像**: [gitee.com/Zeon7744/awesome-ai-short-drama](https://gitee.com/Zeon7744/awesome-ai-short-drama)  
> **GitCode 镜像**: [gitcode.com/Zeon7744/awesome-ai-short-drama](https://gitcode.com/Zeon7744/awesome-ai-short-drama)

Issues 和 PR 请在 GitHub 提交。

---

## 📊 内容概览

| 类别 | 数量 | 说明 |
|------|------|------|
| 🎭 短剧剧本 | 9 部 | 130 集，符合红果平台规范 |
| 📖 短篇小说 | 5 部 | 可直接改编为短剧 |
| 🛠️ 创作工具 | 6 个 | 格式校验、数据分析、页面生成 |
| 📚 方法论文档 | 3 篇 | 爽点设计、改编指南、平台策略 |

---

## 🎬 短剧剧本库

| 序号 | 剧名 | 类型 | 集数 | 亮点 |
|------|------|------|------|------|
| 1 | [剑魂重生](short-dramas/剑魂重生/) | 玄幻重生 | 30集 | 战神魂穿废少 |
| 2 | [帝师无双](short-dramas/帝师无双/) | 玄幻穿越 | 10集 | 双皇共治 |
| 3 | [总裁的替身前妻](short-dramas/总裁的替身前妻/) | 都市异能 | 10集 | 马甲掉落 |
| 4 | [暗夜追凶](short-dramas/暗夜追凶/) | 悬疑推理 | 10集 | 侦探悬疑 |
| 5 | [江城情缘](short-dramas/江城情缘/) | 都市甜宠 | 30集 | 豪门恋曲 |
| 6 | [狂少逆袭](short-dramas/狂少逆袭/) | 都市豪门 | 10集 | 废柴崛起 |
| 7 | [神医赘婿](short-dramas/神医赘婿/) | 都市异能 | 10集 | 医术无双 |
| 8 | [龙皇归来](short-dramas/龙皇归来/) | 玄幻重生 | 10集 | 龙王归来 |
| 9 | [替身归来](short-dramas/替身归来/) | 都市豪门 | 10集 | 身份反转 |

> 每部剧本均符合 **红果短剧平台规范**（≤15字对话，≥3爽点/集）

---

## 📖 短篇小说库

| 作品 | 类型 | 字数 | 改编建议 |
|------|------|------|----------|
| [万古战神在都市](short-stories/万古战神在都市_短篇.md) | 都市修真 | ~9,300 | 战神流短剧 |
| [帝师无双](short-stories/帝师无双_短篇.md) | 玄幻穿越 | ~14,600 | 王道玄幻短剧 |
| [战神失忆后被村姑捡回家了](short-stories/战神失忆后被村姑捡回家了_短篇.md) | 都市异能 | ~12,400 | 甜宠反差短剧 |
| [江城情缘](short-stories/江城情缘_短篇.md) | 都市甜宠 | ~10,900 | 豪门恋曲短剧 |
| [重生劫奴](short-stories/重生劫奴_短篇.md) | 玄幻修真 | ~12,000 | 逆天改命短剧 |

---

## 🛠️ 配套工具

| 工具 | 功能 | 快速命令 |
|------|------|----------|
| [格式校验器](tools/format_checker.py) | 检查剧本规范 | `python tools/format_checker.py <目录>` |
| [数据统计器](tools/stats_analyzer.py) | 字数/章节统计 | `python tools/stats_analyzer.py <目录>` |
| [README 生成器](tools/readme_gen.py) | 自动生成文档 | `python tools/readme_gen.py <readme> <目录>` |
| [Markdown 转 HTML](tools/md2html.py) | 内容展示 | `python tools/md2html.py input.md` |
| [短剧详情页生成器](scripts/gen_drama_pages.py) | 批量生成展示页 | `python scripts/gen_drama_pages.py` |

---

## 📚 方法论与教程

| 文档 | 说明 |
|------|------|
| [爽点设计 10 讲](docs/爽点设计-10讲.md) | 短剧核心节奏方法论 |
| [短剧改编指南](docs/adaptation-guide.md) | 小说→短剧的改编方法论 |
| [红果平台运营策略](docs/redfruit-strategy.md) | 投稿规范与流量机制 |

---

## 🗺️ 产品矩阵

| 仓库 | 定位 | 链接 |
|------|------|------|
| **awesome-ai-short-drama** | 短剧创作 OS：作品 + 工具 + 资源清单 | ← 当前 |
| [baibai](https://github.com/Zeon7744/baibai) | 通用 Vibe Coding 工具库 | → |
| [dev-artifacts](https://github.com/Zeon7744/dev-artifacts) | 开发成果成品库 | → |

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/Zeon7744/awesome-ai-short-drama.git
cd awesome-ai-short-drama
```

### 2. 浏览剧本

```bash
# 查看短剧列表
ls short-dramas/

# 查看小说列表
ls short-stories/
```

### 3. 运行工具

```bash
# 校验剧本格式
python tools/format_checker.py short-dramas/

# 统计内容数据
python tools/stats_analyzer.py short-dramas/

# 生成短剧展示页
python scripts/gen_drama_pages.py
```

---

## 📈 项目统计

- **总字数**: ~80,000+ 字
- **短剧集数**: 130 集
- **剧本数量**: 9 部
- **工具数量**: 6 个
- **方法论文档**: 3 篇

---

## 🎯 创作规范

所有剧本遵循以下规范：

1. **标题格式**: `第X集：集名`
2. **结尾标记**: `第X集完`
3. **对话长度**: ≤15 字/句
4. **节奏要求**: 每集 ≥3 爽点 + 1 甜点
5. **禁止字符**: 耀、曜

---

## 🤝 贡献指南

欢迎贡献！你可以：

- 补充新的短剧剧本
- 添加创作工具
- 完善方法论文档
- 修正已有内容

### 贡献流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/new-drama`)
3. 提交更改 (`git commit -m 'Add new drama: XXX'`)
4. 推送到分支 (`git push origin feature/new-drama`)
5. 开启 Pull Request

---

## 📰 行业资讯

关注 AI 短剧行业动态：

- [红果短剧官网](https://www.shortdramas.com)
- [抖音短剧](https://www.douyin.com)
- [即刻 - AI短剧圈子](https://jike.com)

---

## ☕ 支持作者

如果这个项目对你有帮助，欢迎赞助 ☕

| 渠道 | 方式 |
|------|------|
| [爱发电](https://afdian.com/@Zeon7744) | 支付宝 / 微信支付 |
| [GitHub Sponsors](https://github.com/sponsors/Zeon7744) | PayPal / Stripe |

---

## 📄 License

CC0-1.0 License — 自由使用，无需署名。

---

<div align="center">

**由 [Zeon7744](https://github.com/Zeon7744) 维护**  
*AI 短剧创作全链路开源项目*

⭐ 如果对你有帮助，点个 Star 鼓励一下！

</div>

---

## 🚀 免费 → Pro → 企业（变现入口）

免费=浏览素材；Pro=下载完整剧本/小说；企业=商用授权+定制题材

- **免费**：立即 [安装/克隆] 使用，命中配额即可升级。
- **Pro**：[Gitee Pro 订阅](https://gitee.com/Zeon7744) 解锁高级能力。
- **企业**：私有部署 / 定制需求 → 见 `pricing.md`，或联系商务（GitHub Issues / Gitee）。

> 详细定价与 SKU 见 [pricing.md](pricing.md) ｜ 支持项目见 [FUNDING.yml](FUNDING.yml)

---

## 快速上手
依赖安装：
```bash
无 Python 依赖（纯内容/配置仓）
```

## 变现路径
内容/素材仓，商用需遵循 License（CC）；Pro 素材订阅功能待接 ai-mcn-studio 变现通道。

## 🎬 可运行 demo
`python3 demo_shortdrama.py`：一条命令跑通"素材扫库 → 内容分类 → 格式校验 → 变现钩子"，资源仓从"能翻素材"升级为"能自证可用 + 看到变现入口"。

## ⚖️ 法控声明（内容与版权）
- **内容免责**：本仓素材/剧本/方法论**仅供创作参考与学习**，商用须遵循 LICENSE（代码 MIT）+ LICENSE-CONTENT（示例内容 CC-BY-NC）授权范围；AI 生成/改编内容可能含版权与合规风险，发布责任由使用者承担。
- **合规卡点**：短剧发布前须完成平台备案与人工合规审查（对接 ai-mcn-studio 的 `batch_compliance` 批量合规扫描）。
- **数据脱敏**：素材不采集/存储任何真实用户个人信息；短剧素材中的虚构人物不涉真实肖像权。
> 定价与赞助：见仓库内 pricing.md / FUNDING.yml（若有）。
