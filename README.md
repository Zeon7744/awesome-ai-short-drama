# 🎬 Awesome AI Short Drama

> AI 短剧创作的全链路解决方案 — 从剧本到工具，从作品到方法论

用 AI 做短剧，从剧本到成片，这一套就够了。持续更新，欢迎 PR 补充。

[![GitHub Stars](https://img.shields.io/github/stars/Zeon7744/awesome-ai-short-drama?style=social)](https://github.com/Zeon7744/awesome-ai-short-drama)
[![爱发电](https://img.shields.io/badge/爱发电-国内赞助-946ce6?style=flat-square)](https://ifdian.net/a/Zeon7744)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub-Sponsors-ea4aaa?style=flat-square&logo=githubsponsors)](https://github.com/sponsors/Zeon7744)

---

## 🗺️ 产品矩阵

| 仓库 | 定位 | 链接 |
|------|------|------|
| **awesome-ai-short-drama** | 短剧创作 OS：作品 + 工具 + 资源清单 | ← 当前 |
| [baibai](https://github.com/Zeon7744/baibai) | 通用 Vibe Coding 工具库（CLI + MCP） | 查看 → |

---

## 📚 原创内容

### 短篇小说（5部）

可直接改编为 AI 短剧/漫剧的视觉化写作，8000-15000 字/部。

| 作品 | 类型 | 字数 | 核心看点 |
|------|------|------|---------|
| [万古战神在都市](short-stories/万古战神在都市_短篇.md) | 都市修真/兵王 | ~9,300 | 战神魂穿废少，闪婚总裁，一路碾压 |
| [帝师无双](short-stories/帝师无双_短篇.md) | 玄幻穿越/王道 | ~14,600 | 白皇降临，双皇共治，三系融合碎虚空 |
| [战神失忆后被村姑捡回家了](short-stories/战神失忆后被村姑捡回家了_短篇.md) | 都市异能/甜宠 | ~12,400 | 失忆憨虎 vs 村姑，甜宠反差，战王归来 |
| [江城情缘](short-stories/江城情缘_短篇.md) | 都市甜宠/豪门 | ~10,900 | 毒舌女主怼上冷面阎王，反差萌 |
| [重生劫奴](short-stories/重生劫奴_短篇.md) | 玄幻修真/逆天 | ~12,000 | 天劫棋局，众生觉醒，斩道破局 |

### 短剧剧本（9部 · 130集）

符合红果短剧平台规范（≤15字对话、≥3爽点/集）。

| 序号 | 剧名 | 类型 | 集数 | 剧本 |
|------|------|------|------|------|
| 1 | [剑魂重生](short-dramas/剑魂重生/剑魂重生_完整剧本.md) | 玄幻重生 | 30集 | [查看](short-dramas/剑魂重生/剑魂重生_完整剧本.md) |
| 2 | [帝师无双](short-dramas/帝师无双/帝师无双_完整剧本.md) | 玄幻重生 | 10集 | [查看](short-dramas/帝师无双/帝师无双_完整剧本.md) |
| 3 | [总裁的替身前妻](short-dramas/总裁的替身前妻/总裁的替身前妻_完整剧本.md) | 都市异能 | 10集 | [查看](short-dramas/总裁的替身前妻/总裁的替身前妻_完整剧本.md) |
| 4 | [暗夜追凶](short-dramas/暗夜追凶/暗夜追凶_完整剧本.md) | 悬疑推理 | 10集 | [查看](short-dramas/暗夜追凶/暗夜追凶_完整剧本.md) |
| 5 | [江城情缘](short-dramas/江城情缘/江城情缘_完整剧本.md) | 都市甜宠 | 30集 | [查看](short-dramas/江城情缘/江城情缘_完整剧本.md) |
| 6 | [狂少逆袭](short-dramas/狂少逆袭/狂少逆袭_完整剧本.md) | 都市豪门 | 10集 | [查看](short-dramas/狂少逆袭/狂少逆袭_完整剧本.md) |
| 7 | [神医赘婿](short-dramas/神医赘婿/神医赘婿_完整剧本.md) | 都市异能 | 10集 | [查看](short-dramas/神医赘婿/神医赘婿_完整剧本.md) |
| 8 | [龙皇归来](short-dramas/龙皇归来/龙皇归来_完整剧本.md) | 玄幻重生 | 10集 | [查看](short-dramas/龙皇归来/龙皇归来_完整剧本.md) |
| 9 | [替身归来](short-dramas/替身归来/替身归来_完整剧本.md) | 都市豪门 | 10集 | [查看](short-dramas/替身归来/替身归来_完整剧本.md) |

> 📌 剧本创作规范：标题第X集：集名 · 结尾第X集完 · 对话≤15字 · 每集≥3爽点+1甜点

---

## 🛠️ 配套工具

短剧专属工具链，全部开源可本地运行。

| 工具 | 功能 | 使用说明 |
|------|------|---------|
| [格式校验器](tools/format_checker.py) | 检查剧本是否符合平台规范（禁止字符、括号格式、标题结构、评分报告） | `python tools/format_checker.py <目录>` |
| [内容分类器](tools/classifier.py) | 自动识别短剧/小说/教程等类型，生成分类报告 | `python tools/classifier.py <目录>` |
| [数据统计器](tools/stats_analyzer.py) | 字数/章节/类型分布统计，排行榜生成 | `python tools/stats_analyzer.py <目录>` |
| [README 生成器](tools/readme_gen.py) | 根据内容目录自动生成 README 表格 | `python tools/readme_gen.py <readme路径> <内容目录>` |
| [MD→HTML 转换](tools/md2html.py) | Markdown 转美观 HTML 页面，用于短剧展示 | `python tools/md2html.py <输入.md> [输出.html]` |
| [短剧详情页生成器](scripts/gen_drama_pages.py) | 批量为每部短剧生成独立 HTML 展示页 | `python scripts/gen_drama_pages.py` |

> 💡 更多通用 CLI 工具（MCP Server、格式转换等）请前往 [baibai](https://github.com/Zeon7744/baibai)

---

## 📖 方法论与教程

| 文档 | 说明 |
|------|------|
| [红果平台运营策略](docs/redfruit-strategy.md) | 红果短剧投稿规范与流量机制 |
| [短剧改编指南](docs/adaptation-guide.md) | 小说→短剧的改编方法论 |
| [爽点设计 10 讲](docs/爽点设计-10讲.md) | 短剧核心节奏方法论（持续更新中） |

> 📝 方法论文档持续创作中，欢迎 Star 跟进。

---

## 🔗 资源与工具清单

AI 短剧全链路工具、模型、提示词、工作流精选。

### ✍️ 剧本创作

| 工具 | 说明 | 地址 |
|------|------|------|
| ChatGPT | 剧本创作、角色设定、对白润色 | [链接](https://chat.openai.com) |
| Claude | 长文本剧本、多线叙事、角色一致性 | [链接](https://claude.ai) |
| 豆包 | 中文短剧剧本，熟悉国内平台调性 | [链接](https://www.doubao.com) |
| DeepSeek | 中文创作，逻辑推理强 | [链接](https://www.deepseek.com) |
| Kimi | 长文档处理，剧本大纲与参考资料分析 | [链接](https://kimi.moonset.cn) |
| 通义千问 | 阿里出品，中文内容创作 | [链接](https://tongyi.aliyun.com) |
| 文心一言 | 百度出品，中文理解 | [链接](https://yiyan.baidu.com) |

### 🎥 AI 视频生成

#### 国产平台

| 工具 | 特点 | 地址 |
|------|------|------|
| 即梦 AI | 字节出品，图片/视频生成，支持 Seedance 模型 | [链接](https://jimeng.jianying.com) |
| 可灵 AI | 快手出品，视频生成质量高，支持图生视频 | [链接](https://klingai.kuaishou.com) |
| Vidu | 生数科技，动漫风格擅长 | [链接](https://www.vidu.studio) |
| 智谱清影 | 智谱 AI 视频生成 | [链接](https://chatglm.cn/video) |
| 海螺 AI (Hailuo) | MiniMax 出品，视频生成 | [链接](https://hailuoai.video) |
| 小云雀 | 字节短剧创作平台，Seedance 2.0 接入 | - |

#### 海外平台

| 工具 | 特点 | 地址 |
|------|------|------|
| Sora | OpenAI 视频生成 | [链接](https://openai.com/sora) |
| Runway | 老牌 AI 视频，Gen-4 模型 | [链接](https://runwayml.com) |
| Pika | 视频生成与编辑 | [链接](https://pika.art) |
| Luma Dream Machine | 图生视频，运动质量好 | [链接](https://lumalabs.ai/dream-machine) |
| Veo 2 / Veo 3 | Google DeepMind 视频模型 | - |

### 🎨 AI 图片生成

| 工具 | 特点 | 地址 |
|------|------|------|
| Midjourney | 顶级画质，角色设计/分镜 | [链接](https://www.midjourney.com) |
| Stable Diffusion | 开源，本地部署，ComfyUI 生态 | [链接](https://stability.ai) |
| ComfyUI | 节点式工作流，短剧批量出图首选 | [链接](https://github.com/comfyanonymous/ComfyUI) |
| Flux | Black Forest Labs，开源模型新标杆 | [链接](https://github.com/black-forest-labs/flux) |
| 即梦 AI | 字节文生图/图生图 | [链接](https://jimeng.jianying.com) |
| 可灵 AI | 快手文生图 | [链接](https://klingai.kuaishou.com) |
| LiblibAI | 国内模型与 LoRA 社区 | [链接](https://www.liblib.art) |

### 🎵 AI 音乐与音效

| 工具 | 特点 | 地址 |
|------|------|------|
| Suno | AI 作曲，支持人声，短剧 BGM/主题曲 | [链接](https://suno.com) |
| Udio | AI 音乐生成，音质出色 | [链接](https://www.udio.com) |
| ElevenLabs Sound Effects | AI 音效生成 | [链接](https://elevenlabs.io/sound-effects) |

### 🎙️ AI 配音与语音

| 工具 | 特点 | 地址 |
|------|------|------|
| 剪映 | 自带 AI 配音，中文音色多，免费 | [链接](https://www.capcut.cn) |
| ElevenLabs | 顶级 AI 语音克隆与配音 | [链接](https://elevenlabs.io) |
| Fish Speech | 开源语音克隆，中文效果好 | [链接](https://github.com/fishaudio/fish-speech) |
| ChatTTS | 开源中文 TTS，自然对话风格 | [链接](https://github.com/2noise/ChatTTS) |
| CosyVoice | 阿里开源语音克隆 | [链接](https://github.com/FunAudioLLM/CosyVoice) |

### 🎞️ 视频剪辑与后期

| 工具 | 特点 | 地址 |
|------|------|------|
| 剪映专业版 | 国产首选，AI 字幕/配音/特效一站式 | [链接](https://www.capcut.cn) |
| CapCut | 剪映国际版 | [链接](https://www.capcut.com) |
| DaVinci Resolve | 专业调色与剪辑 | [链接](https://www.blackmagicdesign.com/products/davinciresolve) |
| Topaz Video AI | 视频超分/补帧/降噪 | [链接](https://www.topazlabs.com/topaz-video-ai) |

### 📝 字幕工具

| 工具 | 特点 | 地址 |
|------|------|------|
| 剪映自动字幕 | 一键识别，中文准确率高 | - |
| Whisper | OpenAI 开源语音识别，多语言 | [链接](https://github.com/openai/whisper) |
| faster-whisper | Whisper 加速版 | [链接](https://github.com/SYSTRAN/faster-whisper) |

### 🔄 角色一致性方案

- **IP-Adapter + Reference Only**：ComfyUI 中保持角色面部一致
- **PuLID**：个性化人脸保持，提升角色一致性
- **InstantID**：零样本身份保持生成
- **LoRA 训练**：用角色图片训练专属 LoRA，最稳定的一致性方案
- **即梦角色一致性**：即梦 AI 内置角色参考功能

---

## 📱 发布平台

### 国内短剧平台

| 平台 | 说明 | 地址 |
|------|------|------|
| 红果短剧 | 字节系，免费短剧平台，AI 短剧扶持 | [链接](https://www.shortdramas.com) |
| 抖音短剧 | 字节系，流量最大 | [链接](https://www.douyin.com) |
| 快手星芒短剧 | 快手短剧品牌 | - |
| 腾讯微短剧 | 腾讯系 | - |
| 爱奇艺短剧 | 爱奇艺微短剧/漫剧 | - |
| 优酷短剧 | 阿里系 | - |
| 哔哩哔哩 | B 站，二次元/漫剧受众 | [链接](https://www.bilibili.com) |
| 小红书 | 种草+短剧 | - |
| 微信视频号 | 微信生态 | - |

### 海外平台

| 平台 | 说明 |
|------|------|
| YouTube Shorts | 短视频，广告分成 |
| TikTok | 全球最大短视频平台 |
| ReelShort | 中国短剧出海代表 |
| DramaBox | 短剧出海平台 |

---

## 📰 行业资讯与社区

- **即刻 App**：搜索"AI 短剧""AI 视频"圈子
- **B 站**：搜索"AI 短剧教程"，关注头部 UP 主
- **V2EX**：技术讨论，AI 工具节点
- **少数派**：AI 工具评测与教程
- **Reddit r/aivideo**：海外 AI 视频社区
- **Hugging Face**：模型与数据集

---

## 🤝 贡献

欢迎提交 PR！你可以：
- 补充新的工具和平台
- 修正已有链接和信息
- 添加教程和工作流
- 分享你的制作经验

---

## 📄 License

CC0-1.0 License - 自由使用，无需署名。

---

## ☕ 支持作者

如果这个仓库对你有帮助，欢迎爱发电支持 ☕

| 渠道 | 方式 | 链接 |
|------|------|------|
| **爱发电** | 月度订阅 / 一次性打赏 | [ifdian.net/a/Zeon7744](https://ifdian.net/a/Zeon7744) |

---

> ⚠️ 本仓库仅做资源和工具收录，不构成任何投资或商业建议。使用 AI 工具时请遵守各平台服务条款及当地法律法规。
