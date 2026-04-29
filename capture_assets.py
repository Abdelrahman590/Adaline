import os
from playwright.sync_api import sync_playwright

def capture_designs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Capture Logo
        logo_path = os.path.abspath("logo.html")
        page.goto(f"file://{logo_path}")
        # Wait for fonts and rendering
        page.wait_for_timeout(1000)
        # Select the logo container for a tight crop or just capture full page if centered
        container = page.locator(".logo-container")
        container.screenshot(path="assets/logo.png", scale="device")
        print("Captured assets/logo.png")

        # Capture Social Media Post
        post_path = os.path.abspath("post.html")
        page.goto(f"file://{post_path}")
        # Set viewport to the post size (1080x1080)
        page.set_viewport_size({"width": 1080, "height": 1080})
        page.wait_for_timeout(1000)
        page.screenshot(path="assets/social_post.png", full_page=True, scale="device")
        print("Captured assets/social_post.png")

        browser.close()

if __name__ == "__main__":
    if not os.path.exists("assets"):
        os.makedirs("assets")
    capture_designs()
