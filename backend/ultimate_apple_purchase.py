from backend.warmup.warmup_browser import BrowserWarmupSystem
from backend.browser.stealth_browser import run_stealth_browser
from backend.payment.injector import inject_card_info
from backend.notify.telegram import send_telegram

class UltimateApplePurchaseSystem:
    def __init__(self, task):
        self.task = task
        self.page = None

    def phase_1_warmup(self):
        send_telegram("🔥 เริ่ม Browser Warmup...")
        self.page = run_stealth_browser(self.task, "gemini")
        warmup = BrowserWarmupSystem(self.page)
        warmup_result = warmup.warmup()
        send_telegram(f"✅ Warmup เสร็จ: {warmup_result['visited']}")

    def phase_2_purchase(self):
        send_telegram("🍎 เริ่มสั่งซื้อ iPhone จริง...")
        result = inject_card_info(self.page, self.task['card'])
        send_telegram(f"📦 สถานะการซื้อ: {result['status']}")
        return result

    def phase_3_report(self, result):
        send_telegram("📊 สร้างรายงานการซื้อเรียบร้อย")
        return {"status": "done", "result": result}

    def execute(self):
        self.phase_1_warmup()
        result = self.phase_2_purchase()
        return self.phase_3_report(result)
