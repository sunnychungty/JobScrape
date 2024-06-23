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
    
# chrome_driver_path = r"C:\Users\schu0091\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
chrome_driver_path = r"C:\Users\Sunny\Downloads\chromedriver-win64\chromedriver.exe"

driver = setup_driver(chrome_driver_path)    
driver.get("https://www.seek.com.au/jobs/in-All-Melbourne-VIC")
html_source = driver.page_source
soup = beautifulsoup(html_source, 'html.parser')

containers = soup.find_all('article', class_ = "y735df0 _1iz8dgs6m")

jobs = re.findall(r'data\-job\-id', str(containers))

job_containers = soup.find_all('article', class_='y735df0 y735df1 _1iz8dgs7i _1iz8dgs6e _1iz8dgs9q _1iz8dgs8m _1iz8dgsh _1iz8dgs66 _1iz8dgs5e _12jtennb _12jtenn9 _12jtenna _94v4w18 _94v4w1b _1iz8dgs32 _1iz8dgs35')



for foo in job_containers:
    job_data = {}
    
    job_data['job_id'] = container.get('data-job-id')
    
    print(job_data)
    

with open (r'../credential/page_source_test.txt') as f:
    doc_ = f.read()
# doc_ = doc_.replace("\n", "")
soup = beautifulsoup(doc_, 'html.parser')

if soup.find('a', class_ = 'more-link button'):
    print(soup.find('a', class_ = 'more-link button')['href'])

#     # print(job.get_text(strip=True))
#     # print(job['href'])
cursor, cnx = sql_connection()

