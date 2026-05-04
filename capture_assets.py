import os
from playwright.sync_api import sync_playwright

def capture_assets():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Ensure assets directory exists
        if not os.path.exists('assets'):
            os.makedirs('assets')

        # List of assets to capture
        assets = [
            {'html': 'src/logo.html', 'output': 'assets/logo.png', 'width': 800, 'height': 400},
            {'html': 'src/social_post.html', 'output': 'assets/social_post.png', 'width': 1080, 'height': 1080}
        ]

        for asset in assets:
            html_path = os.path.abspath(asset['html'])
            if os.path.exists(html_path):
                print(f"Capturing {asset['html']}...")
                page.set_viewport_size({"width": asset['width'], "height": asset['height']})
                page.goto(f"file://{html_path}")
                # Wait for fonts to load
                page.evaluate("document.fonts.ready")
                page.screenshot(path=asset['output'], full_page=False, omit_background=True)
                print(f"Saved to {asset['output']}")
            else:
                print(f"Warning: {html_path} not found.")

        browser.close()

if __name__ == "__main__":
    capture_assets()
