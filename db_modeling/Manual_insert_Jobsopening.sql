INSERT INTO JobsOpening_temp (JobID, job_externalRef, job_title, job_desc, salary, date_posted, date_closing, job_url, page_html, JobSource, DateRetrieved, Location, company_name)
SELECT
    (SELECT IFNULL(MAX(JobID), 0) + 1 FROM JobsOpening_temp),
    "3947478720",
    "Data Engineer ",
    # JOB DESC
    "", 
    # Salary
    Null,
    # Date_posted
    "2024-07-02",
    # Date_closing
    null,
    "https://www.linkedin.com/jobs/view/3947478720",
    # page_html
    "",
    # JobSource
    "LinkedIn",
    # DataRetrieved
    Current_date(),
    # Location
    "Melbourne",
    # Company
    "InfoCentric";