# Copy temp to JobsOpening
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

# count empty page_html from seek
SELECT count(*) from JobsOpening_temp where page_html is null and JobSource = "Seek";

<<<<<<< HEAD
# select max JobID
SELECT MAX(JobID) from JobsOpening_temp;

#Insert job_desc
UPDATE JobsOpening_temp
set job_desc = """
=======
UPDATE JobsOpening_temp
SET job_desc = '
'
WHERE JobID = 9851;

select * from Job_app order by JobID desc limit 1;
>>>>>>> 40847a355948fdbf511ef131a958e506b5248087

"""
where JobID = "";


<<<<<<< HEAD
=======
SELECT * FROM JobsOpening_temp where job_externalRef = "3918986985";
SELECT * FROM JobsOpening_temp where company_name = "South East Water";
SELECT * FROM JobsOpening_temp where JobID = "2255";


SELECT * FROM JobsOpening_temp order by JobID desc limit 1;


select * from JobsOpening_temp where JobSource = "Monash" and JobID = "667418";
>>>>>>> 40847a355948fdbf511ef131a958e506b5248087

