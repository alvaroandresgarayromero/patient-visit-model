
# Nurse Workflow Application
This project is a nurse process web application for hospital organizations who would like to optimize their employee workflow. The application at its core utilizes the client-centered care principles of Assessment, Diagnosis, Planning, Implementation, and Evaluation as a baseline of its main features. 

As part of the Full-Stack Udacity Nanodegree Capstone final project, the scope of the nurse process web application will focus on the implementation of the Assessment feature. This feature consists of supporting two user roles: Nurse, and Patient. The Patient role has access to create, update, and delete their own personal information, which consists of their name and age. Likewise, the nurse role has access to create, update, and delete their own personal information, which consists of their name. The Nurse role has access to create, update, and remove an assessment visit. The assessment visit consists of medical objective data such as the vital signs. When all assessments are completed, then both Patient and Nurse roles have access to read the data recorded. 

By completing this project, the student will have had the opportunity to implement all concepts learned throughout the program, which include architecting relational database models in Python, utilizing SQLAlchemy to conduct database queries, following RESTful principles of API development, structuring endpoints to respond to HTTP methods, including error handling, enabling role based authentication and roles-based access control with Autho0 (third-party authentication software as a service API), hosting the application live via Heroku, executing unit test, creating requirements, and documentation of a web API.

## Getting Started

### Development Environment

#### Source Control

GitHub is used to maintain all required files

- Verify git is installed by checking the version. If not, install git.

    ```bash
    $ git --version
    ```

- Fork and then clone the project repository 
  
    ```bash
    $ git clone https://github.com/alvaroandresgarayromero/patient-visit-model.git
    ```

#### Local Development

Docker and Docker-Compose are utilized for local development
 
- Verify Docker is installed by checking the version. If not, install Docker

    ```bash
    $ docker --version
    ```
  
- Verify Docker-Composed is installed by checking the version. If not, install Docker-Composed

    ```bash
    $ docker-composed --version
    ```
  
  #### Execution
  
- Build Docker Image and Run Container

    ```bash
    # If the expected image does not exist then docker-compose will build a new image from DockerFile
    # Any future changes on the DockerFile will need to be manually build ($ docker-compose build) prior to executing the command below
    # Note that 'docker-compose' handles automatic image and container builds on all code changes except if the DockerFile changes.
    $  docker-compose up
    ```
  
    ```bash
    # To enter Docker Container Postgres database
    $ psql -h localhost -p 5432 -d patientnursedb -U postgres --password
      Password: 
  
    # Where the password will be requested. This is defined in the .evn file
    ```
  
    ```bash
    # To enter Docker Container Flask app 
    $ docker exec -it <CONTAINER_NAME> /bin/bash
    ```
  
  #### Verify Server Is Running (Quick Test)

    Input: 
  
    ```bash
    curl http://0.0.0.0:8080/verify_server_is_running
    ```
  
    Output: 
  
    ```json
    {
        "success": true
    }
    ```

#### Deployment Development

Heroku is utilized for Continuous Integration and Development (CI/CD). 
Heroku provides functionality to work with Docker. So, this project takes advantage of this feature.

- Verify Heroku is installed by checking the version. If not, install Heroku CLI

    ```bash
    $ heroku --version
    ```
  
- Create a Heroku account, and then log in to Container Registry

    ```bash
    $ heroku container:login
    ```

- Navigate to the app's directory, and create a Heroku app

    ```bash
    $ heroku create patient-visit-model
    ```

- Create Heroku-Postgres database add-on feature
  
    ```bash
    $ sudo heroku addons:create heroku-postgresql:hobby-dev --app patient-visit-model
    ```
- Verify DATABASE_URL exists - the app uses this URL to access the database.

    ```bash
    # Verify DATABASE_URL exists - the app uses this URL to access the database.
    $ sudo heroku config --app patient-visit-model
    ```
  
    ```bash
    # As of 04/01/2021, the DATABASE_URL can be access in the CLI as
    $ psql -h ec2-52-87-107-83.compute-1.amazonaws.com -p 5432 -d dcaa3dle9k21qs -U ljqndisewszxtw --password
      Password: 
  
      # Where the user password will be requested. This is defined in the DATABASE_URL
    ```
  
  #### Execution

- Step 1: Configure our Heroku application to use Docker by manually building and deploying the image to Heroku.
  
    ```bash
    # builds docker container on heroku container registry
    $ heroku container:push web --app patient-visit-model
  
    # release the image to the app
    $ heroku container:release web --app patient-visit-model
  
    # opens web application on browser
    $ heroku open --app patient-visit-model
    ```
  
- Step 2: Automatic Deployment - Heroku handles building the Docker Images

  - This is enabled with the heroku.yml file (already provided in this workspace). 
  - In Heroku, link your git repository in order to trigger automatic builds.
       
    ```bash
    # push a change to the master branch to test the automatic build.
    # For example, modify the "/verify_server_is_running" endpoint json response
    $ git push
    ```
    
  #### Verify Server Is Running (Quick Test)

    Input (web browser): 
  
    ```bash
    https://patient-visit-model.herokuapp.com/verify_server_is_running
    ```
  
    Output: 
  
    ```json
    {
        "success": true
    }
    ```

## API Reference:

### Getting Started

#### Base URL

- Local Host:
  
    Hosted in a Docker Container as defined by the web service in docker-compose.yml
  
    ```bash
    $ curl http://0.0.0.0:8080/
    ```
  
- Web Host: 
  
    Hosted in Heroku using free web dyno. This means that the app will go to sleep if inactive for 30 minutes. Upon incoming traffic, then it will be woken up after a short delay.

    ```bash
    https://patient-visit-model.herokuapp.com/
    ```
  
#### Authentication (AUTH0)
  
The backend utilizes AUTH0 for application authorization, user permissions, and user information.

AUTH0 is a third party platform that securely manages users, and their private information. 
Thus, allowing us not to worry about managing the security concerns when it comes to keeping users data safe. AUTH0 generated JSON-WEB-TOKEN (JWT) and AUTH0 API enables external applications (us) to interface with them, and utilize these security features.

A JWT is generated upon successful user login by AUTH0. Normally, the frontend (not supported) would provide support to login into AUTH0 LOGIN page.
Upon successful login, the generated JWT is passed to the backend endpoint where it gets decrypted, and then verified with the AUTH0 API to determined if the JWT is healthy, and has not been manipulated/tinkered. 
Upon successful authorization, then the payload data in the JWT is utilized to check whether the user has permission to access the requested end-point. 
In addition, the backend uses the JWT to request the AUTH0 API for more information about the user. 

AUTH0 Configurations:

- Application:
  - Name: PatientVisitModel
  - Domain: $AUTH0_DOMAIN, see autho0/setup.sh
  - Client Secret (autogenerated): $AUTH0_CLIENT_SECRET, see auth0/setup.sh
  - Application Type: Regular Web Application
  - Token Endpoint Authentication Method: POST
  - Application Login URI: https://<frontend_domain>/login
  - Allowed Callback URLs (required to get JWT from URL): https://<frontend_domain>/login-results
  - Allowed Logout URLs: https://<frontend_domain>/logout 

- API:
  - ID (autogenerated): $AUTH0_CLIENT_ID, see auth0/setup.sh
  - Name: PatientVisit  
  - Identifier (autogenerated): $AUTH0_AUDIENCE, see auth0/setup.sh 
  - Enable RBAC: On
  - Add Permissions in the Access Token: On

- Roles
  - Admin: Admin has access to create, edit, delete & update
  - Nurse: Nurse can create Assessment, Diagnosis, Planning, Implementation, and Evaluation of a particular patient. For now, Assessment visit is supported
  - Patient: Patient can view their medical visit information
  
- Permissions: @todo
  - Admin:  
  - Nurse: 
  - Patient:
  
- Active Users:
  - ADMIN_USER:
    - email: admin@nursevisitmodel.com
    - password: Alvaro123
    
  - NURSE_USER:
    - email: nurse@nursevisitmodel.com
    - password: Alvaro123    
    
  - PATIENT_USER_1:
    - email: patient_nursepatientmodel_1@gmail.com
    - password: Alvaro123
    
  - PATIENT_USER_2:
    - email: patient_nursepatientmodel_2@gmail.com
    - password: Alvaro123

Generate and Update JWT token environment variables: 

  - Step 1: The following script will generate the required URL to access the '/authorize' AUTH0 API endpoint in order to create a user JWT token
    
    ```bash
    $ source auth0/auth0_auth_login.sh 
    ```
    
  - Step 2: Copy the URL, and paste it into your desired web-browser. The AUTH0 LOGIN page will load.
  - Step 3: Login with one of the 'Active User' credentials. Upon successful login, AUTH0 will generate a new URL with the JWT token code. 
  - Step 4: Copy the JWT token code into the respective auth0/setup.sh 'token' environment variable
      - $ADMIN_USER | $NURSE_USER | $PATIENT_USER_1 | $PATIENT_USER_2
  
  - Step 5: Set the new environment variable(s)
    
    ```bash
    $ source auth0/setup.sh 
    ```

#### Error Handling

  Errors are returned as JSON objects in the following format:

  ```json
  {
      "success": false, 
      "error": 400,
      "message": "bad request"
  }
  ```

  The API will return three error types when requests fail

   - 400: Bad Request
   - 401: Unauthorized
   - 404: Resource Not Found
   - 422: Not Processable

#### Resource endpoint library

- POST /nurses/create

  - General: 
    - Creates a new nurse user record
  - JSON Request Arguments:
    - name [string] : Name for new nurse
  - Return: 
    - Returns a dictionary with information about the recently created nurse user record, and its newly assigned id.
  
  - Sample Input:
  
    ```bash
    $ curl -X POST http://0.0.0.0:8080/nurses/create -H "Content-Type: application/json" -d '{"name":"Alvaro"}'
    ```
  - Output: 
    
    ```json
    {"id":1,"name":"Alvaro"}
    ```
    
- POST /patients/create

  - General: 
    - Creates a new patient user record
  - JSON Request Arguments:
    - name [string] : Name for new patient
    - age [integer] : Age of user
    - gender [string] : Gender of user
  - Return: 
    - Returns a dictionary with information about the recently created patient record, and its newly assigned id.
  - Sample Input:
  
    ```bash
    $ curl -X POST http://0.0.0.0:8080/patients/create -H "Content-Type: application/json" -d '{"name":"Courtney", "age":27, "gender":"female"}'
    ```
  - Output: 
    
    ```json
    {"id":1, "age":27,"gender":"female","name":"Courtney"}
    ```
    
- GET /nurses/<int: a_id>

  - General: 
    - Fetches a nurse user from the nurse table
  - Variable Rule Arguments:
    - a_id [integer] : Respective ID of the nurse record
  - Return: 
    - Returns a dictionary with information about the nurse record with its assigned id.
  - Sample Input:
  
    ```bash
    $ curl -X GET http://0.0.0.0:8080/nurses/1
    ```
  - Output: 
    
    ```json
    {"id":1,"name":"Alvaro"}
    ```
    
- GET /patients/<int: a_id>

  - General: 
    - Fetches a patient user from the patient table
  - Variable Rule Arguments:
    - a_id [integer] : Respective ID of the patient record
  - Return: 
    - Returns a dictionary with information about the patient record with its assigned id.
  - Sample Input:
  
    ```bash
    $ curl -X GET http://0.0.0.0:8080/patients/1
    ```
  - Output: 
    
    ```json
    {"id":1,"age":27,"gender":"female","name":"Courtney"}
    ```

