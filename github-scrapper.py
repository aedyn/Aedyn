# This version just looks for the word "password" but can be moddified to take more than just that argument and add additional arguments and print them

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# https://github.com/usernam121
scrape = input("What page would you like to scrape? ")
cdp = "/home/sket/Documents/chrome-linux64/chrome"
driver = webdriver.Chrome()
driver.get(f"{scrape}")
repo = f"{scrape}"
res = driver.find_elements(By.CLASS_NAME, "repo")

links = []
flink = []

def going_for_raw(second_page):
    driver.get(second_page)
    raw = driver.find_element(By.CLASS_NAME, "LinkButton-module__linkButton__nFnov")
    raw.click()
    html = driver.page_source
    html = f"{html}"
    if "password" in html:
        print(f"Found password {second_page}")

def loop(next_page):
    global a
    driver.get(next_page)
    res2 = driver.find_elements(By.CLASS_NAME, "Link--primary")
    for a in res2:
        if "py" in a.text:
            second_page = f"{next_page}/blob/main/{a.text}"
            going_for_raw(second_page)
for i in res:
    links.append(i.text)

for l in links:
    next_page = f"{repo}/{l}"
    flink.append(next_page)
    loop(next_page)

driver.quit()
