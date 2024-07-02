INSERT INTO JobsOpening_temp (JobID, job_externalRef, job_title, job_desc, salary, date_posted, date_closing, job_url, page_html, JobSource, DateRetrieved, Location, company_name)
SELECT
    (SELECT IFNULL(MAX(JobID), 0) + 1 FROM JobsOpening_temp),
    "3921722563",
    "Database Migration Specialist / DBA - AWS Engineering",
    # JOB DESC
    "bout the job
About Us

Mantel Group is an Australian-owned technology consulting business with capabilities across Cloud, Digital, Data, Delivery & Security. Since our inception in November 2017, we have experienced remarkable growth across Australia & New Zealand and are honoured to be recognised as a Great Place to Work for 5 years in a row!

We hire smart and talented people and get out of their way. As a principle-based organisation we have a flat structure with no hierarchy. By focusing on our five principles and not getting caught up in red tape, we trust you to get the job done!

Mantel Group’s dedicated cloud capability means you are able to work with a team of passionate people and all the latest tech in your cloud of choice whether you want to help businesses reach their full potential with Microsoft products, be part of the full cloud transformation on AWS or an expert in Google cloud - there’s an opportunity here for you.

About The Role

We are looking for passionate consultants to help us grow Mantel Group’s reputation in the marketplace by delivering high quality consulting services to our clients.

As a Database Migration Specialist / DBA in our AWS Engineering team, you'll be responsible for migrating the database workloads to AWS including providing technical expertise for design, deployment and support for cloud database onboarding and migration projects.

You’ll use your RDBMS knowledge to assess, design, modernise and migrate to the best fit AWS backed solutions from on-premise or hosted solutions. You’ll be a key member of the Cloud Adoption team, helping our clients adopt modern AWS environments and operating models. You will build trusted relationships with our clients to effectively deliver the database modernization/migration including enabling our client’s teams through mentoring and guidance.

Your day to day

Provide consulting services that combine architectural vision with hands-on technical experience using some of the latest cloud technologies and methods
Be responsible for the assessment, build architecture and migration of applications and data specialising in databases and data platforms to strategic platforms, specifically AWS
Work closely with technology teams and applications teams to coordinate migrations while ensuring minimal disruption to our client’s business
Manage the upgrading of databases and associated infrastructure as needed to support the desired migration outcomes
Design, develop, build and operate sophisticated and highly automated secure AWS and hybrid infrastructure that adheres with industry compliance standards
Use software development, DevOps and Continuous Integration methods to build, configure and manage the infrastructure
Define and drive new architectures based on the applicable regulatory compliance standards and work with multiple stakeholders to gain endorsement
Perform troubleshooting, analysis and resolve issues as needed to achieve project outcomes
Liaise with the project team, clients, vendors and stakeholders using multiple communication channels to manage the delivery of the project
Establish and maintain relationships with clients as a source of informed, reliable, professional advice about solution options based on the consultant’s specific skills and knowledge.
Willingness to continually upskill; including learning new technologies and obtaining new certifications
Build, recognise and promptly advise Mantel Group management of potential follow-on business opportunities


What You’ll Need To Be Successful

Experience migrating SQL and/or Oracle databases to the cloud working with AWS services such as DMS, SCT, RDS, VPC, EC2, DynamoDB and Aurora (note, not all required)
Demonstrated experience in Microsoft SQL Server and/or Oracle commercial database technologies on AWS as well as physical and virtualized servers
Demonstrated experience in driving deep-dive assessments of Microsoft SQL Server and/or Oracle databases to build recommendations on optimisation and cost benefits.
Demonstrated technical knowledge managing various versions of Microsoft SQL Server and/or Oracle environments to support upgrades across different applications with minimal disruption to end users
Demonstrated experience in using automation to achieve repeatable tasks (deployment, configuration, migration etc. using SQL, Python, CloudFormation, Terraform etc.)
Understanding of Oracle and SQL server licensing models


What you can expect from us:

We know you won’t have one job for life. At Mantel Group we believe in supporting our team to take their career in a direction that aligns with their passions. We have internal opportunities across Cloud, Data, Digital, Delivery & Security.
You’ll get all the tools you need to hit the ground running including a new phone, laptop & swag. 
We believe in unique experiences for all. Our My Deal program allows you to tailor your yearly plan, with the support of your Leader, to decide on what’s most important to you. That might be extra professional development, extra annual or parental leave, time to work on your side hustle, or something else completely different! One size does not fit all. 
You’ll be genuinely supported by an organisation that cares about not only you but your family as well, Mantel Group offers Flexible Personal Leave options for those unplanned moments in life.
We support a flexible hybrid approach to working which is guided by our principles; we trust each other to “make good choices” about the best workplace locations for the requirements of the project, role and client. This can change based on our client needs.


Click ‘Apply’ to be considered for this role and our Talent team will be in touch.

We value a diverse workplace and strongly encourage people from all backgrounds and minority groups to apply.", 
    # Salary
    Null,
    # Date_posted
    "2024-07-02",
    # Date_closing
    NULL,
    "https://www.linkedin.com/jobs/view/3953791146",
    # page_html
    "",
    # JobSource
    "LinkedIn",
    # DataRetrieved
    "2024-07-02",
    # Location
    "Melbourne",
    # Company
    "Mantel Group";