INSERT INTO JobsOpening_temp (JobID, job_externalRef, job_title, job_desc, salary, date_posted, date_closing, job_url, page_html, JobSource, DateRetrieved, Location, company_name)
SELECT
    (SELECT IFNULL(MAX(JobID), 0) + 1 FROM JobsOpening_temp),
    "3978056763",
    "Data Warehouse Developer",
    # JOB DESC
    "", 
    # Salary
    Null,
    # Date_posted
    "2024-07-17",
    # Date_closing
    null,
    "https://www.linkedin.com/jobs/view/3978056763",
    # page_html
    "",
    # JobSource
    "LinkedIn",
    # DataRetrieved
    Current_date(),
    # Location
    "Melbourne",
    # Company
    "Sharp & Carter";