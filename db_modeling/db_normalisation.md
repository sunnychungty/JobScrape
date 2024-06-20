# Raw table

## Job openings
Cols:
JobID, job_externalRef, job_title, job_desc, salary, job_level, date_posted, date_closing, company_name, contact_person, Location, Profile match, application_status, Scrape_status, job_url, company_url, page_html, date_retrieved, source

# 1NF
- No repeating groups
## JobsOpening Table
* PK: JobID
JobID, job_externalRef, job_title, job_desc, salary, job_level, date_posted, date_closing, company_name, contact_person, Location, Profile_match, app_status, scrape_status, job_url, company_url, page_html, date_retrieved, source

# 2NF
- Remove repeating group (partial dependencies)
## JobsOpening Table
* PK: JobID
JobID, job_externalRef, job_title, job_desc, salary, job_level, date_posted, date_closing, company_id, Location, Profile_match, app_status, scrape_status, job_url, company_url, page_html, date_retrieved, source

## Company Table
* PK: company_id
company_id, company_name, company_url, contact_person, contact

# 3NF
- Remove data no dependent on key (Transitive dependencies) -> ensuring non-key attributes are not dependent on other non-key attributes
## JobsOpening Table
* PK: JobID
JobID, job_externalRef, job_title, job_desc, salary, job_level, date_posted, date_closing, job_url, page_html, scrape_status

## Job_app
* PK: JobID
JobID, profile_match, app_status, date_retrieved, source

## Company table
* PK: company_id
company_id, company_name, company_url, contact_