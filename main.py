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
from datetime import *
with open(r'../credential/DBlogin.txt') as f: 
    d = dict([line.strip('\n').split(' ', 1) for line in f]) 

cnx = mysql.connect(user=d['user'],
                    password=d['password'],
                    host=d['host'],
                    port=d['port'],
                    database=d["database"])


# Create a cursor object
cursor = cnx.cursor(buffered=True)

# SQL statement to insert a new row into the Jobs table
add_job = """
INSERT INTO Jobs (JobexternalID, JobName, JobID, DateRetrieved, Source, URL)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Data to be inserted
job_data = (
    3,  # JobexternalID
    'Database Administrator',  # JobName
    98765,  # JobID
    datetime.now(),  # DateRetrieved
    'CompanySite',  # Source
    'https://example.com/job/98765'  # URL
)

try:
    # Execute the SQL statement
    cursor.execute(add_job, job_data)
    
    # Commit the transaction
    cnx.commit()
    print("Job inserted successfully.")
except mysql.Error as err:
    print(f"Error: {err}")
    cnx.rollback()
finally:
    # Close the cursor and connection
    cursor.close()
    cnx.close()



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