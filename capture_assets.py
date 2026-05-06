import os
from playwright.sync_api import sync_playwright

def capture():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Ensure assets directory exists
        if not os.path.exists('assets'):
            os.makedirs('assets')

        # Capture Logo
        logo_path = os.path.abspath('src/logo.html')
        page.goto(f'file://{logo_path}')
        # Wait for fonts to load
        page.wait_for_timeout(1000)
        page.locator('#logo-container').screenshot(path='assets/logo.png', omit_background=True)
        print("Captured logo.png")

        # Capture Social Media Post
        social_path = os.path.abspath('src/social_post.html')
        page.goto(f'file://{social_path}')
        page.wait_for_timeout(1000)
        page.locator('#post-container').screenshot(path='assets/social_post.png')
        print("Captured social_post.png")

        browser.close()

if __name__ == "__main__":
    capture()
