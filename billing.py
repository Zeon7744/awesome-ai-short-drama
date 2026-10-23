"""
awesome-ai-short-drama 收款层 — 爱发电 afdian 网关

定价锚点（与 README 对齐）：
  免费: ¥0 — 浏览素材/在线预览/工具使用，3 部/天
  Pro:  ¥49/月 — 下载完整剧本 + 模板库 + 高级工具
  单次: ¥9.9/部 — 单部剧本完整下载
  企业:  ¥499/月 — 商用授权 + 定制题材 + 红果对接
"""
import os
import time
import uuid
import json
import urllib.request

PAYWALL_RULES = {
    "free":       {"daily_limit": 3, "label": "免费版"},
    "pro":        {"daily_limit": -1, "label": "Pro ¥49/月"},
    "single":     {"daily_limit": 1, "label": "单次 ¥9.9/部"},
    "enterprise": {"daily_limit": -1, "label": "企业 ¥499/月"},
}

_STATE = {"date": "", "count": 0}

def _today():
    return time.strftime("%Y-%m-%d")

def check_access(plan: str = "free", action: str = "download") -> dict:
    """门控：免费版 3 部/天，Pro/企业不限次，单次 1 部/次。"""
    rules = PAYWALL_RULES.get(plan, PAYWALL_RULES["free"])
    limit = rules["daily_limit"]

    if limit == -1:
        return {"allowed": True, "remaining": -1, "reason": ""}

    if _STATE["date"] != _today():
        _STATE["date"] = _today()
        _STATE["count"] = 0

    if _STATE["count"] >= limit:
        return {
            "allowed": False,
            "remaining": 0,
            "reason": f"免费版每日 {limit} 部已用完，升级 Pro 或单次购买解锁",
            "upgrade_url": "https://afdian.com/@Zeon7744",
            "http_status": 402,
        }

    _STATE["count"] += 1
    return {"allowed": True, "remaining": limit - _STATE["count"], "reason": ""}

def get_pricing() -> list[dict]:
    return [
        {"plan": "free", "price": 0, "price_label": "¥0",
         "features": ["浏览素材", "在线预览", "3 部/天"]},
        {"plan": "pro", "price": 49, "price_label": "¥49/月",
         "features": ["下载完整剧本", "模板库", "高级工具"]},
        {"plan": "single", "price": 9.9, "price_label": "¥9.9/部",
         "features": ["单部剧本完整下载"]},
        {"plan": "enterprise", "price": 499, "price_label": "¥499/月",
         "features": ["商用授权", "定制题材", "批量下载", "红果对接"]},
    ]

class NoopGateway:
    name = "noop"
    def create_order(self, tenant_id, amount_cents, product, plan, order_meta=None):
        return {"order_id": "noop_" + str(uuid.uuid4())[:12], "status": "created", "gateway": "noop"}
    def query_callback(self, order_id):
        return {"order_id": order_id, "status": "unpaid", "paid": False}
    def refund(self, order_id, amount_cents, reason=""):
        return {"order_id": order_id, "ok": True}

class AfdianGateway:
    name = "afdian"
    DEFAULT_BASE = "https://afdian.com/api"
    def __init__(self):
        self.user_id = os.environ.get("JZ_AFDIAN_USER", "")
        self.token = os.environ.get("JZ_AFDIAN_TOKEN", "")
        self.base = os.environ.get("JZ_AFDIAN_BASE", self.DEFAULT_BASE)

    def _post(self, path, payload):
        body = dict(payload)
        if self.token:
            body["token"] = self.token
        req = urllib.request.Request(f"{self.base}{path}",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def create_order(self, tenant_id, amount_cents, product, plan, order_meta=None):
        if not self.user_id or not self.token:
            return {"order_id": "pending", "status": "created_pending_key",
                    "needs_secret": ["JZ_AFDIAN_USER", "JZ_AFDIAN_TOKEN"]}
        price = round(amount_cents / 100.0, 2)
        out_trade_no = "drama_" + str(uuid.uuid4())[:16]
        payload = {"user_id": self.user_id, "price": str(price),
                   "name": f"short-drama({plan})"[:42], "out_trade_no": out_trade_no}
        try:
            result = self._post("/payment/create", payload)
            if result.get("code") != 0:
                return {"order_id": out_trade_no, "status": "gateway_rejected", "code": result.get("code")}
            return {"order_id": out_trade_no, "status": "created",
                    "pay_url": result.get("data", {}).get("url", ""), "gateway": "afdian"}
        except Exception as e:
            return {"order_id": out_trade_no, "status": "gateway_error", "error": str(e)}

    def query_callback(self, order_id):
        if not self.user_id or not self.token:
            return {"order_id": order_id, "status": "pending_key", "paid": False}
        payload = {"user_id": self.user_id, "out_trade_no": order_id}
        try:
            result = self._post("/payment/query", payload)
            data = result.get("data", {})
            return {"order_id": order_id, "paid": data.get("status") in ("paid", "success")}
        except Exception as e:
            return {"order_id": order_id, "paid": False, "error": str(e)}

    def refund(self, order_id, amount_cents, reason=""):
        if not self.user_id or not self.token:
            return {"order_id": order_id, "ok": False}
        price = round(amount_cents / 100.0, 2)
        try:
            self._post("/payment/refund", {"user_id": self.user_id, "out_trade_no": order_id, "price": str(price)})
            return {"order_id": order_id, "ok": True}
        except Exception as e:
            return {"order_id": order_id, "ok": False, "error": str(e)}

_REGISTRY = {"noop": NoopGateway, "afdian": AfdianGateway}
def get_gateway(name=None):
    return _REGISTRY.get(name or os.environ.get("BILLING_GATEWAY", "noop"), NoopGateway)()

def create_order_for_plan(tenant_id, plan, product="short-drama"):
    g = get_gateway()
    prices = {p["plan"]: p["price"] for p in get_pricing()}
    return g.create_order(tenant_id, int(prices.get(plan, 0) * 100), product, plan)
