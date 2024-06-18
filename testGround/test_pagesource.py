# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 01:07:55 2024

@author: Sunny
"""

import time
import mysql.connector as mysql
from bs4 import BeautifulSoup as beautifulsoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver(chrome_driver_path):
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def main():
    # Path to the credentials file and ChromeDriver executable
    chrome_driver_path = r"C:\Users\Sunny\Downloads\chromedriver-win64\chromedriver.exe"

    driver = setup_driver(chrome_driver_path)

    # try:
    # URL and element IDs for the login process
    driver.get("https://google.com")
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    print(driver.page_source)
    
    
if __name__ == "__main__":
    main()
    
with open (r'../credential/page_source_test.txt') as f:
    doc_ = f.read()
# doc_ = doc_.replace("\n", "")
soup = beautifulsoup(doc_, 'html.parser')

if soup.find('a', class_ = 'more-link button'):
    print(soup.find('a', class_ = 'more-link button')['href'])


jobs_container = soup.find('tbody', id='search-results-content')

# # Find all job links within the container
jobs = jobs_container.find_all('a', class_='job-link')

# # # Print the job links
for job in jobs:
    jobID_match = re.search(r'\/job\/(\d+)\/', str(job))
    jobID = jobID_match.group(1)
    print(jobID)

#     # print(job.get_text(strip=True))
#     # print(job['href'])
cursor, cnx = sql_connection()

if is_dup(jobID, cursor, cnx):
    print(f"jobID {jobID} is dup")


jobid = 666172
query = f"SELECT COUNT(*) FROM Jobs_temp WHERE JobexternalID = {jobid}"
print(query)
cursor.execute(query)
result = cursor.fetchone()
if result[0] > 0:
    print('yes')