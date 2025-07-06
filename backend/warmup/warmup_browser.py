import random

WARMUP_URLS = [
    "https://google.com", "https://facebook.com", "https://youtube.com",
    "https://instagram.com", "https://cloudflare.com", "https://aws.amazon.com",
    "https://azure.microsoft.com", "https://analytics.google.com",
    "https://twitter.com", "https://fonts.googleapis.com",
    # ... เพิ่มอีก 40+ เว็บ
]

class BrowserWarmupSystem:
    def __init__(self, page):
        self.page = page

    def simulate_human_behavior(self):
        self.page.mouse.move(random.randint(100, 500), random.randint(100, 500))
        self.page.mouse.click(random.randint(100, 500), random.randint(100, 500))
        self.page.mouse.wheel(0, random.randint(200, 800))
        self.page.keyboard.press("PageDown")
        self.page.wait_for_timeout(random.randint(2000, 5000))

    def warmup(self):
        urls = random.sample(WARMUP_URLS, k=min(10, len(WARMUP_URLS)))
        for url in urls:
            self.page.goto(url, timeout=60000)
            self.page.wait_for_timeout(random.randint(15000, 30000))
            self.simulate_human_behavior()
        return {"status": "completed", "visited": urls}
