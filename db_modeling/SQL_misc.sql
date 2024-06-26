ALTER TABLE Job_app
ADD app_date DATE;

INSERT INTO Job_app (JobID, app_status, app_date)
VALUES (989, "Applied", "27/06/2024");

INSERT INTO JobsOpening (JobID, job_externalRef, job_title, job_desc, salary, job_level, date_posted, date_closing, job_url, page_html, DateRetrieved, JobSource)
SELECT 
    j.JobID, 
    j.job_externalRef, 
	j.job_title, 
    j.job_desc, 
    j.salary, 
    j.job_level, 
    j.date_posted, 
    j.date_closing, 
    j.job_url, 
    j.page_html, 
    j.DateRetrieved, 
    j.JobSource
FROM 
    JobsOpening_temp j
LEFT JOIN 
    JobsOpening ja 
ON 
    j.JobID = ja.JobID
WHERE 
    ja.JobID IS NULL;


UPDATE Job_app
SET app_status = 'Applied'
WHERE JobID = 989;

select * from Job_app;

ALTER TABLE Job_app MODIFY COLUMN app_status VARCHAR(20);