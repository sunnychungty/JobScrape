INSERT INTO JobsOpening_temp (JobID, job_externalRef, job_title, job_desc, salary, date_posted, date_closing, job_url, page_html, JobSource, DateRetrieved, Location)
SELECT
    (SELECT IFNULL(MAX(JobID), 0) + 1 FROM JobsOpening_temp),
    "3950688220",
    "Graduate - Data, Strategy & Analytics",
    "",
    "76935",
    "2024-06-17",
    NULL,
    "https://careers.racv.com.au/job/485-Bourke-Street-Melbourne-Graduate-Data%2C-Strategy-&-Analytics/1052738866/",
    "",
    "LinkedIn",
    "2024-07-02",
    "Melbourne";