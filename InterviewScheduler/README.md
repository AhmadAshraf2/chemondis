# Interview Scheduling API


## SUMMARY

The API is built using REST standard and contains the below mentioned endpoints

1. View all time slots (Interviewer, candidiate=).
2. Create a time slot.
3. Get Available time slots for multiple users.
 

## TOOLS USED.

API is built using Django DRF, and PostgreSQL.

Docker containers are used for development environment.

Swagger has been configured with Django to access and test the endpoints.


## ASSUMPTIONS AND IMPROVEMENTS:

As for the time being Django's default user model is used. Since scheduling an interview between interviewer and candidate 
is same as scheduling a Interview between 2 regular people, I find it redundant to mark a user as an interviewer or candidate.
If in the future we have use cases where marking type of each user is essential, then we can use Django's Abstract User class

I have not yet implemented Authentication or authorization. which can easily be introduced using django's in-built Session, Token
Authentication.

Django Unit tests can be written to perform extensive testing.

I am not including init.db scripts to populate data in the DB. I have exposed all models on Django admin panel. please enter users
and slots before testing.


## HOW TO RUN:

Please install Docker and Docker-compose on your machine.

Go to the InterviewScheduler folder and run the below command to start docker containers.

        Docker-compose up --build

Docker-compose uses 3 files (placed in /InterviewScheduler/dockers folder) to setup the docker containers. DockerFile contains command 
to setup django_container. 
After the container is setup, we need to make migrations. Bash script entrypoint.sh contains the commands to migrate, 
create django superuser and start the server.

        Superuser username = admin (same for postgres user)
        Superuser password = admin123456 (same for postgres user)

A problem arises where the django_container gets ready before the postgres container and runs the migration commands 
before the database is ready. 
So to solve this, Wait_for_it.sh bash file ensures that the migrations are run after the database is up and ready to entertain requests.

After starting the dockers containers, move to the browser on your host machine and go to the below URL.

        127.0.0.1:8000/docs (swagger)
        127.0.0.1:8000/admin (admin panel)

#### Example data format for Endpoints

1. Get all slot: (takes no arguments).

        url : 127.0.0.1:8000/slot/view/

2.  Create Slot

        URL : 127.0.0.1:8000/slot/create/

        Body : {
          "start_date": "2018-08-08T12:00:00",
          "end_date": "2018-08-08T13:00:00",
          "user": "1"
        }

3. Get Available Slots
        
        URL : 127.0.0.1:8000/slot/interviewslot/
        
        Body : {
          "names": [
            "dave", "ahmad", "ali"
          ]
        }
