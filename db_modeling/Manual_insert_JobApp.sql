SET @nextJobAppID = (SELECT IFNULL(MAX(JobAppID), 0) + 1 FROM Job_app);

INSERT INTO Job_app (JobAppID, app_status, app_date, JobID, company, latest_status_update)
VALUES (@nextJobAppID, 
		'Applied', 
		Current_date(), 
		'2258', 
		(Select company_name from JobsOpening_temp where JobID = "2258"),
        Current_date());


UPDATE Job_app
SET latest_status_update = current_date()
WHERE JobAppID = 6;

select * from JobsOpening_temp order by JobID desc limit 1;

select * from Job_app;