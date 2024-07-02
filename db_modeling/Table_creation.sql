-- JobsOpening Table
CREATE TABLE JobsOpening (
    JobID INT PRIMARY KEY,
    job_externalRef VARCHAR(255),
    job_title VARCHAR(255),
    job_desc TEXT,
    salary DECIMAL(10, 2),
    job_level VARCHAR(50),
    date_posted DATE,
    date_closing DATE,
    job_url VARCHAR(255),
    page_html TEXT,
    scrape_status bit,
    JobSource VARCHAR(50),
    DateRetrieved DATETIME,
    Location VARCHAR(50)
);

CREATE TABLE JobsOpening_temp (
    JobID INT PRIMARY KEY,
    job_externalRef VARCHAR(255),
    job_title VARCHAR(255),
    job_desc TEXT,
    salary DECIMAL(10, 2),
    job_level VARCHAR(50),
    date_posted DATE,
    date_closing DATE,
    job_url VARCHAR(255),
    page_html TEXT,
    scrape_status bit,
    JobSource VARCHAR(50),
    DateRetrieved DATETIME,
	Location VARCHAR(50)
);

-- Job_app Table
CREATE TABLE Job_app (
    JobAppID INT PRIMARY KEY,
    profile_match DECIMAL(5, 2),
    app_status bit,
    app_date DATE,
    JobID INT,
    company varchar(255)
);

-- Company Table
CREATE TABLE Company (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    company_name VARCHAR(255),
    company_url VARCHAR(255),
    contact_person VARCHAR(255),
    contact VARCHAR(255)
);

-- Question Table
CREATE TABLE Questions (
    QID INT PRIMARY KEY AUTO_INCREMENT,
    JobAppID INT,
    Question LONGTEXT, 
    Answer LONGTEXT,
    FOREIGN KEY (JobAppID) REFERENCES Job_app(JobAppID)
);
#ALTER TABLE JobsOpening_temp drop COLUMN page_html LONGTEXT;
# select from JobsOpening_temp where page_html is not null;

ALTER TABLE JobsOpening_temp drop COLUMN page_html;

INSERT INTO JobsOpening (JobID, job_externalRef, job_title, job_url, DateRetrieved, JobSource)
SELECT JobID, job_externalRef, job_title, job_url, DateRetrieved, JobSource
FROM JobsOpening_temp;

