
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

- Build Docker Image and Run Container

    ```bash
    # If the expected image does not exist then docker-compose will build a new image from DockerFile
    # Any future changes on the DockerFile will need to be manually build ($ docker-compose build) prior to executing the command below
    # Note that 'docker-compose' handles automatic image and container builds on all code changes except if the DockerFile changes.
    $  docker-compose up
    ```


#### Deployment Development

Docker and Heroku are utilized for Continuous Integration and Development (CI/CD) 

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

- Option 1: Manually build and deploy the images to Heroku
  
    ```bash
    # builds docker container on heroku container registry
    $ heroku container:push web --app patient-visit-model
  
    # release the image to the app
    $ heroku container:release web --app patient-visit-model
  
    # opens web application on browser
    $ heroku open --app patient-visit-model
    ```
  
- Option 2: Automatic Deployment - Heroku handles building the Docker Images



