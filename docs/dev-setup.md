
# Welcome to banQuests!

This documents gives a brief setup and installation guide for the banQuest Django backend application.

## Prerequisites

- Must fork and clone the backend repo in your local machine

- Have Python installed (see [doc](https://wiki.python.org/moin/BeginnersGuide/Download))

- Install [PostgreSQL](https://www.postgresql.org/download/) and setup username and password for new database `banQuest`

- Install Postman for API testing (see [doc](https://www.postman.com/downloads/))

## Setup

> Depending on host OS commands might change. Setup a python alias first if required.

Please refer to `Setting up testing env using docker-compose` section for a 360 degree setup including react UI and postgre db. Or else, follow the below instructions for standalone local API app setup:

1.  **Create a virtual environment:**
	Open your terminal and, inside your _banQuest_ project folder, use the following command to create a virtual environment named **.venv**: `python -m venv .venv`

	To activate the virtual environment, enter
	
	`source .venv/bin/activate`
	
	> When you're finished with your virtual environment, enter the following command to deactivate it: `deactivate`.


2.  **Install Django:**

	Install Django in the virtual environment with the command
	`python -m pip install django`

	Verify that it's installed by entering
	`python -m django --version`

  

3.  **Setup local database connection:**

	After `banQuest` database creation and user auth (username, password) setup, we need to set environment variables for the application to connect to the database. This can either be done manually or via shell.

	Note: environment variables > default placeholder values

	Via terminal (only for linux/OSX):

	Create an `.env` file with below data format in the project directory:

		DB_NAME=banQuest
		DB_USER=example
		DB_PASSWORD=example@123
		DB_HOST=111.222.333.444
		DB_PORT=5432

	- next run `source .env`
	
	Or manually update the `banquest/settings.py` file to establish Django-DB connection.
	Edit the `DATABASE` section of the settings file replacing all the local PostgreSQL placeholders like USER, PASSWORD, and HOST.

	Now run the following commands to run migrations on the database:

		# Generate a new migration for the changes in your models
		python manage.py makemigrations
		# Apply the migrations to your database
		python manage.py migrate

4.  **Run on development server:**

	The `scripts/runlocal.py` platform independent script provides the automation to set env vars, install requirements, then start local server on port :8000 with a single command for local testing, 
	
	`python scripts/runlocal.py` [assuming .env file has been created with proper env vars]
	
	But for more customization the manual procedure mentioned below can be used.
	Let’s verify your Django project works. Change into the outer `banQuest` directory, if you haven’t already, and run the following commands:
	
	`python manage.py runserver`

	You’ll see the following output on the command line:
	
		Performing system checks...
		System check identified no issues (0 silenced).
		You have unapplied migrations; your app may not work properly until they are applied.
		Run 'python manage.py migrate' to apply them.
		February 17, 2024 - 12:20:32
		Django version 5.0, using settings 'banquest.settings'
		Starting development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
		Quit the server with CONTROL-C.

	> If you want to use a different port than the default 8000, specify the port number on the command line, such as `python3 manage.py runserver 5000`.

-  `Ctrl+click` the `http://127.0.0.1:8000/` URL in the terminal output window to open your default browser to that address. If Django is installed correctly, you'll see a default page.

  

- When you're done, close the browser window and stop the server using `Ctrl+C` as indicated in the terminal output window.

  

## API Testing (Manual)

1. Start the web server with the following command:

	`python scripts/runlocal.py`

2. [TBD] Use the template collection to access api configurations.

3. Or simply use your test API URL to [test the request on Postman](https://www.geeksforgeeks.org/basics-of-api-testing-using-postman/).

	> _Note_: Alternatively you can also use curl for testing API response
	>  `curl --request GET --url http://127.0.0.1:8000/`

4. For a new API request open an issue [here](https://github.com/dosXdev/banQuest/issues) with the appropriate API specification.

## Running tests

1. Create .env file and update database secrets

2. Run `unit-tests.py` script to run all test modules:

	`python scripts/unit-tests.py`


## Running in a container

Steps for backend containerisation using [Docker](https://docs.docker.com/desktop/):

	export API_PUSH_KEY=<YOUR_PUSH_KEY>
	docker login -u <REG_USER_NAME> -p $API_PUSH_KEY
	docker build -t <REG_USER_NAME>/banquest:<TAG> .
	docker push <REG_USER_NAME>/banquest:<TAG>
	docker run --env-file .env --name banquest-app-c1 -p 8000:8000 -d banquest:<TAG>

> _Note_: Default backend appilication image for running BanQuest inside of a container is still a WIP

## Setting up testing env using `docker-compose`:

1. For `docker-compose` to run we assume you have both the frontend and backend repo cloned inside a parent directory.
2. `cd` into the backend repo (banQuest) and run the following command `docker-compose up --build`

	> _Note: You can replace the hardcoded env vars in the docker-compose file as need be_

3. This should build and bring up both the React and Django apps along with a postgresql instance. 
4. APIs should be accessible at port `:8000` and the UI at port `:3000`.