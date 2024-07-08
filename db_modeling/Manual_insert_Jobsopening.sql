INSERT INTO JobsOpening_temp (JobID, job_externalRef, job_title, job_desc, salary, date_posted, date_closing, job_url, page_html, JobSource, DateRetrieved, Location, company_name)
SELECT
    (SELECT IFNULL(MAX(JobID), 0) + 1 FROM JobsOpening_temp),
    "3954051542",
    "Data Analyst",
    # JOB DESC
    "Join this fast growing data and information services organisation as an Operations Data Analyst to provide analytics and insights, supporting the creation and maintenance of dashboards, scorecards, and identifying key areas of opportunity.

Key accountabilities

Conduct in-depth analysis of business requirements and collaborate with stakeholders to define project objectives and scope
Act as a liaison between business and technical teams, ensuring alignment and delivering solutions that meet business objectives
Develop, investigate, analyse, validate, and review operations functions
Facilitate workshops to clarify and negotiate business outcomes.
Establish and maintain collaborative networks with business and other stakeholders
Elicit and document business requirements using a variety of business analysis techniques
Prepare and/or update business documents such as Policies, procedures, process maps, guidelines, work instructions, FAQs intranet content and similar
Perform advanced analytics of various aspects of operations, monitors trends, and reports findings
Collect and utilise operational and benchmarking data to recommend targets for improvements in customer service, productivity, and control of costs
Produce monitoring reports and/or performance scorecards
Prepare appropriate reports and statistics and conducts surveys to evaluate departmental operational and fiscal performance
Performs root cause analysis to understand the performance of programs and identifies opportunities for improvements
Skills, experience, and knowledge

Experience in supporting business critical systems and applications
Demonstrated experience and understanding of operational management, data and system processes
Substantial knowledge and understanding relational database structures
Advanced understanding of scripting (SQL, PowerShell, Power Automate, Ad-Hoc script)
Strong uunderstanding of data flows, and integrations across various systems and applications
Knowledge of various integration methods (API and XML)
Excellent data analytics/dashboard reporting experience (Power BI, SSRS and Tableau)
Exceptional communication skills, both written and verbal
Highly organised, flexible and ability to work under pressure
Excellent troubleshooting and problem solving skills
Apply now to secure an interview or contact Samantha Hogan on 9236 7786 for a confidential discussion.", 
    # Salary
    Null,
    # Date_posted
    "2024-06-26",
    # Date_closing
    null,
    "https://www.linkedin.com/jobs/view/3954051542",
    # page_html
    "",
    # JobSource
    "LinkedIn",
    # DataRetrieved
    Current_date(),
    # Location
    "Melbourne",
    # Company
    "Talent";