import os
from playwright.sync_api import sync_playwright

def capture_assets():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        src_dir = 'src'
        assets_dir = 'assets'

        if not os.path.exists(assets_dir):
            os.makedirs(assets_dir)

        for filename in os.listdir(src_dir):
            if filename.endswith('.html'):
                file_path = os.path.abspath(os.path.join(src_dir, filename))
                output_path = os.path.join(assets_dir, filename.replace('.html', '.png'))

                print(f"Capturing {file_path} to {output_path}...")

                page.goto(f"file://{file_path}")

                # Wait for any potential fonts or animations to load
                page.wait_for_timeout(1000)

                if filename == 'social_post.html':
                    # Set viewport to 1080x1080 for social media post
                    page.set_viewport_size({"width": 1080, "height": 1080})
                    page.screenshot(path=output_path, full_page=False)
                elif filename == 'logo.html':
                    # Capture the logo with a transparent background if possible,
                    # or just a clean capture.
                    # Usually better to capture just the element or a small viewport
                    logo_element = page.query_selector('.logo-container')
                    if logo_element:
                        logo_element.screenshot(path=output_path, omit_background=True)
                    else:
                        page.screenshot(path=output_path, full_page=True, omit_background=True)
                else:
                    page.screenshot(path=output_path, full_page=True)

                print(f"Done capturing {filename}.")

        browser.close()

if __name__ == "__main__":
    capture_assets()
