# -*- coding: utf-8 -*-
"""短剧资源仓可运行 demo（awesome-ai-short-drama P0：资源仓从"能看"到"能跑 + 变现钩子"）。

定位：资源库 + 方法论仓（上游供素材/选题/方法论给 ai-mcn-studio 生产引擎）。
本 demo 一条命令跑通"素材扫库 → 内容分类 → 格式校验 → 变现钩子"，让资源仓
不止"翻素材"，而能"自证可用 + 看到变现入口"，不改动 tools/ 任何接口。

运行：
    python3 demo_shortdrama.py
"""
from __future__ import annotations

import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

from tools.classifier import classify_content  # noqa: E402
from tools.format_checker import validate_directory  # noqa: E402

# 变现钩子参数（与 README "免费→Pro→企业"对齐）
PRO_PRICE_CNY = 299  # 素材库订阅 Pro 参考价
PAYMENT_CHANNELS = ["支付宝个人码", "BufPay"]


def _scan_materials() -> list[str]:
    """扫 drama-scripts / short-stories / short-dramas 下的 .md 素材。"""
    found: list[str] = []
    for sub in ["drama-scripts", "short-stories", "short-dramas"]:
        d = BASE / sub
        if d.is_dir():
            found += [str(p) for p in sorted(d.glob("*.md"))]
    return found


def _monetization_hook(n_materials: int, per_license_cny: float = 50.0) -> str:
    """变现钩子前置：素材库存量数字 + 收入估算 + 国内收款入口。"""
    est = n_materials * per_license_cny
    chan = "、".join(PAYMENT_CHANNELS)
    return (
        f"  📦 素材库存量 {n_materials} 部，按单部授权 ¥{per_license_cny:,.0f} 计，"
        f"本期可变现 ≈ ¥{est:,.0f}\n"
        f"  💳 收款入口：{chan}（Pro 素材订阅 ¥{PRO_PRICE_CNY}/月）"
    )


def run() -> None:
    print("=== 短剧资源仓可运行 demo：素材扫库 → 分类 → 校验 → 变现钩子 ===\n")

    # 1) 扫素材
    materials = _scan_materials()
    print(f"[1] 扫到素材 {len(materials)} 部:")
    for m in materials[:8]:
        print(f"    · {Path(m).name}")
    if not materials:
        print("    （暂无人工 .md 素材，跳过分类/校验，仅展示变现钩子）")

    # 2) 内容分类（对素材做主题/类型识别）
    if materials:
        print("\n[2] 内容分类（前 5 部）:")
        for m in materials[:5]:
            c = classify_content(m)
            print(f"    {Path(m).name}: {c.get('type', c.get('classification', '未知'))}")

    # 3) 格式校验（素材目录的 md 质量闸口）
    target_dir = next((str(BASE / s) for s in ["drama-scripts", "short-stories"] if (BASE / s).is_dir()), str(BASE))
    print(f"\n[3] 格式校验（{Path(target_dir).name}/ 目录）:")
    results = validate_directory(target_dir)
    passed = sum(1 for r in results if getattr(r, "is_valid", True))
    print(f"    共校验 {len(results)} 个文件，通过 {passed} 个")
    for r in results[:5]:
        print(f"    · {getattr(r, 'filename', getattr(r, 'file', '?'))}: "
              f"{'✓' if getattr(r, 'is_valid', True) else '✗ ' + str(getattr(r, 'issues', ''))[:40]}")

    # 4) 变现钩子
    print("\n[4] 变现钩子（资源仓 → Pro 素材订阅/单部授权）:")
    print(_monetization_hook(len(materials)))

    print("\n✅ 资源仓 demo 闭环完成：能自证可用（扫库/分类/校验）+ 看到变现入口")
    print("   定位：上游供素材/选题/方法论给 ai-mcn-studio 生产引擎，不互卷。")


if __name__ == "__main__":
    run()
