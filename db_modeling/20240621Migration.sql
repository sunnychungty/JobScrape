INSERT INTO JobsOpening_temp (JobID, job_externalRef, job_title, job_url, JobSource, DateRetrieved)
select JobID, JobexternalID, JobName, URL, Source, DateRetrieved
FROM Jobs_temp;