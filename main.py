# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 23:15:05 2024

@author: Sunny
"""

import time
import mysql.connector as mysql
from bs4 import BeautifulSoup as beautifulsoup
import re
from scrapeFunctions import *
from datetime import datetime

# Get sql connection credential
with open(r'../credential/DBlogin.txt') as f: 
    d = dict([line.strip('\n').split(' ', 1) for line in f]) 


def sql_connection():
    cnx = mysql.connect(user=d['user'],
                        password=d['password'],
                        host=d['host'],
                        port=d['port'],
                        database=d["database"])


    # Create a cursor object
    cursor = cnx.cursor(buffered=True)    
    return cursor, cnx

def is_dup(jobid, cursor, cnx):
    query = f"SELECT COUNT(*) FROM Jobs_temp WHERE JobexternalID = {jobid}"
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
    

def add_id(job, JobID, cursor, cnx):
    query = "SELECT MAX(JobID) FROM Jobs_temp;"
    
    try:
        cursor.execute(query)
        max_job_id_result = cursor.fetchone()
        max_job_id = max_job_id_result[0] if max_job_id_result[0] is not None else 0
        new_job_id = max_job_id + 1
        
        add_job = """
        INSERT INTO JobsOpengin_temp (job_externalRef, job_title, JobID, DateRetrieved, JobSource, job_url)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        # Assuming job contains the job external ID and name
        job_name = job.get_text(strip=True)  # Assuming job is a BeautifulSoup object

        # Data to be inserted
        job_data = (
            JobID,  # JobexternalID
            job_name,  # JobName
            new_job_id,  # JobID
            datetime.now(),  # DateRetrieved
            'Monash',  # Source
            f'https://careers.pageuppeople.com/513/ci/en/job/{JobID}/'  # URL
        )

        # Execute the SQL statement
        cursor.execute(add_job, job_data)
        
        # Commit the transaction
        cnx.commit()
        print("Job inserted successfully.")
    except mysql.Error as err:
        print(f"Error: {err}")
        cnx.rollback()


def extract_ID(cursor, cnx, credentials_path, driver):
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
                    print(f"jobID {jobID} already exist in DB")
                    continue
                else:
                    add_id(job, jobID, cursor, cnx)
                    job_count_new += 1
        # Check for the "More Jobs" button and click it
        more_jobs_button = soup.find('a', class_='more-link button')
        if more_jobs_button:
            print(f'Processing information on page {n + 1}')
            n += 1
            try:
                driver.get('https://careers.pageuppeople.com/' + soup.find('a', class_='more-link button')['href'])
                time.sleep(5)
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(f"All job openings processed, {job_count} found, {job_count_new} are new")
            break

def main():
        # sql connection and read credential
    cursor, cnx = sql_connection()
    # chrome_driver_path = r"C:\Users\Sunny\Downloads\chromedriver-win64\chromedriver.exe"
    credentials_path = r"..\credential\login.txt"

    chrome_driver_path = r"C:\Users\schu0091\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    driver = setup_driver(chrome_driver_path)

    extract_ID(cursor, cnx, credentials_path, driver)


             
    while(True):
        pass


if __name__ == "__main__":
    main()

