# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 23:15:05 2024

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


def main():
    # Path to the credentials file and ChromeDriver executable
    credentials_path = r"..\credential\login.txt"
    chrome_driver_path = r"C:\Users\Sunny\Downloads\chromedriver-win64\chromedriver.exe"

    # Read credentials from file
    myusername, mypassword, url = read_credentials(credentials_path)

    # Set up the driver
    driver = setup_driver(chrome_driver_path)

    # try:
    # URL and element IDs for the login process
    username_id = "input28"
    password_id = "input36"
    submit_button_id = "preferences_prompt_submit"

    # Log in to the website
    login_to_website(driver, url, username_id, password_id, submit_button_id, myusername, mypassword)

    # Wait for the next page to load
    time.sleep(10)

    # Print the title of the next page to verify
    print(driver.title)

    # Click the submit button
    click_button(driver, submit_button_id)
        
    pageHTML = driver.page_source
    
    soup = beautifulsoup(pageHTML, 'html.parser')
    
    print("\n",
                  "======================= PROFILE RESULTS =========================")
    
    # return experiences 

        
        
    while(True):
        pass
    # finally:
    #     # Close the driver
    #     driver.quit()


if __name__ == "__main__":
    main()


# soup = beautifulsoup(pageHTML, 'html.parser')
# jobs_list = soup.find('tbody', id='search-results-content')
# jobs = jobs_list.find_all('a', class_ = 'job_link')



# jobs_container = soup.find('tbody', id='search-results-content')

# # Find all job links within the container
# jobs = jobs_container.find_all('a', class_='job-link')

# # Print the job links
# for job in jobs:
#     print(job)
#     print(job.get_text(strip=True))
#     print(job['href'])