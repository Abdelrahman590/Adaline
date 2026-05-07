import asyncio
from playwright.async_api import async_playwright
import os

async def capture_design(filepath, output_path, width=1080, height=1080):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': width, 'height': height})
        absolute_path = f"file://{os.path.abspath(filepath)}"
        await page.goto(absolute_path)
        # Wait for fonts to load
        await asyncio.sleep(2)
        await page.screenshot(path=output_path, full_page=True, omit_background=True)
        await browser.close()

async def main():
    # Logo
    if os.path.exists('src/logo.html'):
        print("Capturing logo...")
        await capture_design('src/logo.html', 'assets/logo.png', width=800, height=800)
        await capture_design('src/logo_dark.html', 'assets/logo_dark.png', width=800, height=800)

    # Social Media Post
    if os.path.exists('src/social_post.html'):
        print("Capturing social media post...")
        await capture_design('src/social_post.html', 'assets/social_post.png', width=1080, height=1080)

if __name__ == "__main__":
    asyncio.run(main())
