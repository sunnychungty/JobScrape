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


def input_panel():
    x = input("""What are we Scraping today?
              1. All
              2. Monash
              3. Unimelb
              4. Seek
              5. Get page Source
              6. Scrape page Source
              7. Everything
              """)
    return x

def get_page_source(cursor, cnx, driver):
    query = """
            SELECT JobID, job_url FROM JobsOpening_temp WHERE page_html IS NULL AND JobSource <> "Monash" LIMIT 1
            """
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        jid, jurl = result
        driver.get(jurl)
        
        html_source = driver.page_source
        soup = beautifulsoup(html_source, 'html.parser')
      
        html_ = str(soup)
        
        update_query = """
                       UPDATE JobsOpening_temp 
                       SET page_html = %s
                       WHERE JobID = %s
                       """
        
        cursor.execute(update_query, (html_, jid))
        cnx.commit()
    else:
        print("No job found matching the criteria.")
    

def main():
    # SQL connection and read credential
    open_msg()
    cursor, cnx = sql_connection(d)
    credentials_path = r"..\credential\login.txt"
    chrome_driver_path = r".\driver\chromedriver-win64\chromedriver.exe"
    
    while True:
        x = input_panel()

        driver = setup_driver(chrome_driver_path)    
        
        if x == "1":
            extract_Monash_ID(cursor, cnx, credentials_path, driver)
            extract_Seek_ID(cursor, cnx, driver)
        elif x == "2":
            extract_Monash_ID(cursor, cnx, credentials_path, driver)
        elif x == "4":
            extract_Seek_ID(cursor, cnx, driver)
        elif x == "5":
            while True:
                get_page_source(cursor, cnx, driver)
        elif x == "6":
            while True:
                scrape_html(cursor, cnx)
        elif x == "7":
            extract_Seek_ID(cursor, cnx, driver, all_categories=True)
        else:
            pass

if __name__ == "__main__":
    main()

