import os
from playwright.sync_api import sync_playwright

def capture_designs():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Ensure assets directory exists
        if not os.path.exists('assets'):
            os.makedirs('assets')

        # Capture Logo
        # For the logo, we want to capture only the logo-wrapper
        logo_path = os.path.abspath('src/logo.html')
        page.goto(f'file://{logo_path}')
        # Wait for fonts to load
        page.wait_for_timeout(2000)
        logo_element = page.query_selector('.logo-wrapper')
        if logo_element:
            logo_element.screenshot(path='assets/logo.png', omit_background=True)
            print("Successfully captured assets/logo.png")
        else:
            print("Could not find .logo-wrapper in logo.html")

        # Capture Social Media Post
        # The social media post is 1080x1080
        post_path = os.path.abspath('src/social_post.html')
        page.set_viewport_size({"width": 1080, "height": 1080})
        page.goto(f'file://{post_path}')
        # Wait for fonts to load
        page.wait_for_timeout(2000)
        page.screenshot(path='assets/social_post.png')
        print("Successfully captured assets/social_post.png")

        browser.close()

if __name__ == "__main__":
    capture_designs()
