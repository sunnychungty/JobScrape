SET @nextJobAppID = (SELECT IFNULL(MAX(JobAppID), 0) + 1 FROM Job_app);

INSERT INTO Job_app (JobAppID, app_status, app_date, JobID, company, latest_status_update)
VALUES (@nextJobAppID, 
		'Applied', 
		Current_date(), 
		'5871', 
		(Select company_name from JobsOpening_temp where JobID = "5871"),
        Current_date());


UPDATE Job_app
SET latest_status_update = CURRENT_DATE 
WHERE JobAppID <6;

select * from Job_app;

alter table Job_app
add column latest_status_update date;

select * from JobsOpening_temp where JobSource = "Seek" and page_html is not null limit 1;
select * from JobsOpening_temp where job_externalRef = 76777468;

ALTER TABLE JobsOpening_temp
MODIFY COLUMN salary VARCHAR(20);

select JobID, page_html from JobsOpening_temp where JobSource = "Seek" and page_html is not null and scrape_status is null limit 1;


select count(*) from JobsOpening_temp where page_html is null and JobSource = "Seek";
SET latest_status_update = current_date()
WHERE JobAppID = 6;

select * from JobsOpening_temp order by JobID desc limit 1;

select * from Job_app;
