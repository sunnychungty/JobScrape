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