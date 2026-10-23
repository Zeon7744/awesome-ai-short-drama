# awesome-ai-short-drama 模块结构

## 目录
```
awesome-ai-short-drama/
├── demo_shortdrama.py   # 入口：素材扫描 + 短剧演示
├── tools/              # 素材工具（下载/预览/下载完整剧本）
├── drama-scripts/      # 国产短剧引擎与素材（自 domestic-drama 并入）
├── billing.py          # 收款层：NoopGateway + AfdianGateway + PAYWALL_RULES + check_access
└── docs/
```

## 数据流
1. `demo_shortdrama.py` 扫描素材库 → 选一部短剧 → 在线预览
2. 完整下载需付费 → `billing.check_access('free','download')` 门控
3. 超限 402 + 升级链接（爱发电 https://afdian.com/@Zeon7744）

## 门控模型
- `PAYWALL_RULES`: free=3 部/天, pro=不限, single=1 部/次, enterprise=不限
