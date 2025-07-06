import os
from gologin import GoLogin
from playwright.sync_api import sync_playwright

def run_stealth_browser():
    gl = GoLogin({
        "token": os.getenv("GOLOGIN_API_TOKEN"),
        "profile_id": os.getenv("GOLOGIN_PROFILE_ID")
    })
    debugger_address = gl.start()
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(debugger_address)
        context = browser.new_context(
            proxy={
                "server": f"http://{os.getenv('PROXY_HOST')}:{os.getenv('PROXY_PORT')}",
                "username": os.getenv('PROXY_USER'),
                "password": os.getenv('PROXY_PASS')
            } if os.getenv('PROXY_HOST') else None,
            viewport={"width": 1280, "height": 800}
        )
        page = context.new_page()
        return page
