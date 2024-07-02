SET @nextJobAppID = (SELECT IFNULL(MAX(JobAppID), 0) + 1 FROM Job_app);

INSERT INTO Job_app (JobAppID, app_status, app_date, JobID, company)
VALUES (@nextJobAppID, 'Rejected', '2024-06-27', '989', 'NAB');


UPDATE Job_app
SET app_status = "Rejected"
WHERE JobAppID = 1;
