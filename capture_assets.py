import os
import asyncio
from playwright.async_api import async_playwright

async def capture_design(page, html_file, output_image, selector=None, viewport=None):
    file_path = f"file://{os.path.abspath(html_file)}"
    if viewport:
        await page.set_viewport_size(viewport)
    await page.goto(file_path, wait_until="networkidle")

    if selector:
        element = await page.query_selector(selector)
        await element.screenshot(path=output_image, omit_background=True)
    else:
        await page.screenshot(path=output_image)
    print(f"Captured {html_file} to {output_image}")

async def main():
    if not os.path.exists("assets"):
        os.makedirs("assets")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Capture Logo
        # Use a specific viewport for the logo or just capture the element
        await capture_design(
            page,
            "src/logo.html",
            "assets/logo.png",
            selector="#logo",
            viewport={"width": 800, "height": 600}
        )

        # Capture Social Media Post
        await capture_design(
            page,
            "src/social_post.html",
            "assets/social_post.png",
            viewport={"width": 1080, "height": 1080}
        )

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
