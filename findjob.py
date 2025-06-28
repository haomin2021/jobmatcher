from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_stepstone_jobs_selenium(query="arzt", location="heidelberg", pages=3):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    all_jobs = []

    for page in range(1, pages + 1):
        url = f"https://www.stepstone.de/jobs/{query}/in-{location}?page={page}"
        print(f"🔍 Fetching Page {page} ...")
        driver.get(url)
        time.sleep(4)  # 等待 JS 加载

        soup = BeautifulSoup(driver.page_source, "lxml")
        jobs = []

        for tag in soup.find_all("article"):
            title_tag = tag.find("a", attrs={"data-at": "job-item-title"})
            if title_tag:
                title = title_tag.get_text(strip=True)
                link = "https://www.stepstone.de" + title_tag.get("href")
                jobs.append((title, link))

        print(f"✅ Page {page}: {len(jobs)} jobs found.")
        all_jobs.extend(jobs)

    driver.quit()
    return all_jobs

# 执行脚本
results = get_stepstone_jobs_selenium(pages=3)
print(f"\n🎯 Total jobs found: {len(results)}\n")

for title, link in results:
    print(title)
    print(link)
    print("-----")