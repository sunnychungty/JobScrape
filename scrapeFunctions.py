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
from datetime import datetime

import mysql.connector as mysql

def open_msg():
    print("""
          _         _       _____                                       
         | |       | |     / ____|                                      
         | |  ___  | |__  | (___    ___  _ __   __ _  _ __    ___  _ __ 
     _   | | / _ \ | '_ \  \___ \  / __|| '__| / _` || '_ \  / _ \| '__|
    | |__| || (_) || |_) | ____) || (__ | |   | (_| || |_) ||  __/| |   
     \____/  \___/ |_.__/ |_____/  \___||_|    \__,_|| .__/  \___||_|   
                                                     | |                
                                                     |_|                
    """
    )

                                     
def sql_connection(d):
    cnx = mysql.connect(user=d['user'],
                        password=d['password'],
                        host=d['host'],
                        port=d['port'],
                        database=d["database"])


    # Create a cursor object
    cursor = cnx.cursor(buffered=True)    
    print("Connected to Database")
    
    return cursor, cnx
                                     
                                     
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
    
    return jobs

def is_dup(jobid, cursor, cnx):
    query = f"SELECT COUNT(*) FROM JobsOpening_temp WHERE job_externalRef = {jobid}"
    try:
        # Execute the query
        cursor.execute(query)
        # Fetch the result
        result = cursor.fetchone()
        # Check if count is greater than 0, indicating a duplicate
        if result[0] > 0:
            return True
        else:
            return False
    except mysql.Error as err:
        print(f"Error: {err}")
        return False
    

def add_id(job, JobID, cursor, cnx, jobSource):
    query = "SELECT MAX(JobID) FROM JobsOpening_temp;"
    
    try:
        cursor.execute(query)
        max_job_id_result = cursor.fetchone()
        max_job_id = max_job_id_result[0] if max_job_id_result[0] is not None else 0
        new_job_id = max_job_id + 1
        
        add_job = """
        INSERT INTO JobsOpening_temp (job_externalRef, job_title, JobID, DateRetrieved, JobSource, job_url)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        # Assuming job contains the job external ID and name

        # Data to be inserted
        if jobSource == "Monash":
            job_name = job.get_text(strip=True)  # Assuming job is a BeautifulSoup object
            job_data = (
                JobID,  # JobexternalID
                job_name,  # JobName
                new_job_id,  # JobID
                datetime.now(),  # DateRetrieved
                'Monash',  # Source
                f'https://careers.pageuppeople.com/513/ci/en/job/{JobID}/'  # URL
            )
        else:
            job_data = (
                JobID,  # JobexternalID
                "",  # JobName
                new_job_id,  # JobID
                datetime.now(),  # DateRetrieved
                jobSource,  # Source
                f'https://www.seek.com.au/job/{JobID}'  # URL
            )
        # Execute the SQL statement
        cursor.execute(add_job, job_data)
        
        # Commit the transaction
        cnx.commit()
        print(f"Job: {JobID} inserted successfully.")
    except mysql.Error as err:
        print(f"Error: {err}")
        cnx.rollback()


def extract_Seek_ID(cursor, cnx, driver):
    driver.get("https://www.seek.com.au/jobs/in-All-Melbourne-VIC")
    
    job_count = 0
    job_count_new = 0
    n = 1
    while True:
        html_source = driver.page_source
        soup = beautifulsoup(html_source, 'html.parser')
        
        containers = soup.find_all('article', class_="y735df0")
        
        jobs = re.findall(r'data\-job\-id\=\"(\d+)\"', str(containers))

        for jobID in jobs:
            job_count += 1
            if is_dup(jobID, cursor, cnx):
                print(f"jobID {jobID} already exist in DB")
                continue
            else:
                add_id("", jobID, cursor, cnx, "Seek")
                job_count_new += 1
        if soup.find('span', class_="y735df0 _1iz8dgs8 _1iz8dgs4"):
            print(f'Processing information on page {n + 1}')
            n += 1
            try:
                driver.get(f"https://www.seek.com.au/jobs/in-All-Melbourne-VIC?page={n}")
                time.sleep(5)
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(f"All job openings processed, {job_count} found, {job_count_new} are new")
            break  # Exit the loop when all job openings are processed


def extract_Monash_ID(cursor, cnx, credentials_path, driver):
    myusername, mypassword, url = read_credentials(credentials_path)

    # Set up the driver
    # driver = setup_driver(chrome_driver_path)

    username_id = "input28"
    password_id = "input36"
    submit_button_id = "preferences_prompt_submit"

    # Log in
    login_to_website(driver, url, username_id, password_id, submit_button_id, myusername, mypassword)

    time.sleep(5)

    # Click the submit button
    click_button(driver, submit_button_id)

    job_count = 0
    job_count_new = 0
    
    n = 1
    while True:
        # Get page source and soup
        pageHTML = driver.page_source
        soup = beautifulsoup(pageHTML, 'html.parser')
        jobs_container = soup.find('tbody', id='search-results-content')
    
        # Get job links in one page
        jobs = jobs_container.find_all('a', class_='job-link')

        for job in jobs:
            job_count += 1
            jobID_match = re.search(r'\/job\/(\d+)\/', str(job))
            if jobID_match:
                jobID = jobID_match.group(1)
                if is_dup(jobID, cursor, cnx):
                    print(f"jobID {jobID} already exists in DB")
                    continue
                else:
                    add_id(job, jobID, cursor, cnx, "Monash")
                    job_count_new += 1
        # Check for the "More Jobs" button and click it
        more_jobs_button = soup.find('a', class_='more-link button')
        if more_jobs_button:
            print(f'Processing information on page {n + 1}')
            n += 1
            try:
                driver.get('https://careers.pageuppeople.com/' + more_jobs_button['href'])
                time.sleep(5)
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(f"All job openings processed, {job_count} found, {job_count_new} are new")
            break  # Exit the loop when all job openings are processed