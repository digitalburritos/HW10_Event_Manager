# Event Manager Company: Software QA Analyst/Developer
***
### Bio: Software QA Analyst / NJIT Student | Code Name: Digital Burritos
As a newly hired Software QA Analyst/Developer and a student in Informatics, I am embarking on an exciting journey to contribute to our project aimed at developing a secure, robust REST API that supports JWT (JSON Web Token) token-based OAuth2 authentication. This API serves as the backbone of our user management system and will eventually expand to include features for event management and registration.
***
### My Journey Working with Event Manager Project
Through this assignment, I gained significant technical skills in building and testing secure REST APIs using FastAPI, PostgreSQL, and JWT for authentication. One of the key challenges I faced was ensuring robust security practices, particularly with username and password validation. I worked on resolving issues related to enforcing constraints like unique usernames and strong passwords, which helped me deepen my understanding of security best practices. Additionally, I increased the project's test coverage for these cases to 90% by writing automated tests with pytest, ensuring the API’s functionality was well-tested. Debugging issues, particularly related to user profile updates and OAuth token generation, also sharpened my problem-solving skills and taught me how to effectively trace and fix bugs in a complex system.

From a collaborative perspective, I learned the importance of version control and Software Development Life Cycle in a dev ops environment. I worked with GitHub for branching, pull requests, merging, and code linking, which helped me appreciate the value of clear communication and code quality. One of the challenges was managing conflicts and ensuring that my contributions aligned with the project's goals. However, through frequent code reviews, helpful resources, and in class discussions, I gained insights into how collaborative practices improve code quality and reduce errors. This assignment has not only enhanced my technical expertise but also reinforced the significance of effective collaboration and continuous learning in software development.
***
### Issues Tackled and Closed 
For easy access to the work completed during this project, you can view the closed issues linked below:

- [Issue #1: Fixing Error 500 When Creating User](https://github.com/digitalburritos/hw10_event_manager/issues/1)
- [Issue #2: Fixing Nickname Mismatch in DB](https://github.com/digitalburritos/hw10_event_manager/issues/2)
- [Issue #3: Fixing Null URL in Response Body](https://github.com/digitalburritos/hw10_event_manager/issues/4)
- [Issue #4: Creating Username Validation](https://github.com/digitalburritos/hw10_event_manager/issues/6)
- [Issue #5: Creating Password Validation](https://github.com/digitalburritos/hw10_event_manager/issues/8)
- [Issue #6: Creating Pytest Coverage](https://github.com/digitalburritos/hw10_event_manager/issues/10)
***
### Setup Instructions
1. Fork my repository using GitHub to create your testing repo in your account 

2. Clone fork locally to your machine using   
`git clone git@github.com:your_user/your_repo.git`

3. Configure `production.yml` for your dockerhub then create a `.env` file with this structure to add your http://mailtrap.io account inbox. Be sure to populate the username and password:    
`smtp_server=sandbox.smtp.mailtrap.io`  
`smtp_port=2525`  
`smtp_username=`  
`smtp_password=`

4. Start and build a multi-container application with this command:  
`docker compose up --build`

5. Goto http://localhost/docs to view openapi spec documentation
- Click `Authorize`   
- Input username: `admin@example.com` 
- Input password: `secret`

6. Goto http://localhost:5050 to connect and manage the database.
The following information must match the ones in the docker-compose.yml file.    
- Login:  
Email address / Username: `admin@example.com`  
Password: `adminpassword`  

- Add new server:  
Host name/address: `postgres`  
Port: `5432`  
Maintenance database: `myappdb`  
Username: `user`  
Password: `password` 
 
7. Test API and cross reference DB
***
### Pytest Note (PLEASE READ THIS SECTION FULLY BEFORE TESTING)
- When running pytests inside the containers you can use this command to run all tests:  
`docker compose exec fastapi pytest`
- You can also run a single test file with this command:  
`docker compose exec fastapi pytest tests/test_pass_val.py`

###  Keep in mind that the user data in the DB will be dropped. To ensure you can use the application again without running into Internal Error on openapi, do this:
1. Go to http://localhost:5050 and delete the `alembic_version` table

2. Run the container  
`docker compose up --build`

3. While the container is running, apply database migrations in a split terminal using this command:  
`docker compose exec fastapi alembic upgrade head`

- Now you will be able to Authorize your login to connect to your DB use the methods in the openapi http://localhost/docs
