## Requirements

- [Docker v19+](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [docker-compose v1.23+](https://docs.docker.com/compose/install/)
- [docker-compose via pip](https://pypi.org/project/docker-compose/)
- make

## Set up development environment

We use images of python, in order to download, follow the instructions.

    shell
        docker pull bjason01/python-iainteractive:latest
        docker pull bjason01/python-iainteractive:develop

### We run the development environment
In the root directory of the project.
Create a .env file, there you can custom environment variables if you need it.

     shell
        touch .env
        chmod 600 .env


You need to generate a Django Secret key to put in the env file, please go to this [website](https://www.educative.io/answers/how-to-generate-a-django-secretkey)


create the .env file

        DJANGO_SECRET_KEY=
        DJANGO_DATABASE_HOST=database
        DJANGO_DATABASE_NAME=iainteractive_db
        DJANGO_DATABASE_USER=postgres
        DJANGO_DATABASE_PASSWORD=postgres
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=postgres
        POSTGRES_DB=iainteractive_db
        
Type in the bash

        make backend
        
Inside the container 
        
        make requirements
        make

Then we need to migrate

        python src/manage.py migrate


Before running the application we need to run the frontend, go to `src/frontend` and run

        yarn install
        yarn run server

### Loading seeders

We will add data for this projects, Grimories and Magic Affinities, and in order to load, please run 

        make seed


### Running server

Now we can run the project, inside the container please

        make runserver


Then you can go to http://0.0.0.0:8000


To create a super user with the following command

        python src/manage.py createsuperuser
        # Set your username
        # Email: leave the email blank
        # Password: set the first password
        # Confirma Password: repeat the password


## Test

In order to have everything right, please create test and run with the command inside de container

        make test
        # This command will run 
        # python src/manage.py test iainteractive.apps.common --settings=iainteractive.settings.test
        # This is for the common app
