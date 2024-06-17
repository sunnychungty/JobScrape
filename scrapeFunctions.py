# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:51:58 2024

@author: schu0091
"""
import time
from bs4 import BeautifulSoup as beautifulsoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def read_credentials(file_path):
    with open(file_path) as f:
        details = f.read().split("\n")
        username = details[0]
        password = details[1]
        weburl = details[2]
    return username, password, weburl

def setup_driver(chrome_driver_path):
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login_to_website(driver, url, username_id, password_id, submit_button_id, username, password):
    driver.get(url)

    username_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, username_id))
    )
    username_field.send_keys(username)

    password_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, password_id))
    )
    password_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

def click_button(driver, button_id):
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, button_id))
    )
    submit_button.click()

def get_page_source(driver, url):
    driver.get(url)
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # Get the page source
    page_source = driver.page_source
    return page_source

def extract_from_page_source(pageHTML):
    soup = beautifulsoup(pageHTML, 'html.parser')
    jobs_container = soup.find('tbody', id='search-results-content')
    jobs = jobs_container.find_all('a', class_='job-link')
