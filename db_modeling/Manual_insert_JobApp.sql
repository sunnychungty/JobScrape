SET @nextJobAppID = (SELECT IFNULL(MAX(JobAppID), 0) + 1 FROM Job_app);

INSERT INTO Job_app (JobAppID, app_status, app_date, JobID, company)
VALUES (@nextJobAppID, 
		'Applied', 
		"2024-07-02", 
		'1526', 
		(Select company_name from JobsOpening_temp where JobID = "1526"));


UPDATE Job_app
SET company = "RACV"
WHERE JobAppID = 3;

select * from Job_app;
