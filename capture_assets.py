import os
from playwright.sync_api import sync_playwright

def capture_assets():
    # Ensure assets directory exists
    if not os.path.exists('assets'):
        os.makedirs('assets')

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Capture Logo
        logo_path = os.path.abspath('src/logo.html')
        page.goto(f'file://{logo_path}')
        # Set viewport to capture only the logo area or use selector
        logo_element = page.locator('.logo-container')
        logo_element.screenshot(path='assets/logo.png', omit_background=True)
        print("Logo captured successfully.")

        # Capture Social Media Post
        post_path = os.path.abspath('src/social_post.html')
        page.goto(f'file://{post_path}')
        # Set viewport for 1:1 post
        page.set_viewport_size({"width": 1080, "height": 1080})
        page.screenshot(path='assets/social_post.png')
        print("Social media post captured successfully.")

        browser.close()

if __name__ == "__main__":
    capture_assets()
