SET @nextJobAppID = (SELECT IFNULL(MAX(JobAppID), 0) + 1 FROM Job_app);

INSERT INTO Job_app (JobAppID, app_status, app_date, JobID, company, latest_status_update)
VALUES (@nextJobAppID, 
		'Applied', 
		Current_date(), 
		(Select Max(JobID) from JobsOpening_temp), 
		(Select company_name from JobsOpening_temp where JobID = (Select Max(JobID) from JobsOpening_temp)),
        Current_date());

