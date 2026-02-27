import re
from playwright.sync_api import sync_playwright

seeds = range(35, 45)

total = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
        page.goto(url)
        page.wait_for_selector("table")

        text = page.inner_text("table")
        nums = [int(x) for x in re.findall(r"-?\d+", text)]
        total += sum(nums)

    browser.close()

print("TOTAL:", total)
