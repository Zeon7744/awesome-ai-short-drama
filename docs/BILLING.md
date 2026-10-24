# awesome-ai-short-drama 收款与门控（面包多 Pay mbd）

## 定价档位（与 billing.py 对齐）
| 档位 | 价格 | 限制 |
|---|---|---|
| Free | ¥0 | 3 部/天浏览+预览 |
| Pro | ¥49/月 | 完整剧本+模板库 |
| 单次 | ¥9.9/部 | 单部完整下载 |
| 企业 | ¥499/月 | 商用+定制题材+红果对接 |

## 收款流程（先体验后付费）
1. 免费 3 部/天，超限 402 + 升级链接（面包多 Pay https://mbd.com/@Zeon7744）
2. 付款 → `billing.MbdGateway.query_callback` 核验 → 本地提权
3. 无 key 走 `noop` 安全降级

## 环境变量
`JZ_mbd_USER` / `JZ_mbd_TOKEN` / `BILLING_GATEWAY`（noop|mbd）
